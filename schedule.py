import datetime
x = datetime.datetime.today().weekday()
x = x+1

if x == 1:
    classes = '''
3:30-5:30       |       VMC
6:00-8:00       |       VMC
'''

elif x == 2:
    classes= '''
5:30-7:00       |       Benu Ma'am (85905636765)    (390467)
'''
elif x == 3:
     classes = '''
3:30-5:30       |       VMC
6:00-8:00       |       VMC
'''   

elif x == 4:
    classes = '''
                |       Nitish Sir (3105888379) (2vcE3E)
'''

elif x == 5:
    classes= '''
3:30-5:30       |       VMC
6:00-8:00       |       VMC
'''

elif x == 6:
    classes= '''
5:15-6:45       |       Benu Ma'am (85905636765) (390467)
'''

elif x == 7:
    classes = '''
No classes :)
'''
print("Classes for today")
print(classes)
