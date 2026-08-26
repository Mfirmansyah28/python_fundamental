#Perulangan While
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 #Increment


#For Bersarang
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)


#kontrol perulangan

# Break
for i in range(2):
    print("Perulangan luar:", i)
    for j in range(10):
        print("Perulangan dalam:", j)
        if j == 1:
            break


#Contoh kedua
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))


#Continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))


#Else Setelah For
number = [1, 2, 3, 4, 5]

for num in number:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")


#Else setelah While
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


#Jika mnggunakan break
n = 10
while n > 0:
    n = n - 1
    if n== 7:
        break
    print(n)

else:
    print("Loop selesai")


#Pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")


#List Comprehension
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

#Contoh lainnya
angka = [1,2,3,4]
pangkat = [n**2 for n in angka]

print(pangkat)