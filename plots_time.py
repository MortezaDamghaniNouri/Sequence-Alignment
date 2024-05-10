import matplotlib.pyplot as plt


# Generate some data
x = [16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]
basic = [1.00040, 1.00255, 1.99366, 6.93130, 14.99963, 28.00941, 67.99817, 124.99976, 198.00115, 278.00703, 519.00673, 818.00675, 1131.99949, 1598.00768, 1996.99235]
efficient = [1.00732, 1.99962, 8.00109, 23.99898, 40.99917, 80.00684, 175.99988, 311.99884, 488.99889, 699.99838, 1252.00081, 1975.01040, 2798.00677, 3936.99574, 4737.00094]

# Create a figure and axis objects
fig, ax = plt.subplots()

# Plot the first curve
ax.plot(x, basic, label='Basic Version', color='blue')

# Plot the second curve
ax.plot(x, efficient, label='Memory Efficient Version', color='orange')

# Add labels and title
ax.set_xlabel('Problem Size (M+N)')
ax.set_ylabel('Time (MS)')
ax.set_title('Time')

# Add a legend
ax.legend()

# Show the plot
plt.show()




