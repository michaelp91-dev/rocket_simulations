import numpy as np

# Rocket properties
mass = 1.0  # kg
thrust = 10.0  # N
burn_time = 2.0  # s
drag_coefficient = 0.5
surface_area = 0.1  # m^2

# Environmental conditions
air_density = 1.225  # kg/m^3
gravity = 9.81  # m/s^2

# Time steps
time_steps = 100
time = np.linspace(0, 5, time_steps)

# Initialize variables
position = np.zeros(time_steps)
velocity = np.zeros(time_steps)
acceleration = np.zeros(time_steps)

# Simulation loop
for i in range(time_steps - 1):
    # Calculate thrust force
    if time[i] < burn_time:
        thrust_force = thrust
    else:
        thrust_force = 0

    # Calculate drag force
    drag_force = 0.5 * air_density * velocity[i]**2 * drag_coefficient * surface_area

    # Calculate net force
    net_force = thrust_force - drag_force - mass * gravity

    # Calculate acceleration
    acceleration[i + 1] = net_force / mass

    # Update velocity and position
    velocity[i + 1] = velocity[i] + acceleration[i + 1] * (time[i + 1] - time[i])
    position[i + 1] = position[i] + velocity[i + 1] * (time[i + 1] - time[i])

# Plot the results
import matplotlib.pyplot as plt
plt.plot(time, position)
plt.xlabel("Time (s)")
plt
