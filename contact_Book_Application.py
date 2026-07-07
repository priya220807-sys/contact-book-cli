import os
def main():
    file_name="contacts.txt"
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        # Add Contact
        if choice == '1':
            name=input("Enter name: ")
            phone=input("Enter phone number: ")
            with open (file_name, 'a') as f:
                f.write(f"{name},{phone}\n")
                print(f"Successfully added contact: {name}, {phone}")
        #View Contacts                
        elif choice == '2':
            print("\n---Saved Contacts---")
            if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
                print("No contacts found.")
            else:
                with open(file_name,"r") as f:
                    for line in f:
                        name,phone=line.strip().split(",")
                        print(f"Name:{name},Phone number:{phone}")
                        
        #Search Contact
        elif choice == '3':
            
            if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
                print("No contacts found.")
                continue
            search_name=input("Enter the name to search:")
            found=False
            with open (file_name,"r") as f:
                for line in f:
                    name,phone=line.strip().split(",")
                    if search_name.lower()==name.lower():
                        print(f"Found contact:Name:{name},Phone number:{phone}")
                        found=True
                        break
            if not found:
                print(f"Contact with name '{search_name}' was not found.")        
        #Delete Contact    
        elif choice == '4':
            if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
                print("No contacts exist to delete.")
                continue
            delete_name=input("Enter the name of the contact to delete:")
            remaining_contacts=[]
            found=False
            with open(file_name,"r") as f:
                for line in f:
                    name,phone=line.strip().split(",")
                    if name.lower()==delete_name.lower():
                        found=True
                    else:
                        remaining_contacts.append(line)
            if found:
                with open(file_name,"w") as f:
                    f.writelines(remaining_contacts)
                print(f"Successfully deleted contact:{delete_name}")
            else:
                print(f"contact with name'{delete_name}' was not found.")
                                
        #Exit
        elif choice == '5':
            print("Thank you for using the contact book application.Goodbye.")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__=="__main__":
    main()