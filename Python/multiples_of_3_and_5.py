# Find numbers that are multiples of 3 and 5 and finds their sum

multiples = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
sum_multiples = sum(multiples)
print("sum =", sum_multiples)
