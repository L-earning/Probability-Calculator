import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    #add the color (aka key in kwargs dictionary) as many times as the value is for that color
    for color in kwargs:
      number_balls = kwargs.get(color)
      for value in range(number_balls):
          self.contents.append(color)

  def draw(self, ball_amount):
    #create a list to store all the results for each draw
    drawn = []
    #if the amount of balls to be drawn is more than what is in he hat, return the hat's contents
    if len(self.contents) < ball_amount:
      return self.contents
    #once a ball is drawn randomly, remove it from the hat and put it into the list
    for i in range(ball_amount):
      drawn.append(random.choice(self.contents))
      self.contents.remove(drawn[i])
    return drawn
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
  drawn = []
  sucesses = 0
  experiments = num_experiments
  #for every experiment, make a copy of the hat to make sure that the 
  #contents of the hat is unchanged each experiment (each time a new ball is 
  #drawn it gets erased from the contents list, so it needs to be renewed 
  #for each experiment), but we want the same hat each time 
  while experiments:
    hat_copied = copy.deepcopy(hat)
    drawn.append(hat_copied.draw(num_balls_drawn))
    experiments -= 1 

  #go through the result of each experiment to check if the expected balls are in the draw
  for draw in drawn:
    was_expected = []
    #go through each of the expected balls and check if the color and the amount of that color is in the draw
    for expected in expected_balls:
      if draw.count(expected) >= expected_balls[expected]:
        was_expected.append(True)
      else:
        was_expected.append(False)

    has_expected = bool(was_expected.count(True) == len(was_expected))

    if has_expected:
      sucesses += 1

  #P(A) = N(A)/N(S)  -> probability of event is equal to the number of sucessful events divided by the number in the sample space
  probability = sucesses/num_experiments

  return probability
 
