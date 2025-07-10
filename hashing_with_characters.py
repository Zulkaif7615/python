s = "azyyzaaaa"
q = ['d','a','y','x']

hash_list = [0] * 27
for ch in s:
    acsii_value = ord(ch)
    index = acsii_value - 97
    hash_list[index] += 1
    
print(hash_list)

for ch in q:
    print(ch,end="-")
    acsii_value = ord(ch)
    index = acsii_value - 97
    print(f"ocurrance-{hash_list[index]}")