def cekfile(nama_berkas):
    ada = True
    try:
        f = open (nama_berkas)
    except IOError:
        ada = False
    return ada

a = cekfile("python.txt")
print(a)