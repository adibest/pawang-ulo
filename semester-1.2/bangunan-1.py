bata = 80
pasir = 50
semen = 10

def kebutuhan_material(pengali,permeter):
    kebutuhan_material = pengali*permeter
    return kebutuhan_material

luas_tembok = int(input("masukkan luas tembok yang akan dibangun dalam meter persegi"))

stok_bata = int(input("jumlah bata tersedia"))
def kebutuhan_bata(stok_bata):
    if stok_bata == kebutuhan_material(luas_tembok,bata):
        print('stok bata cukup')
    elif stok_bata > kebutuhan_material(luas_tembok,bata):
        print('stok bata berlebih',stok_bata - kebutuhan_material(luas_tembok,bata),'buah')
    elif stok_bata < kebutuhan_material(luas_tembok,bata):
        print('stok bata kurang',kebutuhan_material(luas_tembok,bata) - stok_bata,'buah')

# stok_pasir = int(input("jumlah pasir tersedia"))
def kebutuhan_pasir(stok_pasir):
    if stok_pasir == kebutuhan_material(luas_tembok,pasir):
        return('stok pasir cukup')
    elif stok_pasir > kebutuhan_material(luas_tembok,pasir):
        return('stok pasir berlebih',stok_pasir - kebutuhan_material(luas_tembok,pasir),'buah')
    elif stok_pasir < kebutuhan_material(luas_tembok,pasir):
        return('stok pasir kurang',kebutuhan_material(luas_tembok,pasir) - stok_pasir,'buah')

# stok_semen = int(input("jumlah semen tersedia"))
def kebutuhan_semen(stok_semen):
    if stok_semen == kebutuhan_material(luas_tembok,semen):
        return('stok semen cukup')
    elif stok_semen > kebutuhan_material(luas_tembok,semen):
        return('stok semen berlebih',stok_semen - kebutuhan_material(luas_tembok,semen),'buah')
    elif stok_semen < kebutuhan_material(luas_tembok,semen):
        return('stok semen kurang',kebutuhan_material(luas_tembok,semen) - stok_semen,'buah')