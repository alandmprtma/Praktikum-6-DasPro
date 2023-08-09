import tester

tester.start("input.txt")

file = open("input.txt", "r")

# Tulis program kalian disini
line = [0 for i in range(2)]
for i in range(2):
    line[i] = file.readline()

print(line[0])
print(line[1])

arr1 = line[0].split(" ")
arr1[len(arr1)-1] = arr1[len(arr1)-1].rstrip()
print(arr1)
arr2 = line[1].split(" ")
arr2[len(arr2)-1] = arr2[len(arr2)-1].rstrip()
print(arr2)

buah = []
for i in range (len(arr1)):
    for j in range (len(arr2)):
        if arr1[i] == arr2[j]:
            buah.append(arr1[i])
if buah == []:
    print("Tidak ada kata yang sama")

tester.end("input.txt")
"""
for i in range (len(buah)):
    for j in range (len(buah)):
        if buah[i] == buah[j]:
            buah[j] == None
print (buah)
hitungarr1 = 0
angkaarr1 = []
for i in range (len(buah)):
    for j in range (len(arr1)):
        if buah[i] == arr1[j]:
            hitungarr1 += 1
        elif buah[i] == arr1[j] and j == len(arr1)-1:
            hitungarr1 += 1
            angkaarr1.append(hitungarr1)
            hitungarr1 = 0
        elif buah[i] != arr1[j] and j == len(arr1)-1:
            angkaarr1.append(hitungarr1)
            hitungarr1 = 0
        else:
            hitungarr1 += 0
print(angkaarr1)
hitungarr2 = 0
angkaarr2 = []
for i in range (len(buah)):
    for j in range (len(arr2)):
        print(buah[i],",",arr2[j])
        if buah[i] == arr2[j]:
            hitungarr2 += 1
        elif buah[i] == arr2[j] and j == len(arr2)-1:
            hitungarr2 += 1
            angkaarr2.append(hitungarr1)
            hitungarr2 = 0
        elif buah[i] != arr2[j] and j == len(arr2)-1:
            angkaarr2.append(hitungarr1)
            hitungarr2 = 0
        else:
            hitungarr2 += 0
print(angkaarr2)

if buah == []:
    print("Tidak ada kata yang sama")
else:
    for i in range (len(buah)):
        print(buah[i],",",angkaarr1[i],",",angkaarr2[i])

tester.end("input.txt")
"""