import cv2

import model
import database
import config
import utils

"""
File untuk melakukan proses Input Data Wajah. Wajah akan diproses,
diekstrak nilainya dan dilakukan klasifikasi wajah termasuk
kelas yang mana
"""


model = model.Model()
db = database.Database()
db.create_table()

face_cascade = cv2.CascadeClassifier(config.FACE_CASCADE_PTH)
ids = int(input("[INFO] Masukkan ID Unik: "))
name = input("[INFO] Masukkan Nama: ")

cam = cv2.VideoCapture(1)                                           # Akses Kamera

key = None
counter = 0
while True:
    ret, frame = cam.read()                                         # Membaca setiap frame dari stream kamera
    frame_copy = frame.copy()                                       # Copy frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                  # Mengubah mode BGR ke GRAY (hitam putih)
    
                                                                    # Proses pencarian wajah 
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)             # <cascade_file>.detectMultiScale(<frame>, <scale_factor>, <min_neighbors>)
    for x, y, w, h in faces:                                        # Looping semua wajah yang terdeteksi
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)    # Gambar box untuk setiap wajah
        
        if key == ord('c'):                       # Menunggu tombol c di tekan
            roi_face = frame_copy[y:y+h, x:x+w]                     # region of interest dari frame
            cv2.imwrite(f'{config.DATA_ROOT}/people.{ids}.{counter}.jpg',# write region wajah
                        roi_face)
            
            utils.pretty_print(config.TOTAL_DATA, counter,
                                custom_processing='Press (c)apture again ...')
            counter += 1
            if counter >= config.TOTAL_DATA:
                print(f'[INFO] {config.TOTAL_DATA} IMAGE CAPTURED!')     # info done proses
                counter = 0

        elif key == ord('t'):
            model.train()
            db.insert_user(ids, name)
        
    cv2.imshow('Face Detect Video', frame)                          # Jendela untuk menampilkan hasil
    key = cv2.waitKey(1) & 0xff
    if key == ord('x'):                                            # Exit dengan tombol x
        break
        
cam.release()                                                       # Menyudahi akses kamera
cv2.destroyAllWindows()                                             # Menutup jendela

db.close()
