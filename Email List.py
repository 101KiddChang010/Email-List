
#   outputting menu for user accessibility
def menu():
    print("Menu")
    print("------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    print("")

#   searches name in document/dictionary for name and email address
def lookUp(d):
    ui = input("Enter a name: ")

    #successfully finds name and email if detected in dictionary
    if ui in d:
        print("Name:", ui)
        print("Email:", d[ui])

    #error if name isn't detected in dictionary
    else:
        print("The specified name was not found")

#   adds name and dictionary to document/dictionary
def add(d):
    name = input("Enter name: ")
    email = input("Enter email address: ")

    #adds name to dictionary if detected in dictionary
    if name in d:
        print("That name already exists")

    #error if name is not detected in dictionary
    elif name not in d:
        d[name] = email
        print("Name and address have been added")

#   changes email address of an already defined name in document/dictionary
def change(d):
    name = input("Enter name: ")
    email = input("Enter the new address: ")

    #changes email address if name is detected in dictionary
    if name in d:
        d[name] = email
        print("Information updated")

    #error if name is not detected in dictionary
    elif name not in d:
        print("That name doesn't exist")

#   deletes name and email address of an already defined name in document/dictionary
def delete(d):
    name = input("Enter name: ")

    #deletes user name if name is detected in dictionary
    if name in d:
        d.pop(name)
        print("Information deleted")
    
    #error if user name is not detected in dictionary
    elif name not in d:
        print("Specified name not found")

#   reads names and emails from the document and returns it as a python dictionary
def load():
    #loads email document/file if it exists already
    try:
        f = open("email.txt", "r")

        d = {}

        #creates python dictionary by splitting up each line of the document and splitting the names/email addresses
        for line in f:
            l = line.split()
            d[l[0]] = l[1]

        f.close()

        return d

    #creates new email document/file if it doesn't exist
    except:
        f = open("email.txt", "a")
        d = {}
        f.close()

        return d

#   saves changes made in python dictionary to the document
def save(d):
    #erases all information of the user document
    f = open("email.txt", "w").close

    #creates the user document
    f = open("email.txt", "a")

    for key,value in d.items():
        f.write("{:10}{}".format(key,value) + "\n")

    f.close()

#   main function/line to run program
def main():
    emails = load()

    #start of user inputs
    menu()
    ui = int(input("Enter your choice: "))

    if ui == 5:
        save(emails)
        print("Information Saved")

    #user input loop
    while ui != 5:
        if ui == 1:
            lookUp(emails)
            print()
            menu()
            ui = int(input("Enter your choice: "))

            #if user inputs 5 while in if 1
            if ui == 5:
                save(emails)
                print("Information Saved")

        elif ui == 2:
            add(emails)
            print()
            menu()
            ui = int(input("Enter your choice: "))

            #if user inputs 5 while in elif 2
            if ui == 5:
                save(emails)
                print("Information Saved")

        elif ui == 3:
            change(emails)
            print()
            menu()
            ui = int(input("Enter your choice: "))

            #if user inputs 5 while in elif 3
            if ui == 5:
                save(emails)
                print("Information Saved")

        elif ui == 4:
            delete(emails)
            print()
            menu()
            ui = int(input("Enter your choice: "))

            #if user inputs 5 while in elif 4
            if ui == 5:
                save(emails)
                print("Information Saved")
        
        else:
            print("***invalid choice***")
            ui = int(input("Please enter a valid choice: "))

            #if user inputs 5 while in else
            if ui == 5:
                save(emails)
                print("Information Saved")

main()
