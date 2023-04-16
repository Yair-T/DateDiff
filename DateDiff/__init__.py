# 
#  This code by YairT © 2023 
#  This code in MIT License
#

from .main import DateDiff

if __name__ == "__main__":
    date_diff = DateDiff("8/18/2008", "9/26/2008")
    print(date_diff.days_difference())