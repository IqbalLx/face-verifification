Quickstart:
- Untuk melakukan input wajah baru gunakan command "python input_face.py" di dalam folder ini
    - Tekan tombol 'c' untuk melakukan capture data wajah sebanyak 10x
    - Tekan tombol 't' untuk memulai proses training agar data wajah dikenali
    - Terakhit, tekan tombol 'x' saat proses sudah selesai untuk keluar program

- Untuk mencoba hasil training model, gunakan command "python recog_face.py"
    - Maka jendela baru akan tampil dan menampilkan Face Recognition terhadap wajah yang
      terdeteksi di kamera
    - Proses Recognition menggunakan metode LBPH yang mengukur seberapa dekat jarak wajah saat ini
      dengan wajah yang sudah disimpan di database, semakin dekat jaraknya (angka yang muncul kecil) 
      maka semakin bagus.
    - Konfigurasi saat ini jika jarak yang dihitung lebih kecil dari 50 maka ditampilkan. Sementara
      yang lebih akan dibuang dan ditampilkan sebagai Unknown.
    
Penjelasan Detail:
- Metode deteksi wajah menggunakan algoritmal Viola-Jones
- Metode rekognisi wajah menggunakan metode LBPH (Local Binary Pattern Histogram)
- Database yang digunakan untuk menampung ID dan Nama adalah SQLite3
- Library yang dipakai antara lain: OpenCV, NumPy, dan Sqlite3

- Script input_face.py
  Dalam script ini dilakukan proses deteksi wajah, ketika user menekan tombol 'c' untuk 
  capture wajah maka wajah saat ini (yang terdeteksi) akan disimpan dalam folder "data".
  Setelah 10 wajah berhasil disimpan maka dilakukan proses "fitting" atau training agar
  model dapat mengenali fitur wajah tersebut berasosiasi dengan ID yang mana.
  Setelah proses training selesai maka akan dihasilkan file "recognizer.yml" pada 
  folder "model". 
  Penjelasan script lebih lanjut sebagian besar sama dengan video yang ada di YouTube saya 

- Script face_recog.py
  Dalam script ini dilakukan proses rekognisi wajah dengan mengukur jarak histogram data wajah
  saat ini dengan yang sudah ada di model. Seluruh proses kurang lebih sama dengan video yang
  ada di YouTube saya, bedanya saat ini adalah proses penampilan nama berdasarkan nama yang telah 
  disimpan di dalam database.