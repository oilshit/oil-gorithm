import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(7.5, 7.5)
fig.suptitle("In-situ stress on Example 2.1 (Question 1)")
ax = fig.add_subplot(projection='3d')

# STRIKE-SLIP STRESS STATE
# vertical stress
sigma_v = 1.92 * -1 # acuan stress vertical ke bawah
                    ## karena batuan mengalami kompaksi

# horizontal stress
sigma_h_min = 1.75
sigma_h_max = 1.77

# add scatter (dot) plot into every single sigma
## to get the geological stress state
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, 0, color="r", linewidths=1)
ax.quiver(sigma_h_min, sigma_h_max, 0, 0, 0, sigma_v, color="r", linewidths=1)

ax.scatter(sigma_h_min, sigma_h_max, sigma_v, label="Normal Fault", color="b")
ax.quiver(0, 0, 0, sigma_h_min, sigma_h_max, sigma_v, color="b", linewidths=1)

ax.set_xlabel('Minimum Horizontal Stress (SG)')
ax.set_ylabel('Maximum Horizontal Stress (SG)')
ax.set_zlabel('Overburden Stress (SG)')

ax.legend()

plt.show()