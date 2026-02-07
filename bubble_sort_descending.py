bubble_sort_descending.py
# Nama pembuat
nama_pembuat = "Iche Wanenda"

angka = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

n = len(angka)

for i in range(n):
    for j in range(0, n - i - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

print("Hasil pengurutan dari besar ke kecil:")
print(angka)
