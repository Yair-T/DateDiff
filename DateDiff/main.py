#
#  This code by YairT © 2023
#  This code in MIT License
#
from datetime import datetime

class DateDiff:
    def __init__(self, date1, date2):
        self.date1_obj = datetime.strptime(date1, "%d/%m/%Y")
        self.date2_obj = datetime.strptime(date2, "%d/%m/%Y")

    def days_difference(self):
        delta = self.date2_obj - self.date1_obj
        return delta.days
    