class Power:
    def __init__(self, n):
        self.num = n

    def add_to_num(self, num):
        self.num = self.num + num

    @staticmethod
    def add(a1, b):
        return a1 + b


a = Power(5)
print(a.num)

a.add_to_num(6)
print(a.num)

# we can call a static method by using class name or instance variable
sum1 = Power.add(2, 8)
print(a.add(12, 55))
