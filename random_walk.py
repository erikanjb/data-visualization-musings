##a random walk is a path that has no clear direction but is determined by a series pof random decisions.
from random import choice
import matplotlib.pyplot as plt

#create the randomwalk class

class Randomwalk:
    """A class to generate random walks."""

    def __init__(self, num_points = 5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]
     #choosing directions
    def fill_walk(self):
        """calculate all the points in the walk"""

        # keep taking steps until the walks reaches the desired length.
        while len(self.x_values) < self.num_points:

            #Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_direction

            y_direction = choice([1, -1])
            y_distance  = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



#plotting the random walk
iw = Randomwalk()
iw.fill_walk()

#plot setup
plt.style.use("classic")
fig, ax = plt.subplots()
#use the scatter method
ax.scatter(iw.x_values, iw.y_values, s=15)
plt.show()

            
