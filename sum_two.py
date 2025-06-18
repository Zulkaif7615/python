def sum_two_num(arr,target):
    seen = {}
    for i,num in enumerate(arr):
        # print(f"i-{i} and num-{num}")
        complement = target - num
        # print(complement)
        # print(seen)
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
        
        
arr = [23,34,45,65,55,24,25,23]
# print(enumerate(arr))
target = 100
result = sum_two_num(arr,target)
# print(result)

# ///////////////////////////////
# findng a first repeationg element
def first_repeating_elements(arr):
    seen = set()
    for num in arr:
        if num in seen:
            # return arr[num]
            return num
        seen.add(num)
        print(seen)
    return None


arr = [23,34,45,23]
# print(first_repeating_elements(arr))


# ///////////////////////
# find first non-repeating character
def first_non_repeating_char(s):
    char = {}
    for c in s:
        char[c] = char.get(c,0)+1
        # print(char)
    for i , c in enumerate(s):
        # print(f"i-{i} , char-{c} and s-{s}")
        if char[c] == 1:
            return c
    return -1

print(first_non_repeating_char("hhhhelo"))