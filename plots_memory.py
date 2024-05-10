import matplotlib.pyplot as plt


# Generate some data
x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]
basic = [14692, 14712, 14720, 15392, 16332, 17232, 20852, 25308, 31352, 39068, 57884, 81792, 109876, 147020, 173024]
efficient = [15176, 15196, 15352, 15260, 15308, 15336, 15384, 15396, 15444, 15616, 15720, 15856, 16076, 16212, 16260]

# Create a figure and axis objects
fig, ax = plt.subplots()

# Plot the first curve
ax.plot(x, basic, label='Basic Version', color='blue')

# Plot the second curve
ax.plot(x, efficient, label='Memory Efficient Version', color='orange')

# Add labels and title
ax.set_xlabel('Problem Size (M+N)')
ax.set_ylabel('Memory (KB)')
ax.set_title('Memory Usage')

# Add a legend
ax.legend()

# Show the plot
plt.show()




