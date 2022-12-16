from abc import ABC, abstractmethod

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

class ContactMap(ABC):
    def __init__(self):
        self.contacts = {}
    @abstractmethod
    def save(self, contact_name):
       pass
class AddContact(ContactMap):        
    def save(self, contact):
        self.contacts[contact.get_name()] = contact
class DeleteContact(ContactMap):        
    def save(self, contact_name):
        if contact_name in self.contacts:
            del self.contacts[contact_name]
class FindContact(ContactMap):
    def save(self, contact_name):
        if contact_name in self.contacts:
            print(self.contacts[contact_name])


while True:
    name = input("Enter name (or 'q' to quit): ")
    if name == 'q':
        break
    phone = input('Enter the phone: ')
    email = input('Enter Email: ')
    contact = Contact(name, phone, email)
    addcontact = AddContact()
    addcontact.save(contact)
find_contact = FindContact()
find_contact.save(contact)

