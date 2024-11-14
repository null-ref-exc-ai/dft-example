import DFT
import Graphics
import math

# Частота дискертизации
SF = 150
# Время измерения сигнала
T = 3
# Исходная функция
F = lambda x: 1.5 * math.cos(math.pi * 2 * 5 * x + 0.5) + 2 * math.cos(math.pi * 2 * 10 * x + 1)

dft: DFT.DFT = DFT.DFT(T, SF, F)

complex_amplitudes: list[DFT.ComplexAmplitude] = dft.calculate()
amplitudes, phases = {}, {}
for ca in complex_amplitudes:
    if ca.freq >= 0:
        amplitudes.update({ca.freq: ca.amplitude})
        phases.update({ca.freq: ca.phase})

Graphics.show_dict_on_graphic("Amplitudes", "Frequency", "Amplitude", amplitudes, False, False)
Graphics.show_dict_on_graphic("Phases", "Frequency", "Phase", phases, False, False)

idft: DFT.InverseDFT = DFT.InverseDFT(T, complex_amplitudes)
signal: dict[float, float] = idft.calculate()

Graphics.show_dict_on_graphic("Source signal", "Time", "Value", signal, True, True)