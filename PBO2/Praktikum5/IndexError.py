list_angka = [1, 9, 0, 5, 1, 1, 0, 1, 1]
try:
    value = list_angka[11]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")
