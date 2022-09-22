class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.avaliable = set(range(maxNumbers))

    def get(self) -> int:
        return self.avaliable.pop() if self.avaliable else -1

    def check(self, number: int) -> bool:
        return number in self.avaliable

    def release(self, number: int) -> None:
        self.avaliable.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)