def getInput():
   try:
       n = int(input("Enter an integer :"))
       return n
   except ValueError:
       print("That's not an integer!")

getInput()
