import jeans


print("Mutable objects point to the same id even when changed.")
closet = ['shirt', 'hat', 'pants','jacket', 'socks']
print(id(closet), end = " ")
closet.remove('hat')
print(id(closet))
print("Immutable objects don't")
answer = "You're wearing that?"
print(id(answer), end=" ")
answer += " I'm glad you finally got the chance to finally wear it!"
print(id(answer)) #The original string is NOT modified, a new string is created in the background

print()
name = "Wanda"

print(type(name))
# print(dir(name))
print()
'''
Classes are our way of creating our own objects
'''

pants = jeans.Jeans(34, 180, "blue")
pants.put_on()

print()

print(type(pants))
# print(dir(pants))

briefs = pants

print(f"\nI have two variables 'pants' and 'briefs'... Their ids are {id(pants)} and {id(briefs)} respectively because they reference the same object.")
print(pants is briefs)

print()
casual_pants = jeans.Jeans(32, 30, "black")
print(pants is casual_pants, id(pants),'!=', id(casual_pants))