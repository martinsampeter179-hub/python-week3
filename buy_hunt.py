count = 1
total = 0

# BUG: Added missing colon `:` at the end of the while header (SyntaxError).
# BUG: Changed `count < 5` to `count <= 5` so the loop includes the number 5 (Logic Error).
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted integer `total` to a string using `str(total)` to prevent TypeError during string concatenation.
print("Sum of 1 to 5 is: " + str(total))
