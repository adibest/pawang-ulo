# Ini adalah list santri
print ("// Ini adalah list santri")
santri = ['adi', 'anwar', 'arif', 'riza', 'hana']
print (santri)
# Menampilkan indeks nomor 3
print ("// Menampilkan indeks nomor 3")
print (santri[3])
# Menghitung panjang list
print ("// Menghitung panjang list")
panjang = len (santri)
print (panjang)
# Menampilkan semua data dengan perulangan
print ("// Menampilkan semua data dengan perulangan")
for i in santri:
	print (i)

# Dictionary warna alam
print ("// Dictionary warna alam")
warna_alam = {
	'Daun':'Hijau', 
	'Kayu':'Coklat', 
	'Langit':'Merah', 
	'Batu':'Hitam', 
	'Mendung':'Kelabu'
}
# Mengakses warna
print (warna_alam)
# Menampilkan salah satu warna alam
x = warna_alam.get('Daun')
print (x)
# Menampilkan data keseluruhan menggunakan loop
for i in warna_alam:
	print (i, ':', warna_alam[i])
# Mengupdate data dictonary
warna_alam['Laut'] = 'Biru'
warna_alam['Terong'] = 'Ungu'
print (warna_alam)
# Menghapus salah satu data pada Dictionary
warna_alam.pop('Daun')
print (warna_alam)