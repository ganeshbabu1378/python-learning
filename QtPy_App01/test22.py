from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print (datetime_object.year)
print (datetime_object.month)
print (datetime_object.day)

print(type(datetime_object))
print(datetime_object)  # printed in default format