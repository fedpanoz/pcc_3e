# write a function that returns thwe larger of two numbers
# input is two numbers
#output is the larger of the two numbers
def larger_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(larger_of_two(5, 10)) # 10
print(larger_of_two(10, 5)) # 10
