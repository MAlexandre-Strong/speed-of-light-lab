# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:06:20 2024

@author: maxin
"""

import numpy as np
import csv

# Function to calculate velocity
def calculate_velocity(d1, d2, t1, t2):
    return (d1-d2) / (t1-t2)

trials = [
    [4, 6],
    [6,13],
    [8,20],
    [10,26],
    [12,32]
]


# Increment distance by 1 cm up from -10 cm to 10 cm
avg_velocity_dist=[]
for increment_distance in range(-10, 11):
    new_distance = increment_distance / 10
    velocities = []
    for i in range(len(trials)):
        for j in range(i + 1, len(trials)):
            d1 = trials[i][0] + new_distance
            d2 = trials[j][0] + new_distance
            t1 = trials[i][1] * 10 ** -9
            t2 = trials[j][1] * 10 ** -9
            velocity = calculate_velocity(d1, d2, t1, t2)
            velocities.append(velocity)
    avg_velocity_dist.append([increment_distance, np.mean(velocities)])
    print(f"Distance increment: {increment_distance} cm, average velocity: {np.mean(velocities)}")
#print(avg_velocity_dist)
print()
# Increment time by 1 nm up from -10 nm to 10 nm
avg_velocity_time=[]
for increment_time in range(-10, 11):
    new_time = increment_time*10**-9
    velocities_t = []
    for i in range(len(trials)):
        for j in range(i+1, len(trials)):
            d1=trials[i][0]
            d2=trials[j][0]
            t1=trials[i][1]*10**-9+new_time
            t2=trials[j][1]*10**-9+new_time
            velocity = calculate_velocity(d1, d2, t1, t2)
            velocities_t.append(velocity)
    avg_velocity_time.append([increment_time, np.mean(velocities_t)])
    print(f"Time increment: {increment_time} ns, average velocity: {np.mean(velocities_t)}")
#print(avg_velocity_time)
  
#np.savetxt("avg_velocity_dist.csv", avg_velocity_dist, delimiter=",")      
#np.savetxt("avg_velocity_time.csv", avg_velocity_time, delimiter=",")