#max subarray sum is index 1 through index 5 = 10
array = [-1, 2, 4, -3, 5, 2, -5, 2]
p, s = 0, 0


for i in range( len(array) ):
	#s finds max of curr_element vs curr_element + prev_element 
	#this builds the sum
	s = max( array[i], s + array[i] )
	#p then takes max of s vs previously stored max in p 
	p = max( p, s )
	print ("S: ", s, "P: ", p)