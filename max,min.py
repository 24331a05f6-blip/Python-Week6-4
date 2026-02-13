n=int(input("Enter the size of the list:"))
lst=[]
print("Enter elements")
for i in range(0,n):
    lst.append(int(input(" ")))
print(lst)
print("Maximum element of the list is:",max(lst))
print("Minimum element of the list is:",min(lst))
