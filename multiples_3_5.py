def multiples(n):

	print (sum(set(list(range(3, n, 3)) + list(range(5, n, 5)))))

print (multiples(10))



# def multiples(n):

# 	first_sum = sum(range(3, n, 3))

# 	return first_sum + sum(x for x in range(5, n, 5) if x % 3)

# 	# # for number in range(0, n, 5):
# 	# 	if number % 3 == 0:
# 	# 		continue
# 	# 	else:
# 	# 		total += number
# 	# 	# if num % 3 == 0 or num % 5 == 0:

# 	# print (total)

# print (multiples(10))




# def multiples(n):
# 	total = 0
# 	for num in range(0, n, 3):
# 		total += num

# 	for number in range(0, n, 5):
# 		if number % 3 == 0:
# 			continue
# 		else:
# 			total += number
# 		# if num % 3 == 0 or num % 5 == 0:

# 	print (total)

# print (multiples(10))



# def multiples(n):
# 	total = 0
# 	result = sum([num for num in range(n) if num % 3 == 0 or num % 5 == 0])
# 	print (result)

# print (multiples(10))




# def multiples(n):
# 	total = 0
# 	for num in range(n):
# 		if num % 3 == 0 or num % 5 == 0:
# 			total += num
# 	return total


# t = int(input().strip())
# for a0 in range(t):
# 	n = int(input().strip())
# 	multiples(n)