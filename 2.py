import matplotlib.pyplot as plt

inf = {}
with open("inf.txt", "r") as file:
    for line in file:
        city, population = line.strip().split(" : ")
        inf[city] = int(population)

cities = list(inf.keys())
populations = list(inf.values())

plt.figure(figsize=(10, 8))
plt.barh(cities, populations, color='skyblue')
plt.xlabel('Населення')
plt.title('Населення городів')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()
