p1 = 1
p2 = 2
total = 2
cur = 0

while cur <= 4000000:
    ##debugging print
    ##print "%d = %d + %d" % (cur, p1, p2)
    if cur % 2:
      total += cur #Add current fibonacci number to total if divisible by 2

    cur = p1 + p2 #calculate fibonacci number

    #change previous two numbers for next fibonacci number calculation
    p1 = p2
    p2 = cur


print total

