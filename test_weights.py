import math
a = float(input("Average of grades: "))
b = float(input("Behaviour grade: "))
c = (a+b*1.20) / 2

bias = 1
bias_w = -43.41567745
a_w = 36.90314861
b_w = 43.31242842

a = ((a-1)*1) / (6-1)
b = ((b-1)*1) / (6-1)

neuron = bias*bias_w + a*a_w + b*b_w
result = 1 / (1 + math.exp( -neuron))

if result >= 0.5:
    print("Pass")
else:
    print("Deny")
print(result)
if c >= 4.07:
    print("Pass confirmed")
else:
    print("Not passed")
