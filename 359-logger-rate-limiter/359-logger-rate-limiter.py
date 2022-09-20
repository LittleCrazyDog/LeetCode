class Logger:

    def __init__(self):
        self.ok = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.ok[message] <= timestamp:
            self.ok[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)