import random

# Meminta input jumlah data
N = int(input("Masukkan nilai N: "))

for i in range(N):
    data = random.random()  # Menghasilkan angka acak antara 0 dan 1
    print("data ke:", i+1, "=>", data)

print("Selesai")