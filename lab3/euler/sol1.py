total = 0

for num in range(1, 1000): #number range
  if not (num%3) or not (num%5): #check for divisible numbers
    total += num #add relevant numbers to total

print total
