distance_mi = int(input("Enter the value: "))
is_raining = bool(input("Enter True or False: "))
has_bike = bool(input("Enter True or False: "))
has_car = bool(input("Enter True or False: "))
has_ride_share_app = bool(input("Enter True or False: "))

if distance_mi <= 1 and is_raining == False:
    print('True')
else:
    print('False')

if distance_mi > 1 and distance_mi <=6:
    print('True')
elif has_bike == True and is_raining == False:
    print('True')
else:
    print('False')

if distance_mi > 6 and has_car == True or has_ride_share_app == True:
    print('True')
else:
    print('False')