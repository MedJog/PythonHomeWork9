# Есть семья: папа, мама, сын, дочь.
# Характеристики членов семьи: имя, возраст, рост, вес, статус.
# Вывести на экран характеристики каждого члена семьи.
# Подсчитать суммарный возраст или вес семьи.

class Family:
    def __init__(self, member, name, age, height, weight, status):
        self.member = member
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.status = status
    
    def information_1(self):
        return f'"Это {self.member}, его зовут {self.name}, ему {self.age} лет, он {self.status}, рост {self.height} см, вес {self.weight} кг.'

    def information_2(self):
        return f'"Это {self.member}, её зовут {self.name}, ей {self.age} лет, она {self.status}, рост {self.height} см, вес {self.weight} кг.'

    #def summa(object1, object2, object3, object4, atribut):  
    #    summa = getattr(object1, 'atribut') + getattr(object2, 'atribut') + getattr(object3, 'atribut') + getattr(object4, 'atribut')
    #    return summa
    
fother = Family('папа', 'Фёдор', 40, 175, 80, 'бизнесмен')
mother = Family('мама', 'Ирина', 35, 165, 55, 'дизайнер')
son = Family('сын', 'Иван', 18, 170, 70, 'студент')
daughter = Family('дочь', 'Елена', 10, 125, 30, 'школьница')

print(fother.information_1())
print(mother.information_2())
print(son.information_1())
print(daughter.information_2())

