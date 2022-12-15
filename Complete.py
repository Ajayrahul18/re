class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email

class ContactMap:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, contact):
        self.contacts[contact.get_name()] = contact
    def print_contact(self):
        for name, contact in self.contacts.items():
            print(f'Name: {contact.get_name()} Phone: {contact.get_phone()} Email: {contact.get_email()}')
contact_map = ContactMap()
while True:
    name = input("Enter name (or 'q' to quit)")
    if name == 'q':
        break
    phone = input('Enter the phone')
    email = input('Enter Email')
    contact = Contact(name, phone, email)
    contact_map.add_contact(contact)
contact_map.print_contact()
