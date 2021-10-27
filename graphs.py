import csv
import matplotlib.pyplot as plt

file = open('maschools.csv')
r = csv.reader(file)
data = list(r)

district = []
biling = []

# district
x1 = (data[6][2])
district.append(x1)
x2 = data[154][2]
district.append(x2)
x3 = data[219][2]
district.append(x3)
    
# bilingual
y1 = int(data[6][5])
biling.append(y1)
y2 = int(data[154][5])
biling.append(y2)
y3 = int(data[219][5])
biling.append(y3)


# plot bar graph
plt.bar(district, biling, color = 'b', width = 0.72)
plt.xlabel('District', fontweight='bold')
plt.ylabel('Number of Bilingual Students', fontweight='bold')
plt.legend()
plt.savefig('bilingual_students_in_ma_school_districts.jpg')
plt.show()

'''
Graph #2
'''

file = open('parliament.csv')
r = csv.reader(file)
data = list(r)

year = []
average = []

# year
x2 = data[2][2]
year.append(x2)
x3 = data[3][2]
year.append(x3)
x4 = data[4][2]
year.append(x4)
x5 = data[5][2]
year.append(x5)
x6 = data[6][2]
year.append(x6)
x7 = data[7][2]
year.append(x7)
x8 = data[8][2]
year.append(x8)
x9 = data[9][2]
year.append(x9)
x10 = data[10][2]
year.append(x10)
    
# total average
y2 = int(float(data[2][6]))
average.append(y2)
y3 = int(float(data[3][6]))
average.append(y3)
y4 = int(float(data[4][6]))
average.append(y4)
y5 = int(float(data[5][6]))
average.append(y5)
y6 = int(float(data[6][6]))
average.append(y6)
y7 = int(float(data[7][6]))
average.append(y7)
y8 = int(float(data[8][6]))
average.append(y8)
y9 = int(float(data[9][6]))
average.append(y9)
y10 = int(float(data[10][6]))
average.append(y10)

# plot the data
fig, ax = plt.subplots()
ax.plot(year, average)
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Average Seats Held by Women in National Parliament', fontweight='bold')
plt.legend()
plt.savefig('women_in_national_parliament.jpg')
plt.show()

# ignore the rest

'''
file = open('lax.csv')
r = csv.reader(file)
data = list(r)

dom_flights = 0
int_flights = 0
for i in range(1, 1450):
    if data[i][4] == 'Domestic':
        dom_flights += int(data[i][5])
    if data[i][4] == 'International':
        int_flights += int(data[i][5])

print (dom_flights)


flights = ['Domestic', 'International']
counts = [dom_flights, int_flights]

plt.bar(flights, counts, color = 'b', width = 0.72)
plt.xlabel('Flight Type from LAX', fontweight='bold')
plt.ylabel('Number of flights', fontweight='bold')
plt.legend()
plt.savefig('lax_flights.jpg')
plt.show()
'''