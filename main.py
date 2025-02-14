name = input("Enter Your Name: ")

print(f"Hello , {name}!")

## Start Interactive Fiction
while True:
    print("""You entered a room with a table and chair.
      
    OPTIONS:
    1. Look under the table
    2. Sit down""")
 
    choice = input("What would you do: ")

    if choice == "1":
         print(f"You found a key under the table.")
    elif choice == "2":
         print(f"You sit down and relax.")
         break
    else:
         print(f"Invalid, {name} Pause.\N")    




