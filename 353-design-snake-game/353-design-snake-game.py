class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0,0)])
        self.width = width
        self.height = height
        self.food = deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        newHead = [self.snake[0][0] + self.direct[direction][0], self.snake[0][1] + self.direct[direction][1]]
        
        # notice that the newHead can be equal to self.snake[-1]
        if (newHead[0] < 0 or newHead[0] >= self.height or newHead[1] < 0 or newHead[1] >= self.width) or (newHead in self.snake and newHead != self.snake[-1]): return -1
        
        if self.food and self.food[0] == newHead:   # eat food
            self.snake.appendleft(newHead)  # just make the food be part of snake
            self.food.popleft()
        else:   # not eating food: append head and delete tail
            self.snake.appendleft(newHead)
            self.snake.pop()
        
        return len(self.snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)