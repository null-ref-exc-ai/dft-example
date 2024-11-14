from typing import Callable
import math


class ComplexAmplitude:
    """
    Комлпексная амплитуда
    """

    def __init__(self, freq: float, amplitude: float, phase: float, num: complex):
        """
        Коструктор:

        Параметры:
            freq - частота
            amplitude - амплитуда
            phase - фаза
            num - комплексное число, описывающее амлитуду
        """

        self.__freq: float = freq
        self.__amplitude: float = round(amplitude, 10) * 2
        self.__phase: float = round(phase, 10) if self.amplitude != 0 else 0
        self.__num: complex = num

    @property
    def freq(self) -> float:
        """
        Частота сигнала
        """

        return self.__freq

    @property
    def amplitude(self) -> float:
        """
        Амлитуда сигнала
        """

        return self.__amplitude


    @property
    def phase(self) -> float:
        """
        Фаза сигнала
        """

        return self.__phase


    @property
    def num(self) -> complex:
        """
        Комплексное число, описывающее амлитуду
        """

        return self.__num


class DFT:
    """
    Класс для выполнения ДПФ
    """

    def __init__(self, T: int, SF: int, F: Callable[[float], float]):
        """
        Коструктор

        Параметры:
            T - время измерений
            SF - частота дискртизации
            F - входная функция
        """

        self.T: int = T
        self.N: int = T * SF
        self.SF: int = SF

        self.input: list[float] = [F(i * self.T / self.N) for i in range(self.N)]

    def calculate(self) -> list[ComplexAmplitude]:
        """
        Запускает расчет ДПФ
        """

        freqs: list[float] = self.__freqs()
        result: list[ComplexAmplitude] = list()

        for i, k in enumerate(range(self.N)):
            xk: complex = self.__xk(k)

            module = (1 / self.N) * math.sqrt(pow(xk.real, 2) + pow(xk.imag, 2))
            argument = math.atan2(xk.imag, xk.real)

            result.append(ComplexAmplitude(freqs[i], module, argument, xk))

        return result

    def __xk(self, k: int) -> complex:
        """
        Просчитывает значение для определенного индекса частоты

        Параметры:
            k - индекс частоты

        Возвращаемое значение: результат вычисления для переденного k
        """

        return sum([self.input[i] * pow(math.e, (-(1j * 2 * math.pi) / self.N * k * i)) for i in range(0, self.N)])

    def __freqs(self) -> list[float]:
        """
        Подсчитывает частоты сигалов
        """

        f: list[float] = list[float]()

        if self.N % 2 == 0:
            for i in range(int(self.N / 2 - 1 + 1)):
                f.append(i / ((1 / self.SF) * self.N))

            for i in range(int(-self.N / 2), -1 + 1):
                f.append(i / ((1 / self.SF) * self.N))
        else:
            for i in range(int((self.N - 1) / 2 + 1)):
                f.append(i / ((1 / self.SF) * self.N))

            for i in range(int(-(self.N - 1) / 2), -1 + 1):
                f.append(i / ((1 / self.SF) * self.N))

        return f


class InverseDFT:
    """
    Класс для выполнения обратного ДПФ.
    """


    def __init__(self, T: int, amplitudes: list[ComplexAmplitude]):
        """
        Коструктор

        Параметры:
            T - время измерения сигнала
            amplitudes - комлпексные амплитуды исходного сигнала
        """
        self.T: int = T
        self.N: int = len(amplitudes)
        self.amplitudes: list[ComplexAmplitude] = amplitudes


    def calculate(self) -> dict[float, float]:
        """
        Запускает расчет обратного ДПФ
        """

        result: dict[float, float] = dict()

        times: list[float] = [i * self.T / self.N for i in range(self.N)]

        for i in range(self.N):
            result.update({times[i]: self.__xn(i).real})

        return result


    def __xn(self, n: int) -> complex:
        """
        Просчитывает значение сигнала в n-ой точке

        Параметры:
            n - номер точки

        Возвращаемое значение: результат вычисления для переденного n
        """

        return (1 / self.N) * sum([self.amplitudes[i].num * pow(math.e, ((2 * math.pi * 1j) / self.N) * n * i)
                                   for i in range(0, self.N)])
