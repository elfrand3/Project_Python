class summation:
    def sum(self, a, b):
        c = a + b
        print('hasil penjumlahan = ', c)

class minustion:
    def min(self, a, b):
        c = a - b
        print('hasil pengurangan = ', c)

class multiplication:
    def multi(self, a, b):
        c = a * b
        print('hasil perkalian = ', c)

class calculator(summation, minustion, multiplication):
    def devide(self, a, b):
        c = a / b
        print('hasil pembagian = ',int(c))

calc = calculator()
calc.sum(5, 5)
calc.min(23, 3)
calc.multi(6, 5)
calc.devide(80, 2)

