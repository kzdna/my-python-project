# 1. Panggil fungsi detector
response = emotion_detector(text_to_analyze)

# 2. Ambil dominant_emotion-nya dulu
dominant_emotion = response['dominant_emotion']

# 3. CEK DULU DI SINI (Error Handling)
if dominant_emotion is None:
    return "Invalid text! Please try again!."

# 4. Kalau tidak None, baru jalankan return yang panjang (angka-angka)
return (
    f"For the given statement, the system response is 'anger': {response['anger']}... "
    f"The dominant emotion is {dominant_emotion}."
)
