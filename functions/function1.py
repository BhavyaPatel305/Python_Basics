def fun(array):
    array1 = []
    for i in array:
        reverse_num = int(str(i)[::-1])
        array1.append(reverse_num)
    return array1

print(fun([11,23,67,89]))
        
        
        