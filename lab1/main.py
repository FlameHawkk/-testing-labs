def validate(raw, min_value, max_value):
    try:
        value = int(raw)
    except ValueError:
        return None
    if value < min_value or value > max_value:
        return None
    return value

def calculate_panels(M, N):
    # Крыша: N рядов, в ряду i — (2i−1) панелей, сумма = N²
    roof = N * N

    # Основание: M рядов, в каждом ряду (2N−1) панелей
    base = M * (2 * N - 1)

    return roof + base

def main():
    M = validate(input("Введите высоту основания M: "), 0, 10**9)
    if M is None:
        print("Ошибка ввода: M должно быть целым числом от 0 до 10^9. Запустите заново.")
        return

    N = validate(input("Введите высоту крыши N: "), 1, 10**9)
    if N is None:
        print("Ошибка ввода: N должно быть целым числом от 1 до 10^9. Запустите заново.")
        return

    print(f"Всего панелей: {calculate_panels(M, N)}")

if __name__ == "__main__":
    main()
