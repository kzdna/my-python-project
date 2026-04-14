import requests
import json

def emotion_detector(text_to_analyse):
    # Pastikan URL-nya persis seperti ini
url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header untuk model yang digunakan
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Data input dalam format JSON
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Mengirim request POST ke API
    response = requests.post(url, json = myobj, headers=header)
    
    # Mengubah respon teks JSON menjadi Dictionary Python menggunakan json.loads
    formatted_response = json.loads(response.text)
    
    # Mengekstrak set emosi dari respon (mengambil elemen pertama dari emotionPredictions)
    # Jika respon sukses, struktur datanya adalah: formatted_response['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Menentukan emosi dengan skor tertinggi (dominant emotion)
    # Kita mencari key (nama emosi) yang memiliki value (skor) terbesar
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Menyusun hasil akhir dalam format dictionary sesuai instruksi tugas
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result
