def main_menu():
    print('')
    n = raw_input('Masukkan Nama Anda: ')
    print('Nama Pemesan: ',n)
    print("Masukkan Pilihan")
    print("1. Lanjutkan")
    print("2. Kembali")
    print('')

def second_menu():
    print("Masukkan Pilihan")
    print("1. Lanjutkan")
    print("2. Kembali")
    print('')

class tiket_on_stage():
    def reguler (a,b):
        jumlah_pesan = b * 100000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 100000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan
    def medium (a,b):
        jumlah_pesan = b * 150000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 150000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan
    def premium (a,b):
        jumlah_pesan = b * 250000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 250000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan

class tiket_online():
    def reguler (a,b):
        jumlah_pesan = b * 20000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 20000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan
    def medium (a,b):
        jumlah_pesan = b * 30000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 30000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan
    def premium (a,b):
        jumlah_pesan = b * 50000
        pajak = jumlah_pesan * 0.02
        total = jumlah_pesan + pajak
        print('Harga Tiket = Rp 50000')
        print('')
        print('Total Tiket = Rp '), jumlah_pesan
        print('Pajak = Rp '), pajak
        print('________________________+')
        print('Total Seluruhnya = Rp '), total
        return jumlah_pesan

def back_menu():
    print ('Apakah anda ingin memesan tiket lagi? [Y/N] :')
    back = raw_input().upper()
    if back == "Y":
        second_menu()
        pilihan()
        print("")
    else:
        print('Terima Kasih !')
        exit

def pilihan():
    b = input('Masukkan Pilihan: ')
    if b == 1:
    
    pil == 1
    tos = tiket_on_stage()
    while pil !=4:
        print("Pilih Tiket")
        print("1. Reguler")
        print("2. Medium")
        print("3. Premium")
            pil = int(input('Masukkan pilihan anda: '))
            print
            if pil == 1:
                print('')
                b = input('Jumlah Pesan : ')
                tos.reguler(b)
                pil(4)

            if pil == 2:
                print('')
                b = input('Jumlah Pesan : ')
                tos.medium(b)
                pil(4)
            
            if pil == 3:
                print('')
                b = input('Jumlah Pesan : ')
                tos.premium(b)
                pil(4)

    pil == 0
    to = tiket_online()
    while pil !=4:
        print("Pilih Tiket")
        print("1. Reguler")
        print("2. Medium")
        print("3. Premium")
            pil = int(input('Masukkan pilihan anda: '))
            print
            if pil == 1:
                print('')
                b = input('Jumlah Pesan : ')
                to.reguler(b)
                pil(4)

            if pil == 2:
                print('')
                b = input('Jumlah Pesan : ')
                to.medium(b)
                pil(4)
            
            if pil == 3:
                print('')
                b = input('Jumlah Pesan : ')
                to.premium(b)
                pil(4)

            else:
                exit
main_menu()
pilihan()