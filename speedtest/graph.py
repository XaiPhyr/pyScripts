import matplotlib.pyplot as plt

file = open('data', 'r')
read = file.read()
item = read.split(',')

x = []
y = []

for i in range(len(item) - 1):
    x.append(i + 1)
    y.append(int(item[i]))

# y.sort()

print(x, y)

plt.plot(x, y)
plt.xlabel('No. of Data')
plt.ylabel('Data Value')
plt.title('Internet Speed')
plt.show()
