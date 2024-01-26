A python program that calculates the sum of a given range of numbers with 
specified start, stop, and step arguments. This program is based on 
Carl Friedrich Gauss' formula for calculating the sum of n consecutive integers:
S = n(n+1) / 2.

Proof of Gauss' formula
Given a range of numbers 1 to n to add,
S = 1 + 2 + 3 + 4 + 5 + ... + n
S = n + (n-1) + (n-2) + (n-3) + (n-4) + ... + 1

Add both range of numbers:
(S+S) = (n+1) + (n-1+2) + (n-2+3) + (n-3+4) + (n-4+5) + ... + (n+1)

Simplify:
2S = (n+1) + (n+1) + (n+1) + (n+1) + (n+1) + ... + (n+1)

Since there are n numbers of (n+1),
2S = n(n+1)

Divide both sides by 2 to get rid of the coefficient of S
S = n(n+1) / 2

Implementing this formula in python is pretty straight forward if you are 
dealing with the sum of consecutive integers for 
example: range(start=1, stop=10000, step=1) 
s = 10000*(10000+1) // 2 
This will output `50005000`. If the step is not 1, then we have to get the first
and last element in the sequence to better implement the algorithm as done in 
this program.
