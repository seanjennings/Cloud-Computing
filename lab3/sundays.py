from datetime import date #import for date to day number(0-6) conversion

#counter for sundays
s_counter = 0

#set up basic loops for program
for y in range(1901, 2001):#relevant years for loop
  for m in range(1, 13):#loop for all months
    d = date(y, m, 1)#create date with year and month
    if d.weekday() == 6: #check if current day number is equiv. to a sunday
      s_counter += 1 #increment sunday counter

print "Sundays: ", s_counter