import os
from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    # Assuming you have a video file named "sample.mp4" in the same directory as app.py
    video_path = os.path.join(os.path.dirname(__file__), 'sample.mp4')
    return render_template('hello.html', video_path=video_path)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('APP_PORT', 5000))) 