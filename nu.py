import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
#Task 1 a)


print('Task 1 a)')
a = np.zeros((4,3))
print(a)
b = np.ones((4,3))
print(b)
c = np.arange(12).reshape(4,3)
print(c)

#Task 1 b)
print('Task 1 b)')
def F(x):
    return 2 * x**2 + 5

x_values = np.arange(1, 101)


y_values = F(x_values)


df = pd.DataFrame({'x': x_values, 'F(x)': y_values})
#Вивід строкою
print(df)
#ГРАФІЧНО
plt.plot(x_values, y_values, marker='o')
plt.title('Plot of F(x) = exp(-x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.show()
#Task 1 c)
print('Task 1 c)')
def F(x):
    return np.exp(-x)


x_values = np.arange(-10, 11, 1)


y_values = F(x_values)



df_exponential = pd.DataFrame({'x': x_values, 'F(x)': y_values})
#Вивід строкою
print(df_exponential)

#ГРАФІЧНО
plt.plot(x_values, y_values, marker='o')
plt.title('Plot of F(x) = exp(-x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.show()


