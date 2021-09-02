# Perceptron_one
import numpy as np
import matplotlib.pyplot as plt
import math
import copy
import random

def sigm(x):
    return 1 / ( 1 + math.exp(-x))
def show_me(data,students):
    fig, ax = plt.subplots()
    xmin, xmax = 0, 1.1
    z = np.arange(xmin,xmax,1)
    for x in range(students):
        if data[x,3] == 1:
            ax.scatter(data[x,1],data[x,2],color="g")
        else:
            ax.scatter(data[x,1],data[x,2],color="r")
    ax.set_xlim([xmin,xmax])
    ax.set_ylim([0,1.1])
    plt.show()

# Defining variables
eta=0.2
epochs=1000
students = 27*4
grades = 7
threshold = 4.07
beh = 1.20
above_thr = 0

# Creating arrays and random Data
dataset = np.random.randint(1,7,size=(students,grades))
if_passed = np.zeros([students,1])
total_avg = np.zeros([students,1])
bias = np.ones([students,1])
avg = np.zeros([students,1])
beh_grade = np.random.randint(1,7,size=(students,1))

# Calculating average of grades of each student into another array
for n in range(students):
    avg[n] = np.mean(dataset[n])

# Checking global average of data so I can check if Perceptron is right
for x in range(students):
    total_avg[x] = (avg[x] + beh_grade[x] * beh) / 2
    if total_avg[x] > threshold:
        if_passed[x] = 1
    else:
        if_passed[x] = 0


data = np.column_stack((bias,avg,beh_grade,if_passed))

datar = data.copy()

# Changing scale to 0-1
for i in range(students):
    datar[i,1] = (((data[i,1] - 1) * (1-0)) / (6-1)) + 0
    datar[i,2] = (((data[i,2] - 1) * (1-0)) / (6-1)) + 0

# ~99.5% correct -> w = [-43.41567745, 36.90314861, 43.31242842] for Threshhold = 4.07
w = [-1, 1, 1]
nw = np.empty([3,1])
neuron = np.empty([students,1])
error = np.zeros([students,1])
perccorr = 0

# Learning loops
for i in range(epochs):
    for i in range(students):
        neuron[i] = sigm(datar[i,0]*w[0] + datar[i,1]*w[1] + datar[i,2]*w[2] )
        error[i] = math.pow((neuron[i] - datar[i,3]),2)
    result = np.column_stack((neuron,error,datar[:,3]))
    for q in range(students):
        for i in range(len(w)):
            z1 = 2 * (datar[q,3] - neuron[q]) * (-1)
            z2 = neuron[q] * (1 - neuron[q])
            z3 = datar[q,i]
            z4 = z1 * z2 * z3
            w[i] = w[i] - eta * (z4)

    print("Error = ",np.mean(error))
            
dota = 0
print(w)# Test weights
for i in range(10000):
    a = random.uniform(1,6)
    b = random.uniform(1,6)
    tavg = (a+b*beh) / 2
    a = ((a-1)*1) / (6-1)
    b = ((b-1)*1) / (6-1)
    nneu = sigm( (w[0] )+ (a*w[1]) + (b*w[2]))
    if nneu >= 0.5:
        nneu = 1
    else:
        nneu = 0
    if tavg >= threshold:
        tavg = 1
    else:
        tavg = 0
    if tavg == nneu:
        dota = dota + 1
        
# Show results
print("#############  ",students, " Examples. ###############")
print("with epochs: ", epochs,"  and learning rate: ",eta," % of being correct is: ")
print(dota/100)
print("###########################################################")
show_me(datar,students)