"""
Exercise  6.5: Take the following Python code that stores a string:

string = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extraced string
into a floating number.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

string = 'X-DSPAM-Confidence: 0.8475'

colpos = string.find(':')                  #finds the colon character
number = string[colpos+1:]                 #extracts portion after colon
confidence = float(number)              #converts to floating point number
print(confidence)