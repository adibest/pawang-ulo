def main():
    f=open("python.txt","r")
    print("Nama file:",f.name)
    print("Mode Akses:",f.mode)
    # print(f.read())
    print(f.readlines())

if __name__ == "__main__":
    main()