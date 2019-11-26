#Takes an array A and index i into A, and rearranges the elements such that all elements less than A[i] (the pivot) appear first, followed by elements equal to the pivot, followed by elements greater than the pivot


#Brute-force solution

def dutchBruteForce(array, pivot_index): 

	#Idea, start with three emepty lists, iterate through array and match each list to greater less than or equal to pivot and then concatenate lists

	less, equal, greater = [], [], []

	for elem in array: 
		if elem < array[pivot_index]: 
			less.append(elem)
		elif elem > array[pivot_index]: 
			greater.append(elem)
		else: 
			equal.append(elem)

	#Concatenate all lists 
		

	return less + equal + greater


print(dutchBruteForce([5, 5, 3, 2, 1, 1, 7, 8, 3, 3, 4, 1, 1, 2, 2, 3], 2))


# we can avoid using O(n) additional space at the cost of increased time complexity as follows. In the first stage, we iterate through A starting from index 0 to index 1, etc. In each iteration, we seek an element smaller than the pivot - as soon as we find it, we move it to the subarray of smaller elements via an exchange. This moves all the elements less than the pivot to the start of the array. The second stage is similar to the first one, the difference being that we move elements greater than the pivot to the end of the array. 


def dutch_flag_partition(pivot_index, A): 
	pivot = A[pivot_index]
	#First pass: group elements smaller than the pivot
	for i in range(len(A)): 
		#look for a smaller element
		for j in range(i+1, len(A)): 
			if A[j] < pivot: 
				A[i], A[j] = A[j], A[i]
				break
	#second pass: group elements larger than the pivot
	for i in reversed(range(len(A))):
		#look for a larger element. Stop when we reach an element less than pivot, since first pass has moved them to the start of A
		for j in reversed(range(i)): 
			if A[j] > pivot: 
				A[i], A[j] = A[j], A[i]
				break

	return A
	
	
print(dutch_flag_partition(3, [5, 5, 2, 3, 1, 1, 2, 2, 1, 5, 7, 8, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 4]))

#Time complexity of above approach is now O(n^2) because in the first pass when searching for each additiounal element smaller than the pivot we start from the beginnning.  However, there is no reason to start from so far back -- we can begin from the last location we advanced to. To improve time complexity, we can make  a single pass and move all the elements less than the pivot to the beginning. In the second pass we move elements to the end. It  is easy to perform each pass in a single iteration, moving out-of-place elemtns as soon as they are discovered. 

def dutch_flag_partition_two(pivot_index, A): 
	pivot = A[pivot_index]
	#First pass: gropu elements smaller than pivot 
	smaller = 0
	for i in range(len(A)): 
		if A[i] < pivot: 
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1
	#Second pass: group elements larger than pivot
	larger = len(A) - 1 
	for i in reversed(range(len(A))): 
		if A[i] > pivot:  
			A[i], A[larger] = A[larger], A[i]
			larger -= 1 
	return A


print(dutch_flag_partition_two(3, [2, 1, 3,  4, 4, 4, 2, 2, 2, 2, 1, 1, 2, 6, 6, 23, 1, 6, 7, 8, 4]))
#The time compexity for this last method is O(n) and the space complexity is O(1)


def dutch_flag_partition_three(pivot_index, A): 
	pivot = A[pivot_index]
	#Keep the following invariants during partitioning: 
	#Bottom group: A[:smaller]
	#Middle group: A[smaller: equal]
	#Unclassified group: A[equal:larger]
	#top group: A[larger: ]
	smaller, equal, larger = 0, 0, len(A)
	#keep iterating as long as there is an unclassified element
	while equal < larger: 
		#A[equal] is the incoming unclassified element
		if A[equal] < pivot: 
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller + 1, equal + 1
		elif A[equal] == pivot: 
			equal += 1: 
		else: #A[equal] > pivot
			larger -= 1 
			A[equal], A[larger] = A[larger], A[equal]

	
	return A 

#Each iteration decreases the size of unclassified by 1, and the time spent within each iteration is O(1), implying the time complexity is O(n). The space complexity is clearly O(1)


