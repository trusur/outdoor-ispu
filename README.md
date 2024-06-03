# Outdoor Display 7 Parameter KLHK (main)

## Langkah Instalasi
1. Download aplikasi outdor di : `https://github.com/trusur/outdoor-ispu`
2. Extract file `outdoor-ispu.zip`
3. Buka file config.cfg di Notepad lalu sesuaikan ID Stasiun terkait
4. Klik kanan pada file outdoor.exe, buat shortcut
5. Copy shortcut dari file outdoor.exe
6. Ketik Windows + R, lalu masukan command `shell:startup`
7. Paste shortcut di folder tsb
8. Paste juga di desktop jika diperlukan
9. Jalankan software oudoor dari shortcut yang ada di desktop

## Common Troubleshoot:
1. Jika file `outdoor.exe` tidak bisa dijalankan, cobalah install [dotnet-sdk-3.1.413-win-x86.exe](https://dotnet.microsoft.com/en-us/download/dotnet/3.1)
2. Jika di papan ISPU tidak ada perubahan, periksa koneksi LAN dari mini PC ke Controller dengan cara test ping ke IP Controller yaitu: `192.168.2.200`.
3. Buka terminal , masukan command `ping 192.168.2.200 -t`
4. Jika informasi yang didapat berupa Request Timed Out, transmit failed atau error lainnya. Maka harus periksa kabel LAN secara fisik
5. Ada 3 file yang biasa diubah untuk melakukan konfigurasi
    1. data.txt
        19 => Baik
        38 => Sedang
        57 => Tidak Sehat
        76 => Sangat Berbahaya
        96 => Fullbar
    2. data.temp
    3. Config.cfg isi dengan ID Stasiun
6. Jalankan file OutdoorDisplay.exe saja untuk testing bar dan pastikan file outdoor.exe tidak dijalankan
7. Jalankan file outdoor.exe untuk menjalankan aplikasi keseluruhan
