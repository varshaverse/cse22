nums = []
 
x = int(input())
 
while x >= 0:
    nums.append(x)
    x = int(input())
 
#total = sum(nums)

total = 0
for num in nums:
    total += nums
print(f'Your numbers add up to {total}')
