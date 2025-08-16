def addition():
    questionone = int(input("Hey user give me a number to input:"))
    questiontwo = int(input('Hey user give me a second number to input:'))
    answer = questionone + questiontwo

    if answer % 2 == 0:
        print(f"The sum of {questionone} and {questiontwo} is {answer} which is even.")
    else:
        print(f"The sum of {questionone} and {questiontwo} is {answer} which is odd.")

addition()