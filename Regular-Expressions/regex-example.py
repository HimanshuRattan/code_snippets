import re
regex = '^[0-9]{10}$'
phone="999999999"
if re.search(regex, phone):
    print ('Valid phone number')
else:
    print ('Invalid phone number')
