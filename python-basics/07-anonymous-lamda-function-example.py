#lambda functions
doSum = lambda a,b: a+b
print(doSum(10,20))

#Use filter function
my_custom_list = [1,2,3,4,5,6,7,8,9,10]
my_filtered_list = list(filter(lambda x: (x>5), my_custom_list))
print(my_filtered_list)

#Use map function
my_custom_list = [1,2,3,4,5,6,7,8,9,10]
my_manipulated_list = list(map(lambda x: x+x,my_custom_list))
print(my_manipulated_list)

