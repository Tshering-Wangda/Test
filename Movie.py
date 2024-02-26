print("This is to determine if the person is eligible for a discount on a movie ticket or not.")
Age_check = int(input("Enter your age: "))
Std_check = input("Are you a student? (Yes/No): ")

if (Age_check <= 12 ):
    print("You are eligible for a discount on the movie ticket.")

elif (13 <= Age_check <= 18 and Std_check == "Yes"):
    print("You are eligible for a discount on the movie ticket.")

else:
    print("You are not eligible for a discount on the movie ticket. ")