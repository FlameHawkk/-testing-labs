"""
Класс Factorial — расчёт факториала неотрицательного целого числа.
"""

class Factorial:
    def __init__(self, n):
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("n должно быть целым числом")
        if n < 0:
            raise ValueError("n не может быть отрицательным")
        self.n = n

    def compute(self):
        result = 1
        for i in range(2, self.n + 1):
            result *= i
        return result

    def compute_recursive(self):
        """
        Альтернативная рекурсивная реализация — для сравнения.
        """
        if self.n <= 1:
            return 1
        return self.n * Factorial(self.n - 1).compute_recursive()
