'''
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"Total even numbers are {count}")        '''


''' count = 15
while range(count > 3):
    print("Hello MR Adithya")
else:
    print("You have started to learn things") '''

''' print("list Iteration")
l = ["Adi", "divya", "vani"]
for i in l:
    print(i)

print("\n Tuples Iteration")    
t = ("Y", "i", "j")
for i in t:
    print(i)

print("String Iteration")
s = ("Superb")
for i in s:
    print(i)   

print("Dictanories Iteration")
'''

numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(1, len(numbers)):
    total += numbers[i]
    print(total)