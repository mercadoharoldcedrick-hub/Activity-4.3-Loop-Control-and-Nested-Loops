
total = 0

for i in range(1, 51):
    if i % 3 == 0:
        continue

    print(i, end=" ")
    total += i

print("\nSum:", total)
