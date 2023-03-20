class Celcius :
    def suhu(x):
        rea = x * 4/5
        fah = (x * 9/5)+32
        kel = x + 273
        print("suhu dalam reamur: ", rea)
        print("suhu dalam fahrenheit: ", fah)
        print("suhu dalam kelvin: ", kel)

    a = int(input("Masukan suhu dalam celcius: "))
    suhu (a)  