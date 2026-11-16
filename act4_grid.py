
n = int(input("Size: "))

while n < 1 or n > 10:
    n = int(input("Enter size (1-10): "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
