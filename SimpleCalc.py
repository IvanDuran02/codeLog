from time import sleep

#avalible operations to perform.

def add(num1, num2):

  result = num1 + num2

  return print(result)

  

def sub(num1, num2):

  result = num1 - num2

  return print(result)

  

def multiply(num1, num2):

  result = num1 * num2

  return print(result)

  

def divide(num1, num2):

  result = num1 / num2

  return print(result)

while True:

#prompting user for a operation

  userinput = str(input("what would you like to do today sir!\n[add][sub][multiply][divide]\n"))

#promt user for 2 numbers 

  num1 = float(input(f"give me your first number to {userinput}\n"))

  num2 = float(input("now the 2nd please!\n"))

#if user enters "add" this is executed.

  if userinput.lower() == "add":

    add(num1, num2)

    break

#if user enters "sub" this is executed.

  elif userinput.lower() == "sub":

    sub(num1, num2)

    break

#if user enters "multiply" this is executed.

  elif userinput.lower() == "multiply":

    multiply(num1, num2)

    break

#if user enters "divide" this is executed.

  elif userinput.lower() == "divide":

    divide(num1, num2)

    break

#else user will be promoted to re-enter values.

  else:

    print(f"sorry {userinput} wasn't a choice! try again.")

    sleep(2)

 

