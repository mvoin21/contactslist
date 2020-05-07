class ContactList(list):
    def __init__(self, contacts):
        self.contacts = contacts

    @property
    def search_by_name(self):
        find = input('Введте имя для поиска: ')
        find_contacts = []
        for item in self.contacts:
            if item == find:
                find_contacts.append(item)
        
        if find_contacts == []:
            print(f'Результат поиска: нет совпадений')
        else:        
            print(f'Результат поиска: {find_contacts}')

            
                
all_contacts = ContactList(['Ivan', 'Masha', 'Jenya'])

all_contacts.search_by_name