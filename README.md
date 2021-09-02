# Perceptron-One
My first try of "machine learning" algorithm from scratch

Perceptron learns to pass or reject "someone" by inputs "average of grades" and "behaviour grade", basically something like teacher who check student.
Threshold is set to **4.07** by default (average of **(average of grades and behaviour)**)

***main.py*** - file is for learning, also shows graph with data
***test_weights.py*** - is for testing those weights (needs manually type in directly into code bias_w, a_w and b_w)

in ***main.py*** you can change those variables as you want for fun
*Defining variables:*
eta=0.2
epochs=1000
students = 27*4
grades = 7
threshold = 4.07
beh = 1.20
above_thr = 0
