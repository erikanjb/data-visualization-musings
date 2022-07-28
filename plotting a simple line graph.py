
import matplotlib.pyplot as plt
import_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
fig, ax = plt.subplots()

#set linewidth/thickness
ax.plot(squares, linewidth=3)

#set the title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("square of values", fontsize = 14)

#set size of thick labels.
ax.tick_params(axis= "both", labelsize = 14)
plt.show()
