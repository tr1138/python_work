def display_message():
    print("Functions are named blocks of code that can be called repeatadly "
          "during program execution.\nThey can accept arguments which are "
          "passed to parameters that can be used in the function.")
    
print("display_message() funciton being called 5 times")
i = 0
while i < 5:
    display_message()
    i += 1
    print()