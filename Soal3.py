import tester

tester.start("input.txt")

file = open("input.txt", "r")

# Tulis program kalian disini
line1 = file.readline()
hitung = 0
for i in range(int(line1)):
    line = file.readline()
    arr = line.split(" ")
    arr[len(arr)-1] = arr[len(arr)-1].rstrip()
    for j in range(len(arr)):
        hitung += int(arr[j])

print(hitung)
    

tester.end("input.txt")
