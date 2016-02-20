p1 = 1
p2 = 2
count = 2
cur = 0

##based on euler 2
while len(str(cur)) <= 1000:
    ##debugging print
    ##print "%d = %d + %d" % (cur, p1, p2)
    count += 1
    if len(str(cur)) == 1000:
      print count
      break;#break after the first 1000 digit fibonacci

    cur = p1 + p2 #calculate fibonacci number

    #change previous two numbers for next fibonacci number calculation
    p1 = p2
    p2 = cur