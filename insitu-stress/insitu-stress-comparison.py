import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

fig = plt.figure()
fig.set_size_inches(7.5, 7.5)
fig.suptitle("In-situ stress on Example 2.1 (Question 3)\nWith seawater specific gravity.")
ax = fig.add_subplot(projection='3d')

# STRIKE-SLIP STRESS STATE
# horizontal stress
seawater_sg = 1.03

sigma_v = 1.81 * -1 # acuan stress vertical ke bawah
                    ## karena batuan mengalami kompaksi

sigma_h_min = 1.64
sigma_h_max = 1.92

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, sigma_h_max, sigma_v, sigma_h_min, 0, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, 0, sigma_v, 0, sigma_h_max, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Strike-slip Fault", color=mcolors.CSS4_COLORS["dodgerblue"])
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color=mcolors.CSS4_COLORS["dodgerblue"], linewidths=2)

# NORMAL STRESS STATE
# seawater specific gravity
seawater_sg = 1.03

# vertical stress
sigma_v = 1.92 * -1 # acuan stress vertical ke bawah
                                    ## karena batuan mengalami kompaksi

sigma_h_min = 1.75
sigma_h_max = 1.77

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, sigma_h_max, sigma_v, sigma_h_min, 0, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, 0, sigma_v, 0, sigma_h_max, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Normal Fault", color=mcolors.CSS4_COLORS["green"])
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color=mcolors.CSS4_COLORS["green"], linewidths=2)

# EFFECTIVE STRIKE-SLIP STRESS STATE
# horizontal stress
seawater_sg = 1.03

sigma_v = (1.81 - seawater_sg) * -1 # acuan stress vertical ke bawah
                    ## karena batuan mengalami kompaksi

sigma_h_min = 1.64 - seawater_sg
sigma_h_max = 1.92 - seawater_sg

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, sigma_h_max, sigma_v, sigma_h_min, 0, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, 0, sigma_v, 0, sigma_h_max, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Strike-slip Fault (effective stress)", color=mcolors.CSS4_COLORS["cyan"])
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color=mcolors.CSS4_COLORS["cyan"], linewidths=2)

# EFFECTIVE NORMAL STRESS STATE
# seawater specific gravity
seawater_sg = 1.03

# vertical stress
sigma_v = (1.92 - seawater_sg) * -1 # acuan stress vertical ke bawah
                                    ## karena batuan mengalami kompaksi

sigma_h_min = 1.75 - seawater_sg
sigma_h_max = 1.77 - seawater_sg

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, sigma_h_max, sigma_v, sigma_h_min, 0, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, 0, sigma_v, 0, sigma_h_max, 0, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color=mcolors.CSS4_COLORS["maroon"], linewidths=2, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Normal Fault (effective stress)", color=mcolors.CSS4_COLORS["lightgreen"])
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color=mcolors.CSS4_COLORS["lightgreen"], linewidths=2)

ax.set_xlabel('Minimum Horizontal Stress (SG)')
ax.set_ylabel('Maximum Horizontal Stress (SG)')
ax.set_zlabel('Overburden Stress (SG)')

ax.legend()

plt.show()