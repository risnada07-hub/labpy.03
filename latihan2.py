# Program menghitung total laba perusahaan selama 8 bulan

# Inisialisasi variabel
laba = 0
modal_awal = 100000000  # contoh modal awal (tidak digunakan langsung di output)
bulan = 8
total_laba = 0

for i in range(1, bulan + 1):
    if i == 1 or i == 2:
        laba = 0
    elif i == 3 or i == 4:
        laba = 10000000
    elif i == 5 or i == 6 or i == 7:
        laba = 50000000
    else:
        laba = 20000000

    print(f"laba bulan ke- {i} sebesar: {laba}")
    total_laba += laba

print("Total laba adalah:", total_laba)
