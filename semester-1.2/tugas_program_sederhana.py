# Program Menghitung Karakter dan Kata Dalam Kalimat

def sentences():
    return input("Beri saya suatu kalimat : ")

kalimat = sentences()
deret_kata = kalimat.split()
jumlah_kata = len(deret_kata)
total_huruf = 0

# ini adalah alternatif lain fungsi len()
for i in kalimat:
    total_huruf = total_huruf + 1

if ((total_huruf % 2 == 1) and (jumlah_kata % 2 == 1)):
    print("Jumlah karakter pada kalimat yang anda tulis adalah",total_huruf,"karakter.")
    print("Dan ada",jumlah_kata,"kata")
    print("Jumlah karakternya ganjil, jumlah katanya ganjil")
elif ((total_huruf % 2 == 1) and (jumlah_kata % 2 == 0)):
    print("Jumlah karakter pada kalimat yang anda tulis adalah",total_huruf,"karakter.")
    print("Dan ada",jumlah_kata,"kata")
    print("Jumlah karakternya ganjil, jumlah katanya genap")
elif ((total_huruf % 2 == 0) and (jumlah_kata % 2 == 1)):
    print("Jumlah karakter pada kalimat yang anda tulis adalah",total_huruf,"karakter.")
    print("Dan ada",jumlah_kata,"kata")
    print("Jumlah karakternya genap, jumlah katanya ganjil")
else:
    print("Jumlah karakter pada kalimat yang anda tulis adalah",total_huruf,"karakter.")
    print("Dan ada",jumlah_kata,"kata")
    print("Jumlah karakternya genap, jumlah katanya genap")