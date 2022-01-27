def tukar(lists,i,j):
    lists[i], lists[j] = lists[j], lists[i]

def bubble(listku):
    perubahan = True
    sesi = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and perubahan:
        perubahan = False
        j=1
        while j < sesi:
            if listku[j] < listku[j-1]:
                perubahan = True
                tukar(listku, j, j-1)
            j+=1
            print(listku)
            # jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi
            if not perubahan:
                print("hasil akhir = %s" %str(listku))
                sesi-=1

print("===============================================")
print("sebelum Bubble Sort")
myList=[55, 21, 11, 90, 13, 76, 49, 30]
print(myList)
print("Setelah Bubble Sort")
bubble(myList)