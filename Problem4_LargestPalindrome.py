import math
largest_palindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        num_str = str(num)
        num_str_len = len(num_str)
        if num_str[0:int(math.ceil(num_str_len/2))] == num_str[int(num_str_len):int(math.floor(num_str_len/2)-1):-1]:
            if num > largest_palindrome:
                largest_palindrome = num

print(largest_palindrome)
