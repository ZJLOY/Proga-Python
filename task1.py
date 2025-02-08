class Tyre:
    def __init__(self, width: int, height: int, diameter: int):
        """
        Создание и подготовка к работе объекта "Шина"

        :param width: Ширина шины
        :param height: Высота профиля
        :param diameter: Диаметр диска (в дюймах)

        Примеры:
        >>> tyre = Tyre(205, 55, 16)
        """
        if not all(isinstance(x, int) and x > 0 for x in [width, height, diameter]):
            raise ValueError("Ширина, высота и диаметр должны быть целыми положительными числами")

        self.width = width
        self.height = height
        self.diameter = diameter

    def __str__(self):
        return f'Шина {self.width}/{self.height} R{self.diameter}'

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height}, diameter={self.diameter})'

    def current_pressure(self) -> float:
        """Метод, который проверяет давление в колесе"""
        ...

    def repair_tyre(self) -> None:
        """Метод, который ремонтирует шину"""
        ...


class WinterTyre(Tyre):
    def __init__(self, width: int, height: int, diameter: int, studded: bool):
        """
        Создание и подготовка к работе объекта "Зимняя шина"

        :param width: Ширина шины
        :param height: Высота профиля
        :param diameter: Диаметр диска (в дюймах)
        :param studded: Шипованное ли колесо

        Примеры:
        >>> tyre = WinterTyre(205, 55, 16, True)
        """
        super().__init__(width, height, diameter)

        if not isinstance(studded, bool):
            raise TypeError("studded должен быть логическим значением (True/False)")

        self.studded = studded

    def __str__(self):
        return f'Зимняя шина {self.width}/{self.height} R{self.diameter} {"(шипованная)" if self.studded else "(не шипованная)"}'

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height}, diameter={self.diameter}, studded={self.studded})'

    def repair_tyre(self) -> None:
        """Метод ремонта шины, если шина шипованная — выполняется дошиповка"""
        ...


if __name__ == "__main__":
    pass
