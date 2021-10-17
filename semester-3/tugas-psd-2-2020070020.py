# PRAKTIKUM
# Kegiatan 1: Membuat Class dan Objek
class Mobil:
    def __init__(self):
        self.warna = 'Hitam'
        self.tipe = 'Sedan'
        print ('Objek telah dibuat')

    def maju(self):
        print ('maju')

    def mundur(self):
        print ('mundur')

    def melaju(self, speed):
        print ('melaju dengan kecepatan %s km/jam' % speed)

# membuat objek pertama
mobil1 = Mobil()
print (mobil1.warna)
mobil1.maju()
mobil1.melaju(100)

# membuat objek kedua
mobil2 = Mobil()
print (mobil2.tipe)
mobil2.mundur()
mobil2.melaju(150)

# Latihan 1
# 1. Memodifikasi class Mobil dan membuat 3 objek baru di dalamnya
class Mobil:
    def __init__(self):
        self.merk = 'Ford'
        self.warna = 'Ungu'
        self.kapasitas = '8 orang'
        self.posisi_setir = 'kanan'
        print ('Objek telah dibuat')

    def gas(self, injak):
        print ('gass dengan %s' % injak)

    def rem(self, injak):
        print ('rem dengan %s' % injak)

    def reting(self, arah, waktu):
        print ('reting ' + arah + ' dalam waktu ' + str(waktu) + ' detik')

# 2. Membuat class KucingObjek
class KucingObjek:
    def __init__(self):
        self.umur = '2 Tahun'
        self.warnabulu = 'Hitam'

    def meong(self):
        print ('Meooongggg!')

    def umur(self, usia):
        print ('umur meong sudah %s tahun' % usia)

# Kegiatan 2: Method Objek dan Init
class Orang:
    # method __init__
    def __init__(self,nama):
        self.nama = nama

    # deklarasi method
    def katakanSalam(self):
        print ("Assalamu'alaikum, " %self.nama)

org = Orang()
org.katakanSalam()

# Latihan 2
# 1. Membuat class PersegiPanjang dengan dua method
class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        print (self.panjang*self.lebar)
        #print ("Luas persegi panjang dengan dimensi " + str(self.panjang) + "x" + str(self.lebar) + " sama dengan " + self.panjang*self.lebar + "satuan luas")

    def keliling(self):
        print (2*(self.panjang+self.lebar))
        #print ("Keliling persegi panjang dengan dimensi " + str(self.panjang) + "x" + str(self.lebar) + " sama dengan " + (2*(self.panjang+self.lebar)) + "satuan panjang")

# Kegiatan 3: Variable class dan objek (instance)
class Orang:
    # variable class, untuk menghitung jumlah orang
    total = 0
    def __init__(self,nama):
        # inisiasi data, data yang dibuat pada self merupakan variable objek
        self.nama = nama
        # ketika ada orang yang dibuat, tambahkan total orang
        Orang.total += 1
    def __del__(self):
        # kurangi total orang jika obyek dihapus
        Orang.total -= 1
    def katakanHalo(self):
        print ("Halo, nama saya", self.nama, " apa kabar?")
    def total_populasi(cls):
        print ('Total Orang adalah ', cls.total)
        method class
    total_populasi = classmethod(total_populasi)

org = Orang('Budi')
org.katakanHalo()
Orang.total_populasi()

org2 = Orang('Andi')
org2.katakanHalo()
Orang.total_populasi()
print ('objek dihapus')

del org
del org2
Orang.total_populasi()

# TUGAS
# 1. Class Hewan
class Hewan():
    def __init__(self,nama,jumlah_kaki,makanan,type_hewan):
        self.nama = nama
        self.jumlah_kaki = jumlah_kaki
        self.makanan = makanan
        self.type_hewan = type_hewan
        print ('Nama Hewan : ', self.nama)
        print ('Jumlah Kaki : ', self.jumlah_kaki)
        print ('Makanan : ', self.makanan)
        print ('Type Hewan : ', self.type_hewan)

# 2. Class Mahasiswa
class Mahasiswa():
    def __init__(self,nama,nim,alamat,semester):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.semester = semester
    def tampilkanNama(self):
        print ('Nama :', self.nama)
    def tampilkanNim(self):
        print ('Nim :', self.nim)
    def tampilkanAlamat(self):
        print ('Alamat :', self.alamat)
    def tampilkanSemester(self):
        print ('Semester :', self.semester)
