f=open("biodata.txt","a")
f.writelines(["\n",input('Masukkan input: ')])
f.writelines(["\n",input('Masukkan input: ')])
f.writelines(["\n",input('Masukkan input: ')])
f.close()

with open("biodata.txt","r") as file:
    file = file.read()
    print (file)