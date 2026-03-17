import numpy as np

data1 = np.array([40,30,20,10],dtype=float)
print(data1)

data2 = np.array([[1,2],[3,4]])
print(data2)

data3 = np.zeros((3,4,2))
print(data3)
## arange, full, linspace, np.random.rand()
data4 = np.ones((3))
print(data4)

print(data1.dtype,data2.dtype,data3.dtype,data4.dtype)
## size, T, itmesize

# ----------

list1 = [40,7,99,-3]

list_new = []

for item in list1:
    list_new.append(item+5)

print(list_new)


#data1 = np.array([40,7,99,-3])
#print(data1)

data_1 = np.array([40,7,99,-3])
print(data_1 + 5)

data_2 = data_1 + 5

print(data_2)