class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

class Phone:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
ram = RAM(4)
storage = Storage(64)
phone = Phone(ram, storage)
print(phone.ram.capacity) 
print(phone.storage.capacity)