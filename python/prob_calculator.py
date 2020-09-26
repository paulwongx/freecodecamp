import copy
import random

class Hat:
    def __init__(self, **colors):
        self.balls = {}
        self.contents = []
        for c,v in colors.items():
            self.balls[c] = v
            for i in range(v):
                self.contents.append(c)
        # print(self.contents)
        # print(self.balls)

    def draw(self, num_to_draw):
        drawn_balls = []
        if num_to_draw > len(self.contents):
            return self.contents
        else:
            for i in range(num_to_draw):
                rand_idx = random.randint(0,len(self.contents)-1)
                drawn_balls.append(self.contents.pop(rand_idx))
            return drawn_balls
            print(self.contents)
            print(drawn_balls)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    num_correct = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        isCorrect = True
        for c,v in expected_balls.items():
            if drawn_balls.count(c) >= v:
                isCorrect = isCorrect and True
            else:
                isCorrect = isCorrect and False
        if isCorrect == True:
            num_correct += 1

    probability = num_correct / num_experiments
    print(probability)
    return probability



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)