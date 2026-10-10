# -*- coding: utf-8 -*-
"""人脸识别核心模块：Haar 级联人脸检测 + LBPH 特征训练 / 识别 + 签到记录"""
import json
import os
import shutil
import tempfile
from datetime import datetime

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FACE_DIR = os.path.join(BASE_DIR, "data", "faces")
MODEL_PATH = os.path.join(BASE_DIR, "data", "model.yml")
LABELS_PATH = os.path.join(BASE_DIR, "data", "labels.json")
ATTENDANCE_CSV = os.path.join(BASE_DIR, "data", "attendance.csv")
UNKNOWN = "Unknown"
CONF_THRESHOLD = 70  # LBPH 置信度（距离）阈值：超过视为陌生人

_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def _imread(path):
    """兼容中文路径读图"""
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)


def _imread_gray(path):
    """兼容中文路径读灰度图"""
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_GRAYSCALE)


def _imwrite(path, img):
    """兼容中文路径写图"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ext = os.path.splitext(path)[1] or ".png"
    ok, buf = cv2.imencode(ext, img)
    buf.tofile(path)
    return ok


def detect_faces(bgr):
    """检测图中人脸，返回框列表 [(x, y, w, h), ...]"""
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    faces = _cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5, minSize=(60, 60))
    return [tuple(map(int, f)) for f in faces]


def _largest_face_gray(bgr):
    """取最大人脸并统一为 200x200 灰度图，未检测到返回 None"""
    faces = detect_faces(bgr)
    if not faces:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    return cv2.resize(gray[y:y + h, x:x + w], (200, 200))


def _load_labels():
    if os.path.exists(LABELS_PATH):
        with open(LABELS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"next_id": 1, "names": {}}  # names: 姓名 -> 数字标签


def train():
    """遍历人脸库训练 LBPH 模型并保存，返回训练样本数"""
    labels = _load_labels()
    samples, ids = [], []
    for name, pid in labels["names"].items():
        pdir = os.path.join(FACE_DIR, name)
        if not os.path.isdir(pdir):
            continue
        for fn in os.listdir(pdir):
            img = _imread_gray(os.path.join(pdir, fn))
            if img is not None:
                samples.append(img)
                ids.append(pid)
    if not samples:
        raise ValueError("人脸库为空，请先注册人脸")
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(samples, np.array(ids))
    _model_write(model)
    return len(samples)


def _model_write(model):
    """cv::FileStorage 不支持中文路径，经临时 ASCII 路径中转保存"""
    tmp = os.path.join(tempfile.gettempdir(), "lbph_model_tmp.yml")
    model.write(tmp)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    shutil.copyfile(tmp, MODEL_PATH)
    os.remove(tmp)


def register_person(name, image_paths):
    """注册人脸：逐张检测裁剪入库后重新训练。返回 (成功张数, 失败张数)"""
    name = (name or "").strip()
    if not name:
        raise ValueError("姓名不能为空")
    labels = _load_labels()
    if name not in labels["names"]:
        labels["names"][name] = labels["next_id"]
        labels["next_id"] += 1
    person_dir = os.path.join(FACE_DIR, name)
    ok = fail = 0
    for i, p in enumerate(image_paths, 1):
        img = _imread(p)
        if img is None:
            fail += 1
            continue
        face = _largest_face_gray(img)
        if face is None:
            fail += 1
            continue
        _imwrite(os.path.join(person_dir, f"{datetime.now():%Y%m%d%H%M%S}_{i}.png"), face)
        ok += 1
    if ok == 0:
        return 0, fail
    with open(LABELS_PATH, "w", encoding="utf-8") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)
    train()
    return ok, fail


def _load_model():
    if not os.path.exists(MODEL_PATH):
        raise ValueError("尚未训练模型，请先注册人脸")
    model = cv2.face.LBPHFaceRecognizer_create()
    tmp = os.path.join(tempfile.gettempdir(), "lbph_model_read.yml")
    shutil.copyfile(MODEL_PATH, tmp)
    model.read(tmp)
    os.remove(tmp)
    return model


def _log_attendance(name):
    """写入签到记录（CSV），同人同日仅记一次。返回是否新写入"""
    os.makedirs(os.path.dirname(ATTENDANCE_CSV), exist_ok=True)
    today = f"{datetime.now():%Y-%m-%d}"
    if os.path.exists(ATTENDANCE_CSV):
        with open(ATTENDANCE_CSV, "r", encoding="utf-8") as f:
            for line in f.read().splitlines():
                if "," in line:
                    n, t = line.rsplit(",", 1)
                    if n == name and t.startswith(today):
                        return False
    with open(ATTENDANCE_CSV, "a", encoding="utf-8") as f:
        f.write(f"{name},{datetime.now():%Y-%m-%d %H:%M:%S}\n")
    return True


def recognize(bgr, log_attendance=True):
    """识别图中所有人脸并标注，返回 (标注图, 结果文本)"""
    model = _load_model()
    labels = _load_labels()
    id2name = {v: k for k, v in labels["names"].items()}
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lines = []
    for x, y, w, h in detect_faces(bgr):
        face = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
        pid, conf = model.predict(face)
        name = id2name.get(pid, UNKNOWN) if conf <= CONF_THRESHOLD else UNKNOWN
        color = (0, 160, 0) if name != UNKNOWN else (0, 0, 220)
        cv2.rectangle(bgr, (x, y), (x + w, y + h), color, 2)
        text = name if name != UNKNOWN else UNKNOWN
        cv2.putText(bgr, f"{text} {conf:.0f}", (x, max(y - 8, 16)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        if name != UNKNOWN and log_attendance:
            lines.append(f"{name} 签到成功（置信度 {conf:.1f}）"
                         if _log_attendance(name)
                         else f"{name} 今日已签到（置信度 {conf:.1f}）")
        else:
            lines.append(f"陌生人（置信度 {conf:.1f}）")
    return bgr, "\n".join(lines) if lines else "未检测到人脸"
