T=("apple","banana","cherry","mango","grapes","orange")
print("The tuple is ",T)
print("\nsecond fruit is:",T[1])
print("\n from 3-6th fruit is:",T[2:6])
print("\n list all the items in tuple:")
for x in T:
    print(x)
    if "apple" in T:
        print("\n yes, apple is in the tuple")
        print("\n total number of items in the tuple is:",len(T))
        