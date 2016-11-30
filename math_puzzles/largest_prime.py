n = 600851475143
newn = n
largestFact = 0

counter = 2
while counter * counter <= newn:
    if newn % counter == 0:
        newn = newn/counter
        largestFact = counter
    else:
        counter = counter + 1

if newn > largestFact:
    largestFact = newn

print(largestFact)

