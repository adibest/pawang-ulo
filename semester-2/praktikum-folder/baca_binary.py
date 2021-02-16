f = open("bfile.img","wb+")
message = "Hello Python"
encode = message.encode("utf-16")
f.write(encode)
f.seek(0)
bdata = f.read()
print ("Binary Data:",bdata)
decode = bdata.decode("utf-16")
print ("Normal Data:",decode)