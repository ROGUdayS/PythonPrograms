def enter():
    while True:
        try:
            n = int(input("Enter the number of Records you want to add :"))
            return n
        except:
            print("The entered value is not an Integer!\n Please try again")

def insert():
    a = input("Enter Contact name (must be in alphabets) :")
    while not a.isalpha():
        print("The inputs are not valid! Try again")
        a = input("Enter Contact name (must be in alphabets) :")
    b = input("Enter Contact number (must be numerical with 10 digits) :")
    while len(b)!=10 or not b.isdigit():
        print("The inputs are not valid! Try again")
        b = input("Enter Contact number (must be numerical with 10 digits) :")
    return a,b

def multiple_insertion():
    name=[]
    ph_num=[]
    n=enter()
    for i in range(0, n):
        a,b=insert()
        name.extend([a])
        ph_num.extend([b])
    Directory = dict(zip(name, ph_num))
    return Directory

def search(find):
    for k, v in SortedDirectory.items():
        if k==find or v==find:
            print("The Contact name :{}\nThe Contact number :{}".format(k,v))
            return k, v
    print("Not Found!")

def deletion(find):
    k,v=search(find)
    print("Is Deleted from the Record")
    del SortedDirectory[k]
    return SortedDirectory

def updation(find):
    name=[]
    ph_num=[]
    Record=deletion(find)
    a,b=insert()
    name.extend([a])
    ph_num.extend([b])
    Record1 = dict(zip(name, ph_num))
    Directory = {**Record, **Record1}
    return Directory

print("------Telephone Directory------")
SortedDirectory={}
while True:
    Record={}
    choice=input("""Welcome to the Directory!
    How may we help you?
    1. View the Directory
    2. Insert a Contact
    3. Search for a Contact
    4. Delete a Contact
    5. Update a Contact
    6. Exit the Program
    :""")

    if choice=='1':
        print("---Directory---")
        if len(SortedDirectory) == 0:
            print("The Directory is Empty!")
        else:
            for k, v in SortedDirectory.items():
                print("Name :{}   Number :{}".format(k,v))

    elif choice=='2':
        print("Insert")
        Record =multiple_insertion()
        SortedDirectory = {k: v for k, v in sorted(Record.items())}


    elif choice=='3':
        print("Search")
        Search=input("Input the Contact Name or Number you would like to search :")
        search(Search)

    elif choice=='4':
        print("Delete")
        Search = input("Input the Contact Name or Number you would like to Delete :")
        Record=deletion(Search)
        SortedDirectory = {k: v for k, v in sorted(Record.items())}

    elif choice=='5':
        print("Update")
        Search = input("Input the Contact Name or Number you would like to Update :")
        Record = updation(Search)
        SortedDirectory = {k: v for k, v in sorted(Record.items())}

    elif choice=='6':
        print("exit")
        exit()

    else:
        print("That's not a valid option!")