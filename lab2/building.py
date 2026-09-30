"""
Класс Building — расчёт количества панелей для здания.
Крыша: N рядов, треугольник, всего N² панелей.
Основание: M рядов, ширина 2N−1, всего M*(2N−1) панелей.
"""

class Building:
    def __init__(self, M, N):
        """
        M — высота основания (0 ≤ M ≤ 10⁹)
        N — высота крыши      (1 ≤ N ≤ 10⁹)
        """
        if isinstance(M, bool) or not isinstance(M, int):
            raise TypeError("M должно быть целым числом")
        if isinstance(N, bool) or not isinstance(N, int):
            raise TypeError("N должно быть целым числом")
        if M < 0 or M > 10**9:
            raise ValueError("M должно быть в диапазоне от 0 до 10^9")
        if N < 1 or N > 10**9:
            raise ValueError("N должно быть в диапазоне от 1 до 10^9")
        self.M = M
        self.N = N

    @property
    def roof_panels(self):
        """Крыша: N рядов, сумма 1+3+…+(2N−1) = N²."""
        return self.N * self.N

    @property
    def base_panels(self):
        """Основание: M рядов по (2N−1) панелей."""
        return self.M * (2 * self.N - 1)

    @property
    def total_panels(self):
        """Всего панелей."""
        return self.roof_panels + self.base_panels
