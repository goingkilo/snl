def recursive_func(k):

 global result
 print(result)
 
 if (k > 0):
    result=result + k*k
    recursive_func(k-1)
 print(result)

 
print("Entering")

result=0
recursive_func(6)