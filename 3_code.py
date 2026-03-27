running_total = int(input("Enter the running total: "))

num_of_friends = int(input("Enter the number of friends: "))

appetizers = int(input("Enter the price: "))
main_courses = int(input("Enter the price: "))
desserts = int(input("Enter the price: "))
drinks = int(input("Enter the price: "))

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill,2)
print("Each person pays:" ,each_pays)
