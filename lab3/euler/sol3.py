num = 600851475143
i = 2 #divide num by and increase
largest_prime = 1

while num > 1:
  if num % i == 0:
	  largest_prime = i
	  num = num // i
  while num % i == 0: #divide by i until no longer possible
	  num = num // i
  i += 1

print largest_prime