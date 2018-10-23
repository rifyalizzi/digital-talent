import random

# GENERATE RANDOM
nilaiTugas = []
for i in range(250):
    nilaiTugas.append(random.randrange(1,100,1))

print(nilaiTugas)


# Nilai Ganjil
for n in nilaiTugas:
    if (n % 2 == 1):
        print (n,"ganjil")
		
				
# Nilai lebih dari 70
counter = 0
for x in nilaiTugas:
    if x>=70:
        counter +=1
        print (x)
        print ("jumlah >=70 : ",counter)
		
		
# Standar deviasi
total = 0
for n in nilaiTugas:
    total = total + n 
average = total / len(nilaiTugas)

jumlah = 0
for n in nilaiTugas:
    a = (n - average)**2
    jumlah = jumlah + a
stdev = ( jumlah/(len(nilaiTugas)-1))**0.5

print("Standar Deviasi =", stdev)
print ()


# Nilai Maksimum
maksimum = 0
for n in nilaiTugas:
    if (n>maksimum):
        maksimum = n
print("Nilai maksimum adalah",maksimum)

# Nilai Minimum
minimum = 0
for n in nilaiTugas:
    if (n<minimum):
        minimum = n
print("Nilai minimum adalah",minimum)
print ()


# Modus
nilaimaks=0
modus={}
for i in nilaiTugas:
    count= nilaiTugas.count(i)
    modus.update({i:count})

for key in modus:
    if modus[key]>nilaimaks:
        nilaimaks=modus[key]

for key in modus:
    if modus[key]==nilaimaks:
         print("Nilai modus adalah", key)