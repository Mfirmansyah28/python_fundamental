nilai = 81
perilaku = 'Tidak Baik'

if nilai >= 80 and perilaku == 'Baik':
    print("Selamat! anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")

elif nilai >= 80 and perilaku != 'Baik':
    print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
    print("Perbaiki lagi ya!.")

else:
    print("Yuk belajar lebih giat lagi!.")