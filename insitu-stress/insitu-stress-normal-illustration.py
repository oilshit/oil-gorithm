import matplotlib.pyplot as plt
import numpy as np

# Create axis
axes = [1, 1, 1]
 
# Create Data
data = np.ones(axes, dtype=bool)

# Control Transparency
alpha = 0.5
 
# Control colour
colors = np.empty(axes + [4], dtype=np.float32)
 
colors[:] = [1, 0, 0, alpha]  # red

fig = plt.figure()
fig.set_size_inches(7.5, 7.5)
fig.suptitle("In-situ stress on Example 2.1 (Question 1)\nIllustration")
ax = fig.add_subplot(projection='3d')

# Voxels is used to customizations of the
# sizes, positions and colors.
ax.voxels(data, facecolors=colors)

# NORMAL STRESS STATE
# vertical stress
sigma_v = 1.92 * -1 - axes[2] # acuan stress vertical ke bawah
                              ## karena batuan mengalami kompaksi

# horizontal stress
sigma_h_min = 1.75 + axes[0]
sigma_h_max = 1.75 + axes[1]

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(sigma_h_min, axes[1] / 2, axes[2] / 2, (sigma_h_min - axes[0])* -1, 0, 0, color="r", linewidths=3, label="sigma_h (1.75 SG)")
ax.quiver(axes[0] / 2, sigma_h_max, axes[2] / 2, 0, (sigma_h_max - axes[1])* -1, 0, color="g", linewidths=3, label="sigma_H (1.77 SG)")
ax.quiver(axes[0] / 2, axes[1] / 2, sigma_v * -1, 0, 0, (sigma_v + axes[2]), color="b", linewidths=3, label="sigma_V (1.92 SG)")

ax.set_xlabel('Minimum Horizontal Stress (SG)')
ax.set_ylabel('Maximum Horizontal Stress (SG)')
ax.set_zlabel('Overburden Stress (SG)')

ax.legend()

plt.show()