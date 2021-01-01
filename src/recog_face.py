import cv2

import model
import database
import config
import utils


"""
File untuk melakukan proses Face Recognition. Wajah diukur jaraknya
dengan yang sudah ada pada database. Nama yang berasosiasi dengan
jarak wajah terdekat akan dikembalikan hasilnya
"""

model = model.Model()
recognizer = model.load()

db = database.Database()

face_cascade = cv2.CascadeClassifier(config.FACE_CASCADE_PTH)

cam = cv2.VideoCapture(1)                                           # Akses Kamera
while True:
    ret, frame = cam.read()                                         # Membaca setiap frame dari stream kamera 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                  # Mengubah mode BGR ke GRAY (hitam putih)
    
                                                                    # Proses pencarian wajah 
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)             # <cascade_file>.detectMultiScale(<frame>, <scale_factor>, <min_neighbors>)
    for x, y, w, h in faces:                                        # Looping semua wajah yang terdeteksi
        roi_gray = gray[y:y+h, x:x+w]
        ids, dist = recognizer.predict(roi_gray)
        name = db.get_name(ids)[0]                  # Prediksi wajah siapoa
        frame = utils.draw(frame.copy(), x, y, w, h, ids, name, dist)

    
    cv2.imshow('Face Recognition Video', frame)                     # Jendela untuk menampilkan hasil
    
    if cv2.waitKey(1) & 0xff == ord('x'):                           # Exit dengan tombol x
        break

cam.release()                                                       # Menyudahi akses kamera
cv2.destroyAllWindows()                                             # Menutup jendela

db.close()
