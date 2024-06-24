# You shouldn't expect an object to stay at the same index in a list if you're insert and removing 
# This shifts thongs around

row = ['Ford', "Audi", "BMW", "Lexus"]
row.append('Mercedes')
print(row)
row[2] = "Jeep"
print(row)
row.append('Honda')
row.insert(0, 'Kia')
print(row[2])
print(row.index('Jeep'))
#row.pop(row.index('Jeep'))
row.remove('Jeep')

# I'm starting to think that my issue wa the fact that my base intepreter was python 3.11 while everything else was updated. Could that have been it?

for car in row:
    print(car)


work = ("37.4221° N", "122.0853° W")
print(type(work))