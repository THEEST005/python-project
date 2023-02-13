try:
  def age():
    age=int(input("Enter Your Age"))
    print(age)
    result=age*12
    print(f"Age in months is {result}")
  age()
except:
     print("Not a Number")