def is_diserium(num):
    return num == sum(int(digit) ** (i+1) for i, digit in enumerate(str(num)))

n = int(input("Enter a number: "))
print("disarium number" if is_diserium(n) else "not a disarium number")
