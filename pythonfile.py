numbers1 = [1, 2, 3, 4, 5]
numbers2 = [4, 5, 6, 7, 8]
result = map(lambda x,y: x + y, numbers1, numbers2)
print("Addition of 2 lists:", list(result))
num = [1,2,3,4,5]
def square(x):
	return x * x
square = list(map(square, num))
print("Square of each number:", square)