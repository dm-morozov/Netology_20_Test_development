def summarize(x: int, y: int) -> int:
    if x == -5:
        return 0
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_info() -> dict:
    return {
        'first_name': 'Timur',
        'last_name': 'Anvartdinov',
        'age': 37,
        'max_age': 40,
    }