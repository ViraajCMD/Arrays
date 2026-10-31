import array as arr

array_num = arr.array('i', [1,3,5,3,7,9,3])
print("Original Array: "+str(array_num))

print("\nThe number of occurences of the number 3 in the array is:"+str(array_num.count(3)))

array_num.reverse()
print("The reverse order of the Array is:")
print(str(array_num))
