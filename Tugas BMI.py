
weight = 90
height = 169

#Formula Perhitungan BMI
BMI = weight / ((height/100) ** 2)

print("Kategori BMI Anda: ")

if BMI < 15:
    print("Very severely underweight")
elif BMI >= 15 and BMI < 16:
    print("Severely underweight")
elif BMI >= 16 and BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal (healthy weight)")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 30 and BMI < 35:
    print("Moderately obese")
elif BMI >= 35 and BMI < 40:
    print("Severely obese")
else:
    print("Very severely obese")

print("Done")