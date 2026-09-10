# WEEK 3 – LOOPS

# Example 1: for loop
for i in range(5):
    print("Hallo")


# Example 2: range()
for i in range(2, 6):
    print(i)


# Example 3: range() with step
for i in range(0, 10, 2):
    print(i)


# Example 4: for + if
for i in range(1, 11):
    if i >= 5:
        print(i)


# Example 5: loop through a list
names = ["Anna", "Maria", "Liubov"]

for name in names:
    print(name)


# Example 6: list + condition
scores = [45, 72, 90, 33, 81]

for score in scores:
    if score >= 50:
        print(score)


# Example 7: while loop
count = 1

while count <= 5:
    print(count)
    count = count + 1


# Example 8: break
for i in range(10):
    if i == 5:
        break
    print(i)


# Example 9: continue
for i in range(5):
    if i == 2:
        continue
    print(i)
