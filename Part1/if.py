# if=dose some codes only if a condition is true
#  else does nothing

age = int(input("type your age"))

if age>=18 and age<100:
    print("You are an adult")
elif age>100:
    print("You are not human")
elif age<0:
    print("You haven't been born yet")
else:
    print("You are a child")