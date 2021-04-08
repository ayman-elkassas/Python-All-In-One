import matplotlib.pyplot as plt

# x_values=list(range(1,1000))
# squares=[x**2 for x in x_values]
# # s is size of each point
# # scatter like plot but with more arg
# plt.scatter(x_values,squares,s=10)
# plt.show()

x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.scatter(x_values, squares, c=squares,cmap=plt.cm.Blues, edgecolor='none',s=10)

plt.title("Square Numbers", fontsize=24)

plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)
plt.tick_params(axis='both', which='major',labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()


