# Sorting list of numbers

n = int(input("Enter an array size"))
number1 = []
print (f"The Value of N is :{n}")

for i in range (0, n ):
    {
      number1.append(int(input("Enter Numbers{i}: ")))
  }
print(number1)
print (number1[0], number1[1], number1[2], number1[3])

j = 0
while j < 4:
    if number1[j] > number1[j+1]:
        k = number1[j]
        number1[j] = number1[j+1]
        number1[j+1] = k
        j = 0
    else:
        j = j+1


#===============================================================================
# 
# for j in range (0, n-1):
#         if number1[j] > number1[j + 1]:
#             k = number1[j]
#             print (k, j)
#             number1[j] = number1[j + 1]
#             number1[j + 1] = k
#             j = 0
#         else:
#              print(number1[i])
#             
#===============================================================================
        
for j in range (0, n-1):
    print ("Numbers Sorted are : {number1[j]}")
    
