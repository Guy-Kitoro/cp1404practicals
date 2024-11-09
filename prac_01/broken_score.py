"""
Program to evaluate the user's score and determine its validity.
Scores must be between 0 and 100 inclusive:
- 90 or more is excellent
- 50 or more but less than 90 is a pass
- Below 50 is bad
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
