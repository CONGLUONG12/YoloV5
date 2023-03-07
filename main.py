import numpy as np
from PIL import Image as pil_image
import cv2
from flask import Flask
import pickle
from flask import Flask, render_template, request
from flask import jsonify
import requests
import torch
from PIL import Image
import requests
from io import BytesIO
import tqdm
import os

def detect_image(img, model):
    detect = model(img)

    if 'no detections' in str(detect):
        return 1
    else:
        conf = detect.pandas().xyxy[0]['confidence']
        for c in conf:
            if c > 0.75:
                return 0 
    return 1

def detect_video(video, model): 
    vidcap = cv2.VideoCapture(video)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS)) 
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = int(frame_count/100)

    if duration == 0:
        duration = 1
   
    success, image = vidcap.read()

    count = 0
    stt = []
    check = False
    while success:
        if count % (duration) == 0: 
            cv2.imwrite("frames_video/frame%d.jpg" % count, image)
            stt.append(count)
            result = detect_image(f"frames_video/frame{count}.jpg", model)
            if result == 0:
                check = True
                break
        success,image = vidcap.read()
        count += 1

    for j in stt:
        os.remove(f'frames_video/frame{j}.jpg')
    if check == True:
        return 0
    return 1
  
def detect(contents):
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./exp4/weights/last.pt', force_reload=True)
    # if request.method == "POST":
    # Lấy file gửi lên
    paths = []
    re = []
    keys = contents.keys()
    correct_keys = ['link', 'type', 'object_id']
    for k in correct_keys:
        if k not in keys:
            result = dict()
            result['status'] = 400
            result['message'] = 'Bad Request'
            return result

    for content in contents["link"]:
        if content.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', 'gif', 'psd', 'pdf')):
            try: 
                response = requests.get(content)
                img = Image.open(BytesIO(response.content))
            except: 
                result = dict()
                result['status'] = 404
                result['message'] = 'Not Found'
                return result
            paths.append(content)
            re.append(detect_image(img, model))

        elif content.lower().endswith(('.avi', '.mp4', '.mkv', '.wmv', 'vob', 'flv')):
            try:
                page = requests.get(content, stream = True, timeout = 1)
            except:
                result = dict()
                result['status'] = 404
                result['message'] = 'Not Found'
                return result

            if page.status_code == 200:
                paths.append(content)
                re.append(detect_video(content, model))
            else:
                result = dict()
                result['status'] = page.status_code
                result['message'] = page.reason
                return result
        else:
            result = dict()
            result['status'] = 400
            result['message'] = 'Bad Request'
            return result

    # [{link_hinh:"http://linkhinh.png", status:1}, {link_hinh:"http://linkhinh.png", status:0}]
    check = []
    for i in range(len(paths)):
        temp = dict()
        temp['link_hinh'] = paths[i]
        temp['status'] = re[i]
        check.append(temp)

    result = dict()
    result['object_id'] = contents["object_id"]
    result['status'] = 200
    result['message'] = "OK"
    result['data'] = check
    return result

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)

