class Contact:
  def __init__(self, name, phone, mail):
    self.name = name
    self.phone = phone
    self.mail = mail

class ContactList:
  def __init__(self):
    self.contacts = []

  def add_contact(self, name, phone, mail):
    contact = Contact(name, phone, mail)
    self.contacts.append(contact)

  def delete_contact(self, name):
    for contact in self.contacts:
      if contact.name == name:
        self.contacts.remove(contact)
        print(f'Contact {name} is Deleted')
        break
    
  def search_contact(self, name):
    for contact in self.contacts:
      if contact.name == name:
        return contact.name + ": " + contact.phone +" : "+ contact.mail
    return name + " is not found."

contact_list = ContactList()
contact_list.add_contact("Ajay", "555-555-5555", "aaa@gmail.com")
contact_list.add_contact("Rahul", "444-444-4444", "bbb@gmail.com")
#print(contact_list.search_contact("Ajay"))
#print(contact_list.search_contact("Rahul"))
#print(contact_list.search_contact("Alice"))
contact_list.delete_contact("Rahul")
print(contact_list.search_contact("Rahul"))

