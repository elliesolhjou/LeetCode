'''
Write code to reverse the contents of an array. 
'''
# ucberkeley dsa course
def reverseArray(arr):
    revArr = []
    for n in arr[::-1]:
        revArr.append(n)
        # print(revArr)
        arr.pop()
    
    print(f"arr is {arr}")
        
    return revArr
print(reverseArray([1,2,3,4]))
