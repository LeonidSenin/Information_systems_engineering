# Фасад+Иттератор 19.11.21 Практика №3
import time


class Taking_paper:  # Подсистема 1

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.number):
            raise StopIteration
        numbers = self.number[self.index]
        self.index += 1
        return numbers

    def take_paper(self):
        print(f"Taking paper ...")
        time.sleep(2)


class Scaning:  # Подсистема 2

    def scan(self):
        print("Scaning...")
        time.sleep(2)


class Printing:  # Подсистема 3

    def print_doc(self):
        print("Printing...")
        time.sleep(2)


class Printer:  # Фасад

    def __init__(self):
        self.__take_paper = Taking_paper(a)
        self.__scaning = Scaning()
        self.__printing = Printing()

    def start_printing(self):
        print('Start working!')
        time.sleep(2)
        self.__take_paper.take_paper()
        self.__scaning.scan()
        self.__printing.print_doc()
        print('Stop working!')


print('Сколько всего листов в документе?')
a1 = int(input())
print('Номера страниц которые надо распечать:')
a = list(map(int, input().split()))
document = Taking_paper(a)
for i in document:
    if a1 > i:
        print(f'Preparing page {i} for printing')
        Print_Machine = Printer()
        Print_Machine.start_printing()
        print()
    else:
        print(f'This pages {i} are not in this document')
        print()
        continue
