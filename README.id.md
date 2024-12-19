# Arsip Massal ke Folder

[![Bahasa Indonesia](https://img.shields.io/badge/lang-Indonesia-red)](README.id.md) <br>
[![Bahasa Inggris](https://img.shields.io/badge/lang-English-blue)](README.md)  

Skrip Python sederhana untuk mengekstrak banyak file arsip sekaligus (seperti ZIP, RAR, dan lainnya) ke dalam folder dengan nama yang sama seperti arsip tersebut. Alat ini mengotomatisasi proses ekstraksi, membuat folder yang terorganisir untuk setiap arsip, dan secara opsional menghapus file arsip asli setelah ekstraksi.

## Fitur

- Secara otomatis mengekstrak banyak arsip sekaligus.
- Membuat folder dengan nama sesuai arsip untuk organisasi yang lebih baik.
- Mendukung berbagai format arsip (ZIP, RAR, dll.).
- Secara opsional menghapus file arsip setelah ekstraksi.
- Termasuk penanganan kesalahan dan pencatatan untuk melacak progres dan masalah potensial.

## Prasyarat

- **Python 3.6+** diperlukan.
- Pustaka yang dibutuhkan: `os`, `zipfile`, `shutil`, `rarfile` (install menggunakan `pip install rarfile` jika menangani file RAR).

## Instalasi

1. Clone repositori ini:
   
   ```bash
   git clone https://github.com/your-username/batch-archives-to-folders.git
   cd batch-archives-to-folders
   ```

2. Install semua dependensi yang diperlukan:

   ```bash
   pip install rarfile
   ```

## Penggunaan

1. Tempatkan file arsip di direktori target, misalnya My Folder.

2. Jalankan skrip menggunakan Python:

   ```bash
   python batch_archives_to_folders.py
   ```
   
3. Ikuti semua prompt untuk opsi penghapusan atau input direktori.

## Argumen Opsional

- Sesuaikan jalur ekstraksi dengan memodifikasi variabel target_directory dalam skrip.
- Untuk mengaktifkan atau menonaktifkan penghapusan arsip asli setelah ekstraksi, sesuaikan pengaturan delete_after_extraction.

## Pencatatan

- Skrip ini menghasilkan file log extraction_log.txt untuk melacak file yang diekstrak, file yang dilewati, dan kesalahan yang ditemukan selama proses.

## Contoh

- Dengan struktur direktori berikut:

  ```python
  My Folder/
  ├── archive1.zip
  ├── archive2.zip
  └── archive3.rar
  ```

- Running the script will create:

  ```python
  My Folder/
  ├── archive1/
  │   └── [contents of archive1.zip]
  ├── archive2/
  │   └── [contents of archive2.zip]
  ├── archive3/
  │   └── [contents of archive3.rar]
  ```

## Catatan

- Pastikan Anda memiliki izin untuk membuat dan menghapus file di direktori target.
- Untuk menangani format tambahan di luar ZIP dan RAR, pustaka tambahan mungkin diperlukan.
