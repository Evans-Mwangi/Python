	def max_of_three(nums):
	    maximum = max(nums)
	    print (maximum)

	max_of_three([16,20,4])

	def length (string):
	    count=0
	    for c in string:
	        count+=1
	    print (count)

	length('Hello World')

	def character(string1):
		vowels = [a, e, i, o, u]
		string1  = string1.lower()
		return string1.lower() in vowels
	character('a')
