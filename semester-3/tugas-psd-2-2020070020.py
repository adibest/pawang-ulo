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
