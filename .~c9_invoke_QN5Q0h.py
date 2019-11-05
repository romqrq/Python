def even_number_of_evens(numbers):
    count = 0
    if(numbers == 2):
        return False
    for number in numbers:
        if (number % 2) == 0:
            count += 1
    if (count % 2 != 0 >):        
        return count
    else: return False
    # return sum([1 for num in numbers if num%2==0])

assert even_number_of_evens([]) == False, "No numbers"   
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")