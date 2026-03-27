base_price = int(input("Enter the base price: "))
age = int(input("Enter your age: "))
seat_type = input("Enter seat type: ")
show_time = input("Enter show time: ")

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = bool(input("Enter True or False: "))
is_weekend = bool(input("Enter True or False: "))

discount = int(input("Enter the discount: "))
if is_member and age >= 21:
    discount = int(input("Enter the discount: "))
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = int(input("Enter the extra charges: "))
if is_weekend or show_time == 'Evening':
    extra_charges = int(input("Enter the extra charges: "))
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = int(input("Enter the service charges: "))
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:" ,final_price)
else:
    print('Ticket booking failed due to restrictions')
