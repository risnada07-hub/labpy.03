# labpy.03
# Penjelasan Alur Algoritma Program `latihan1.py`, `latihan2.py`, dan `latihan3.py`

Repository ini berisi penjelasan alur algoritma dan hasil output dari tiga program Python dasar:  
- `latihan1.py`  
- `latihan2.py`  
- `latihan3.py`  

Semua program dijalankan menggunakan **Python 3** di terminal (CLI).

---

# Program 1 – latihan1.py
# Tujuan
Menampilkan bilangan acak yang lebih kecil dari 0.5 dengan jumlah tertentu.

# **Alur Algoritma**
1. Import modul `random` untuk menghasilkan bilangan acak.  
2. Minta input jumlah data (`N`) yang ingin ditampilkan.  
3. Lakukan perulangan sebanyak `N` kali.  
4. Pada setiap iterasi, tampilkan bilangan acak yang bernilai antara `0` dan `1`.  
5. Jika nilai bilangan acak kurang dari `0.5`, maka angka tersebut dicetak ke layar.  
6. Setelah selesai, tampilkan pesan "Selesai".

# Contoh Kode
```python
import random

N = int(input("Masukkan jumlah data: "))

for i in range(N):
    data = random.random()
    if data < 0.5:
        print("data ke-", i+1, "=", data)

print("Selesai")
