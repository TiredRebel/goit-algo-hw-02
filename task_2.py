from collections import deque


def is_palindrome(input_string: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом, використовуючи двосторонню чергу (deque).
    Ігнорує регістр та пробіли.

    Args:
        input_string (str): Вхідний рядок для перевірки.

    Returns:
        bool: True, якщо рядок є паліндромом, False інакше.
    """
    # Приведення до нижнього регістру та видалення пробілів
    processed_string = input_string.lower().replace(" ", "")

    # Створення двосторонньої черги
    char_deque = deque(processed_string)

    # Порівняння символів з обох кінців
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()

        if left_char != right_char:
            return False

    return True


def main():
    test_strings = [
        "A man a plan a canal Panama",
        "No lemon no melon",
        "Hello World",
        "Madam",
        "Step on no pets",
        "12321",
        "12345",
    ]

    print("Перевірка на паліндром:")
    for s in test_strings:
        result = is_palindrome(s)
        status = "✅ Паліндром" if result else "❌ Не паліндром"
        print(f"'{s}': {status}")


if __name__ == "__main__":
    main()
