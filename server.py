from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Ini data bohongan supaya tombol Analyze muncul hasilnya
    response = {
        'anger': 0.01,
        'disgust': 0.01,
        'fear': 0.01,
        'joy': 0.96,
        'sadness': 0.01,
        'dominant_emotion': 'joy'
    }
    
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    # Menampilkan halaman utama (index.html)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
