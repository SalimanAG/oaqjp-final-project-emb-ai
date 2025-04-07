from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    respon = emotion_detector(text_to_analyze)

    return f"For the given statement, the system response is 'anger': {respon['anger']}, "\
        f"'disgust': {respon['disgust']}, 'fear': {respon['fear']}, 'joy': {respon['joy']} "\
        f"and 'sadness':{respon['sadness']}. The dominant emotion is {respon['dominant_emotion']}."


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)