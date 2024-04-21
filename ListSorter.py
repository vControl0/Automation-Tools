list = []




def asc():
  while True:
   print("Instructions: Insert your list on the line!! Every word must have a space!!")

   listInput = input("Insert your list file here: ")
   
   listInput = listInput.split()
   sortedList = sorted(listInput)
   print(sortedList)
   
   
  return



def dsc():
  while True:
   print("Instructions: Insert yourlist on the line!! Every word must have a space!! (d = done)")

   listInput = input("Insert your list file here: ")
   
   listInput = listInput.split()
   sortedList = sorted(listInput, reverse=True)
   print(sortedList)
   
   







def playerPick():
  asc_or_dsc = input("Would you like to sort in order or in order descending (a = ascend and d = descend)(q = quit) ")
  while True:
    if asc_or_dsc == "a":
      asc()
    elif asc_or_dsc == "d":
      dsc()
    elif asc_or_dsc == "q":
      quit
    else: 
      print("Please pick a, d, or q")

        
    return


playerPick()
    
    
    
