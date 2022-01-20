# Фабричный метод 17.12.21 Практика 4
from abc import abstractmethod


class Shape(object):
    @abstractmethod
    def amount_of_paint(self):
        pass


class Newspaper(Shape):
    def __init__(self, kol_vo, z):
        self.kol_vo = kol_vo
        self.z = z

    def amount_of_paint(self):
        nakat_news_paper = 1.25  # накат краски
        news_paper_height = 210
        news_paper_width = 297
        s = (news_paper_height * news_paper_width / 1000000) * self.kol_vo
        r_pt_news_paper = s * nakat_news_paper * self.z / 100
        return f'{round(r_pt_news_paper / 1000, 3)}'

    def __str__(self):
        return 'Newspaper'


class Magazine(Newspaper, Shape):

    def __init__(self, kol_vo, z):
        super().__init__(kol_vo, z)  # self.kol_vo = kol_vo # self.z = z

    def amount_of_paint(self):
        nakat_magazine = 1.5  # накат краски
        magazine_height = 145
        magazine_width = 215
        s = (magazine_height * magazine_width / 1000000) * self.kol_vo
        r_pt_magazine = s * nakat_magazine * self.z / 100
        return f'{round(r_pt_magazine / 1000, 3)}'

    def __str__(self):
        return 'Magazine'


class Factory:
    def create_shape(self, name):
        if name == 'newspaper':
            kol_vo = int(input("Введите тираж: "))
            z = int(input("Введите процент заполнения страницы: "))
            return Newspaper(kol_vo, z)

        elif name == 'magazine':
            kol_vo = int(input("Введите тираж: "))
            z = int(input("Введите процент заполнения страницы: "))
            return Magazine(kol_vo, z)


factory = Factory()
shape_name = input("Введите что будем печатать (newspaper/magazine): ")

shape = factory.create_shape(shape_name)

print(f"Тип созданного объекта: {shape.__str__()}")
print(f"Тип объекта {shape_name} на него ушло краски {shape.amount_of_paint()} кг")

# Расчет краски ---------------------------------------------------------------------------------------------

# 1) Рассчитываем площадь печати S (площадь А3 297х420мм=0,125м2, если конечно площадь запечатки А3)
#
# 2) Рассчитываем общую площадь запечатки в м2 - Sобщ. = S * Тираж (Sобщ=12500m2)
#
# 3) Рассчитываем расход краски -
# Rpt=Soбщ*K*Z%, где
# Soбщ - общая площадь запечатки
# K - накат краски (в среднем 1,25 г/м2)
# Z% - площадь запечатки
#
# Итого: Rpt = 12500m2 * 1,25g/m2 * 0,15 = 2345g = 2,5kg
