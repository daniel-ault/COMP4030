#!/usr/bin/python

# Write an algorithm that takes a number as a string, and removes any recurring digits.
# The changes must be in-place.
# Expected time complexity O(n) and auxiliary space (?) O(1)
#
# Example: 
#    Input:  "1299888833"
#    Output: "12983"


def remove_recurring_digits(s):
	newstring = s[0]
	
	for i in range(1, len(s)):
		if s[i] != newstring[len(newstring)-1]:
			# remove digit at i+1
			newstring += s[i]
	
	return newstring

s = '1299888833'

print remove_recurring_digits(s)
		 		
