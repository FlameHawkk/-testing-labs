from main import validate, calculate_panels

print("=== Тест формулы ===")
FORMULA_CASES = [
    (6, 6, 102),
    (3, 3, 24),
    (0, 5, 25),
    (5, 1, 6),
    (1, 1, 2),
    (0, 1, 1),
    (12, 4, 100),
    (10**9, 10**9, 10**18 + 10**9 * (2 * 10**9 - 1)),
]
for M, N, exp in FORMULA_CASES:
    got = calculate_panels(M, N)
    print(f"calculate_panels({M}, {N}) = {got}", "OK" if got == exp else f"FAIL (нужно {exp})")

print()
print("=== Тест валидации ===")
VALIDATE_CASES = [
    ("0", 0, 10**9, 0),
    ("abc", 0, 10**9, None),
    ("5.5", 0, 10**9, None),
    ("", 0, 10**9, None),
    ("-1", 0, 10**9, None),
    ("1000000001", 0, 10**9, None),
    ("6", 1, 10**9, 6),
    ("0", 1, 10**9, None),
    ("-3", 1, 10**9, None),
    ("1000000001", 1, 10**9, None),
]
for raw, lo, hi, exp in VALIDATE_CASES:
    got = validate(raw, lo, hi)
    print(f"validate({raw!r}, {lo}, {hi}) = {got}", "OK" if got == exp else f"FAIL (нужно {exp})")