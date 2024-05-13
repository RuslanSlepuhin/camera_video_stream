import cv2
import numpy as np
from flask import Flask, Response

app = Flask(__name__)

@app.route('/stream')
def stream():
    # Открытие камеры
    cap = cv2.VideoCapture(0)
    while True:
        # Чтение кадра
        ret, frame = cap.read()
        # Преобразование кадра в JPEG
        _, jpeg = cv2.imencode('.jpg', frame)
        # Отправка кадра в виде потока
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8554)
