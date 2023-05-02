print ("Faldi 190511011") 
print("Menghitung Luas dan Volume tabung")

r = int (input("jari jari ="))
la = int (input("luas alas ="))
t = int (input("tinggi ="))
ka = int (input("keliling alas ="))

phi = 22/7

Luas = (2*la) + (ka*t)
Volume = phi*r*r*t

print ("Luas tabung =", Luas)
print ("Volume tabung =", Volume)