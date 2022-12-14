class Contact:
    def __add_contact__(self):
        my_data = dict()
        key = input("Enter a Name: ")
        if key != 'q':
         value1 = input("Enter a Phone: ")
         value2 = input("Enter a Mali: ")
         my_data[key] = value1,value2
        return f'Contact has stored'

contact = Contact()
print(contact.__add_contact__())

