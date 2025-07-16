nums = [ 55, 99, 87 , 64  ]

# print(  nums[3] )
# print(  nums[-2] )

print( nums )

nums[2] = "Abrar"
nums.append("Masharib")
nums.append("Sohrab")

pos = nums.index('Masharib')

print( nums )

del( nums[pos] )

# nums.pop()
print( nums )

