# count numbers in list
# create a function 
def count_numbers():
	x=[1,2,2,3,3,3]
	y=int(input()) 
	for b in x:
		if y==b:
			print("count_numbers=",y)
# call function   
count_numbers()