from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Mengambil teks yang diinput user dari argumen URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Menjalankan fungsi deteksi emosi
    response = emotion_detector(text_to_analyze)

    # Jika dominant_emotion adalah None (untuk Task 9 nanti), 
    # tapi untuk sekarang kita ikuti alur standar dulu:
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Mengembalikan output dalam format string yang diminta
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
