def check_delimiters(expression: str) -> str:
    """
    Перевіряє симетричність дужок у виразі.

    Args:
        expression (str): Рядок з виразом.

    Returns:
        str: "Симетрично" або "Несиметрично".
    """
    stack = []
    opening_delimiters = "({["
    closing_delimiters = ")}]"
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if mapping[char] != top:
                return "Несиметрично"

    if stack:
        return "Несиметрично"

    return "Симетрично"


def main():
    test_cases = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

    for expression in test_cases:
        result = check_delimiters(expression)
        print(f"{expression}: {result}")


if __name__ == "__main__":
    main()
