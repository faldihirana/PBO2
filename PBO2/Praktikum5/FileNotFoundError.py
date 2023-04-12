try:
    with open("kodeNuklir.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File yang diminta gatau kemana!")
