# Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие | ООП Python
# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=


def dec_func(self, func):
    def wrapper(other):
        sc = self.__verify_data(other)
        return func(sc)

    return wrapper


class Clock:
    __DAY = 86400  # число секунд в одном дне
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY
    def get_time(self):
        s = self.seconds % 60  # секунды
        m = (self.seconds // 60) % 60  # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")
    def dec_func(func):
        def wrapper(self, other):
            sc = self.__verify_data(other)
            return func(self,sc)

        return wrapper
    @classmethod
    def __verify_data(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Секунды должны быть целым числом")

        return other if isinstance(other, int) else other.seconds
    @dec_func
    def __eq__(self, sc):
        return sc == self.seconds
    @dec_func
    def __gt__(self, sc):
        return self.seconds > sc
    @dec_func
    def __lt__(self, sc):
        return self.seconds < sc
    @dec_func
    def __ge__(self, sc):
        return self.seconds >= sc
    @dec_func
    def __le__(self, sc):
        return self.seconds <= sc
    @dec_func
    def __add__(self, sc):
        return Clock(self.seconds + sc)
    @dec_func
    def __radd__(self, sc):
        return self + sc
    @dec_func
    def __iadd__(self, sc):
        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
print(10000 < c1)
