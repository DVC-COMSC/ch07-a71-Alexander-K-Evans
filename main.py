numbers = list(map(int, input().split()))
print(numbers)

avg = sum(numbers)/len(numbers)

for i in range(len(numbers)):
    calc = abs(avg - numbers[i])
    print (f'{calc:.2f}', end=' ')

# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
