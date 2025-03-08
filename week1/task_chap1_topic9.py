a=7
b=4

#bitwise xor
print(a^b)
"""
here :
111(7)
100(4)
_______
011(3) ->answer
"""
#bitwise not

print(~a)
"""
111(7)
_______
000(0)

2's complement of 000  
 111
 + 1
_____
1000(-8 in sign representation)
"""

print(~b)
"""
100(4)
______
011(3) 

2's complement of 011
 
 100
 + 1
_____
 101(-5 in sign representation)
"""