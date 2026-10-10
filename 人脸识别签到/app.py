# -*- coding: utf-8 -*-
"""人脸识别签到系统 - Gradio 网页界面

启动：python app.py，浏览器访问 http://127.0.0.1:7860
- 注册人脸：填写姓名 + 上传一张或多张照片（支持正脸清晰的证件照/自拍）
- 识别签到：上传或摄像头拍摄 -> 框出人脸并显示姓名与置信度，签到记录写入 data/attendance.csv
"""
import os

import cv2
import gradio as gr
import numpy as np

import face_core


def _to_bgr(img):
    """Gradio 传入 RGB ndarray，转为 OpenCV BGR"""
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) if img is not None else None


def do_register(name, files):
    if not (name or "").strip():
        return "请填写姓名"
    paths = []
    for f in files or []:
        p = f if isinstance(f, str) else getattr(f, "name", None)
        if p and os.path.exists(p):
            paths.append(p)
    if not paths:
        return "请至少上传一张照片"
    try:
        ok, fail = face_core.register_person(name, paths)
    except Exception as e:  # 训练失败等异常直接反馈到界面
        return f"注册失败：{e}"
    msg = f"注册成功：{name}（成功 {ok} 张，已重新训练模型）"
    if fail:
        msg += f"，{fail} 张未检测到人脸已跳过"
    return msg


def do_recognize(img):
    if img is None:
        return None, "请上传照片或开启摄像头"
    try:
        annotated, text = face_core.recognize(_to_bgr(img))
    except Exception as e:
        return None, f"识别失败：{e}"
    return cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB), text


with gr.Blocks(title="人脸识别签到系统") as demo:
    gr.Markdown("# 人脸识别签到系统\n"
                "基于 OpenCV：Haar 级联人脸检测 + LBPH 特征识别，签到记录自动留存")
    with gr.Tab("注册人脸"):
        name_in = gr.Textbox(label="姓名")
        files_in = gr.File(label="人脸照片（可多张，需包含清晰正脸）",
                           file_count="multiple", file_types=["image"])
        reg_btn = gr.Button("注册并训练", variant="primary")
        reg_out = gr.Textbox(label="注册结果")
    with gr.Tab("识别签到"):
        cam_in = gr.Image(label="上传照片或开启摄像头", sources=["upload", "webcam"])
        rec_btn = gr.Button("识别并签到", variant="primary")
        rec_img = gr.Image(label="识别结果")
        rec_out = gr.Textbox(label="签到信息")

    reg_btn.click(do_register, [name_in, files_in], reg_out)
    rec_btn.click(do_recognize, cam_in, [rec_img, rec_out])

if __name__ == "__main__":
    demo.launch()
