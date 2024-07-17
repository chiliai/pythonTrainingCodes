# what is number data type 
# we have are three type of number
# 1. int
# 2. float
# 3. complex

a = 9
# print("The value is: " + str(a) + " , type of: " + str(type(a)))
# print("The value is: {} ".format(a))
print("The value is: {} , type of: {}".format(a, type(a)))

b = 4.5
# print("The value is: " + str(b) + " , type of: " + str(type(b)))

c = 5j
# print("The value is: " + str(c) + " , type of: " + str(type(c)))


# operators

x = 5
y =  2
res_add = x + y
res_sub = x - y
res_mul = x * y
res_div = x / y
res_modulus	 = x % y # باقیمانده
res_exponentiation = x ** y # توان
res_floor_division = x // y # خارج قسمت صحیح

# print("Addition result is: " + str(res_add))
# print("Subtraction result is: " + str(res_sub))
# print("Multiplication result is: " + str(res_mul))
# print("Division result is: " + str(res_div))
# print("Modulus result is: " + str(res_modulus))
# print("Exponentiation result is: " + str(res_exponentiation))
# print("Floor division result is: " + str(res_floor_division))



# --Precedence in mathematical operators

# res = 9 - 2 * 3 # like is: res = (9 - (2 * 3))
# res = 9 - 2 * 3 / 3 # like is: res = (9 - ((2 * 3) / 3))
res = (9 - 2) * 3 / 3 # like is: res =  (( (9 - 2) * 3) / 3 )
# print(res)



