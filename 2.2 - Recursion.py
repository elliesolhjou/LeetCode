'''
Write a function to reverse a string or an array recursively.
'''
arr= [1,2,3,4,5]
def recursion(data):
    # def base ase
    if len(data) <= 1:
        return data

    # def recursion
    # break it to smaller process 
    return recursion(data[1:])+ [data[0]]

input_arr = [1, 2, 3, 4, 5]
print(recursion(input_arr))


