### DateDiff.
DateDiff is a package for calculating distance between dates.

### How to install and use.
To install (from source) you access the file [dist/dateinfo-0.1.tar.gz](https://github.com/Yair-T/DateDiff/blob/main/dist/dateinfo-0.1.tar.gz "dist/dateinfo-0.1.tar.gz") 
You download the file, open CMD, and go to the folder where the file is located.
Then you type the command: 

    pip install dateinfo-0.1.tar.gz

How to use this: 
```python
from DateDiff import DateDiff

date_diff = DateDiff("18/9/2008", "26/9/2008")
print(date_diff.days_difference()) # = 8
```

Successfully!
