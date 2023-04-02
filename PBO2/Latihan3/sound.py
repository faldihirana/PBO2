from gtts import gTTS

kalimat = "hallo nama saya faldi"
bahsa = "id"

filesaya = gTTS (text=kalimat, lang=bahsa)

filesaya.save("Tugas3.mp3")
print("file tersimpan")