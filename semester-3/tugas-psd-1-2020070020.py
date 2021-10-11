# Review Praktikum Struktur Data
# Kegiatan 1: List
[2, 5, 4.7, False]
myList = [2, 5, 4.7, False]
myList
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

# Kegiatan 2: Penggunaan method pada list
myList = [1400, 5, True, 7.3]
myList.append(False)
print(myList)
myList.insert(2, 4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(7.3))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

# Kegiatan 3: String
"Kholisatul"
myName="Kholisatul"
myName[3]
myName*2
len(myName)

# Kegiatan 4: Penggunaan metode pada String
myName
myName.upper()
myName.center(10)
myName.find('v')
myName.split('v')

# Kegiatan 5: Tuple
myTuple=(2,True,4.96)
myTuple
len(myTuple)
myTuple[0]
myTuple*3
myTuple[0:2]

# Kegiatan 6: Set
mySet
len(mySet)
False in mySet
"dog" in mySet
mySet
yourSet={99,3,100}
mySet.union(yourSet)
mySet|yourSet
mySet.intersection(yourSet)
mySet&yourSet
mySet.difference(yourSet)
mySet-yourSet
{3,100}.issubset(yourSet)
{3,100}<=yourSet
mySet.add("house")
mySet
mySet.remove(4.5)
mySet
mySet.pop()
mySet
mySet.clear()

# Kegiatan 7: Dictionary
kota={'Bali':'Denpasar','Jateng':'Solo'}
print(kota['Bali'])
kota['Jabar']='Bandung'
print(kota)
kota['Jatim']='Kediri'
print(len(kota))
for k in kota:
    print(kota[k]," berada di ", k)

# Kegiatan 8: Penggunaan metode pada Dictionary
phoneext={'nuru1':1490, 'lisa':1157}
phoneext
phoneext.keys()
list(phoneext.keys())
phoneext.values()
list(phoneext.values())
phoneext.items()
list(phoneext.items())
phoneext.get("ulya")
phoneext.get("ulya","NO ENTRY")
