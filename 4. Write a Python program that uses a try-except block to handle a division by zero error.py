num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
def division(num1, num2):
    try:
        answer = num1 / num2
        return answer
    except ZeroDivisionError:
        print ("Error")
print("Result : ",division(num1, num2))
