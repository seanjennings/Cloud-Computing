def palindrome_test(string):
    if len(string) < 1: #if latest string passed in has been shortened down to < 1 character, then it is a palindrome
        return True
    else:
        if string[0] == string[-1]: #if the two corresonding characters either side of the centre match, continue
            #print string[0], ' == ', string[-1]     #test chars being compared
            return palindrome_test(string[1:-1]) #call the function recursively, working from the middle of the string out
        else:
            return False #if any two corresponding characters do not match then the string is not a palindrome

#output test reusults
print 'Oxo \t\t', palindrome_test('Oxo')
print 'OXO \t\t', palindrome_test('OXO')
print '123454321 \t', palindrome_test('123454321')
print 'ROTATOR \t', palindrome_test('ROTATOR')
print '12345	54321 \t', palindrome_test('12345	54321')