import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(7.5, 7.5)
fig.suptitle("In-situ stress on Example 2.1 (Question 3)\nWith seawater specific gravity.")
ax = fig.add_subplot(projection='3d')

# STRIKE-SLIP STRESS STATE
# seawater specific gravity
seawater_sg = 1.03

# vertical stress
sigma_v = (1.81 - seawater_sg) * -1 # acuan stress vertical ke bawah
                    ## karena batuan mengalami kompaksi

# horizontal stress
sigma_h_min = 1.64 - seawater_sg
sigma_h_max = 1.92 - seawater_sg

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, 0, color="r", linewidths=1, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color="r", linewidths=1, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Strike-slip Fault", color="b")
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color="b", linewidths=1)

# NORMAL STRESS STATE
# seawater specific gravity
seawater_sg = 1.03

# vertical stress
sigma_v = (1.92 - seawater_sg) * -1 # acuan stress vertical ke bawah
                    ## karena batuan mengalami kompaksi

# horizontal stress
sigma_h_min = 1.75 - seawater_sg
sigma_h_max = 1.77 - seawater_sg

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, 0, color="r", linewidths=1, linestyle="dashed")
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color="r", linewidths=1, linestyle="dashed")

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Normal Fault", color="g")
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color="g", linewidths=1)

ax.set_xlabel('Minimum Horizontal Stress (SG)')
ax.set_ylabel('Maximum Horizontal Stress (SG)')
ax.set_zlabel('Overburden Stress (SG)')

ax.legend()

plt.show()