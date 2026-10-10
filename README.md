# Python W4 - Histogram

Program ini digunakan untuk melakukan:
1. Histogram Calculation
2. Histogram Equalization
3. Histogram Specification

## File yang Digunakan

Pastikan file berikut berada dalam satu folder:

- `main.py`
- `input.jpg`
- `reference.png`

## Cara Menjalankan Program

1. Buka terminal pada folder program.
2. Install library yang dibutuhkan jika belum tersedia:

```bash
pip install opencv-python numpy matplotlib
```

3. Jalankan program:

```bash
python main.py
```

## Cara Melihat Hasil

Setelah program dijalankan, akan muncul beberapa hasil pengolahan gambar:

- Input Image
- Histogram Equalization
- Reference Image
- Histogram Specification

Program juga menampilkan grafik histogram untuk masing-masing gambar:

- Histogram Input
- Histogram Equalized
- Histogram Reference
- Histogram Specification

Jika window gambar muncul terlebih dahulu, tutup window tersebut untuk melanjutkan ke window grafik histogram.

## Keterangan Histogram

- Sumbu X menunjukkan nilai intensitas piksel dari 0 sampai 255.
- Sumbu Y menunjukkan jumlah atau frekuensi piksel pada setiap nilai intensitas.
- Histogram Equalization digunakan untuk menyebarkan nilai intensitas agar kontras gambar lebih merata.
- Histogram Specification digunakan untuk menyesuaikan distribusi intensitas gambar input agar mendekati gambar reference.