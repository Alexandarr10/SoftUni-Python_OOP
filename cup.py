class Cup:
    def __init__(self, size: int, quantity_liquid: int):
        self.size = size
        self.quantity_liquid = quantity_liquid

    def fill(self, quantity:int):
        if self.quantity_liquid + quantity <= self.size:
            self.quantity_liquid += quantity


    def status(self):
        return self.size - self.quantity_liquid

# Test code
cup = Cup(100, 50)

print(cup.status())

cup.fill(40)

cup.fill(20)

print(cup.status())