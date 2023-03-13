class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(100, 90)) # Output: 190
print(Kalkulator.subtract(60, 9)) # Output: 51

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(5, 2)) # Output: 10
print(Kalkulator.divide(12, 6)) # Output: 2
# 190 51 10 11