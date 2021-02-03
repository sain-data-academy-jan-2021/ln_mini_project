def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")
    
    return input("What would you like to do? ")
    

### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        print("\nHere are the people I know.\n")
        for name in names:
            print(name.title())
    elif choice == '2':
        new_name = input("\nPlease tell me this person's name: ")
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())
    elif choice == 'q':
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")


        import pickle

# This program asks the user for some animals, and stores them.

# Make an empty list to store new animals in.
animals = []

# Create a loop that lets users store new animals.
new_animal = ''
while new_animal != 'quit':
    print("\nPlease tell me a new animal to remember.")
    new_animal = input("Enter 'quit' to quit: ")
    if new_animal != 'quit':
        animals.append(new_animal)

# Try to save the animals to the file 'animals.pydata'.
try:
    file_object = open('animals.pydata', 'wb')
    pickle.dump(animals, file_object)
    file_object.close()
    
    print("\nI will remember the following animals: ")
    for animal in animals:
        print(animal)
except Exception as e:
    print(e)
    print("\nI couldn't figure out how to store the animals. Sorry.")

grades = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}

import pickle              # import module first

#fill user inputs 
f = open('gradesdict.pkl', 'w')   # Pickle file is newly created where foo1.py is
pickle.dump(grades, f)          # dump data to f
f.close()    