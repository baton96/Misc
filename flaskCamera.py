import cv2
from flask import Flask, Response

cam = cv2.VideoCapture(0)
app = Flask(__name__)


@app.route('/')
def index():
    return '''
<html>
  <body>
    <img src="{{ url_for('video_feed') }}">
  </body>
</html>'''


def gen():
    while True:
        frame = cv2.imencode('.jpg', cam.read()[1])[1].tobytes()
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run()
