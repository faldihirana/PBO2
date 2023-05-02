Tinggi = int(input("Masukkan tinggi badan cm: "))
Berat = int(input("Masukkan berat badan kg: "))

BMI = Berat / (Tinggi/100)**2

print(f"BMI anda adalah {BMI}")

if BMI <= 18.4:
    print("Kurus.")
elif BMI <= 24.9:
    print("Normal.")
elif BMI <= 29.9:
    print("sedikit berlebih.")
elif BMI <= 34.9:
    print("sangat berlebih.")
elif BMI <= 39.9:
    print("obesitas.")
else:
    print("You are severely obese.")