def insertionSort(listku):
    for index in range(1, len(listku)):
        Kanan = listku[index]
        Kiri = index - 1
        while Kiri >=0  and listku[Kiri] > Kanan:
            listku[Kiri + 1] = listku[Kiri]
            Kiri -= 1
            listku[Kiri + 1] = Kanan
            index = 0

panjangList = int(input("Panjang data yang diinginkan = "))
listku=[]
for i in range(1, panjangList+1):
    angka = int(input("Masukkan data yang ke %i untuk list = " %i))
    listku.append(angka)

print("Sebelum di insertion sort = ")
print(listku)
insertionSort(listku)
print("Setelah di insertion sort = ")
print(listku)