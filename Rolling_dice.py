#creating the die class
from random import randint


class Die:
    """a class to represent a single die """

    def __init__(self, num_sides = 6):
        """assume a six-sided shape(die) """
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)


#rolling the die

#creating a D6
die = Die()

#toss,roll a bit and store the results in a list[roll the die 100 times]
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print (results)
#Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
            frequency = results.count(value)
            frequencies.append(frequency)
print (frequencies)


#visualize the results
from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}
my_layout  = Layout(title = "Results of rolling one D6 dice 100 times", xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename = "d6.html")
