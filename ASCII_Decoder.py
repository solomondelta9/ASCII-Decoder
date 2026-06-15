# ASCII Decoder

nums = [67, 111, 110, 103, 114, 97, 116, 115, 32, 111, 110, 32, 100, 101, 99, 111, 100, 105, 110, 103, 33]

flag = ""

for n in nums:
  flag += chr(n)

print(flag)
