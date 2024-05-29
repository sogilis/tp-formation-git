def sing() -> list[str]:
    return first_verse() + second_verse()

def first_verse() -> list[str]:
    return [
            "When I find myself in times of trouble, Mother Mary comes to me",
            "Speaking words of wisdom, let it be",
            "And in my hour of darkness she is standing right in front of me",
            "Speaking words of wisdom, let it be",
        ]

def second_verse() -> list[str]:
    raise Exception("Hurry up :(")
