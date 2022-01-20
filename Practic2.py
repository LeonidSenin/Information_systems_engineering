# Адаптер + Фасад 19.11.21 Практика №3
import time


class Taking_paper:  # Подсистема 1

    def take_paper(self):
        print("Taking new paper...")
        time.sleep(2)


class Scaning:  # Подсистема 2

    def scan(self):
        print("Scaning...")
        time.sleep(2)


class Printing:  # Подсистема 3

    def print_doc(self):
        print("Printing...")
        time.sleep(2)


class Printer: # Фасад

    def __init__(self):
        self.__take_paper = Taking_paper()
        self.__scaning = Scaning()
        self.__printing = Printing()

    def start_printing(self):
        print('Start working!')
        time.sleep(2)
        self.__take_paper.take_paper()
        self.__scaning.scan()
        self.__printing.print_doc()
        print('Stop working!')

# Американская вилка
class UsaFork:
    def power_usa(self):
        print('power on. Usa')

    def off_power_usa(self):
        print('power off. Usa')


# Европейская вилка
class EuroFork:
    def power_euro(self):
        print('power on. Euro')

    def off_power_euro(self):
        print('power off. Euro')


# Американская розетка
class UsaSocket:
    def __init__(self, fork):
        self.fork = fork

    def off_connect(self):
        self.fork.off_power_usa()

    def connect(self):
        self.fork.power_usa()
        Print_Machine = Printer()
        Print_Machine.start_printing()

# Адаптер Европейская вилка к американсокой розекте
class AdapterEuroInUsa:
    def __init__(self):
        self._euro_fork = EuroFork()

    def power_usa(self):
        self._euro_fork.power_euro()

    def off_power_usa(self):
        self._euro_fork.off_power_euro()


# uf = UsaFork()
# us = UsaSocket(uf)
# us.connect()
# us.off_connect()

# ef = EuroFork()
# us = UsaSocket(ef)
# us.connect()

# ad = AdapterEuroInUsa()
# us = UsaSocket(ad)
# us.connect()
# us.off_connect()
