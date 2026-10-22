class Pair[T, U]:
    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second

    def swap(self) -> str:
        return Pair(self.second, self.first)


p = Pair(42, "Hallo")
swapped = p.swap()  # mypy weiß: swapped.first ist str, swapped.second ist int
