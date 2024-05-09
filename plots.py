import matplotlib.pyplot as plt


# Generate some data
x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]
basic = [14700, 14576, 14720, 15392, 16332, 17232, 20852, 25308, 31352, 39068, 57884, 81792, 109876, 147020, 173024]
efficient = [14908, 14976, 15028, 15264, 16072, 16848, 19052, 21840, 24580, 27672, 37800, 49004, 65100, 81804, 98412]

# Create a figure and axis objects
fig, ax = plt.subplots()

# Plot the first curve
ax.plot(x, basic, label='sin(x)', color='blue')

# Plot the second curve
ax.plot(x, efficient, label='cos(x)', color='orange')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Multiple Plots')

# Add a legend
ax.legend()

# Show the plot
plt.show()




