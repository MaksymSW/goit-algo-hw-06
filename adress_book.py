"""
У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий набір полів.
Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо їх взаємозв'язок, правила,
за якими вони будуть взаємодіяти.

Користувач взаємодіє з книгою контактів, додаючи, видаляючи та редагуючи записи.
Також користувач повинен мати можливість шукати в книзі контактів записи за одним або кількома критеріями (полями).

Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад).
Також записи можуть містити декілька полів одного типу (декілька телефонів наприклад). Користувач повинен мати
можливість додавати/видаляти/редагувати поля у будь-якому записі.


Технічне завдання
Розробіть систему для управління адресною книгою.

Сутності:
    Field: Базовий клас для полів запису.
    Name: Клас для зберігання імені контакту. Обов'язкове поле.
    Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    AddressBook: Клас для зберігання та управління записами.

Функціональність:
    AddressBook:Додавання записів.
    Пошук записів за іменем.
    Видалення записів за іменем.
    Record:Додавання телефонів.
    Видалення телефонів.
    Редагування телефонів.
    Пошук телефону.
"""

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if len(value)==10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("The phone number must be a string and consist of 10 digits")          

		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self,phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
        
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()




# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
