from faker import Faker


class BaseContact:
    """
     powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail
    """

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def contact_base(self):
        contact = f'Contact to "{self.first_name} {self.last_name} {self.phone}"'
        return contact

    def __len__(self):
        return len((self.first_name + " " + self.last_name))



class BusinessContact(BaseContact):
    """
    rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
    """

    def __init__(self, first_name, last_name, phone, email, job, company_name, phone_business):
        super().__init__(first_name, last_name, phone, email)
        self.company_name = company_name
        self.job = job
        self.phone_business = phone_business
        self.label_length = 0


    def contact_base(self):
        contact = f'Contact to "{self.first_name} {self.last_name} {self.phone_business}"'
        return contact

    def label_length_contact(self):
        length = len((self.first_name + " " + self.last_name))
        return length

    def __len__(self):
        return len((self.first_name + " " + self.last_name))

# base_contact = BaseContact('John', 'Doe', '123', 'john@doe.com', )
# BusinessContact = BusinessContact(
#     'John', 'Doe', '123', 'john@doe.com', 'CEO', 'ACME', '456'
# )


def create_contacts(card_type, count):
    contacts = []

    for _ in range(count):
        fake = Faker()

        first_name = fake.first_name()
        last_name = fake.last_name()
        company_name = fake.company()
        job = fake.job()
        email = fake.email()
        phone = fake.random_number(digits=10)
        phone_business = fake.random_number(digits=7)

        if card_type is BaseContact:
            fake_agent = BaseContact(first_name,last_name,phone,email)
        elif card_type is BusinessContact:
            fake_agent = BusinessContact(first_name,last_name, phone,email,job,company_name,phone_business)
        else:
            raise ValueError('...')

        contacts.append(fake_agent)

    return contacts

x = create_contacts(BaseContact,1)
y = create_contacts(BusinessContact,1)
print(x[0].__dict__)
print(x[0].contact_base())
print((x[0].__len__()))

print(y[0].__dict__)
print(y[0].contact_base())
print(y[0].__len__())