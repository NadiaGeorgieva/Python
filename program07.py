Array_size=int(input("enter size of array:"))
Array=[]
print("enter the elements of array:")
for i in range(Array_size):
	elements=int(input())
	Array.append(elements)
	if i==Array_size:
		break
print("Stored elements are:",Array)
