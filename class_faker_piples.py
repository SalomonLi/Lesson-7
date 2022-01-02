import time
from faker import Faker


class BusinessCard:
    """Основной класс"""
    def __init__(self, first_name, last_name, company_name, job, email, phone, phone_business,*args, **kwargs):
       self.first_name = first_name
       self.last_name = last_name
       self.company_name = company_name
       self.job = job
       self.email = email
       self.phone = phone
       self.phone_business = phone_business
       # self._values = len((self.first_name + " " + self.last_name))



    @property
    def label_length(self):
        # lens = f'{self.first_name} {self.last_name}'
        # self._values = len(lens)
        length_first_last_name = len((self.first_name + " " + self.last_name))

        # print(contact)
        return length_first_last_name

    @lens.setter
    def contact(self):
        contact = f'Contact to "{self.first_name} {self.last_name} {self.email}"'
        pass
        # print(values)
        # contact = f'Contact to "{self.first_name} {self.last_name} {self.email}"'
        # print(contact)
        # return contact

class BaseContact(BusinessCard):
    """должен хранить основные контактные данные, такие как (имя, фамилия, телефон, адрес электронной почты)"""
    """first_name, last_name, phone, email"""
    def __init__(self, *args, **kwargs):
        super(BaseContact, self).__init__(*args, **kwargs)
        self.first_name = args.index('first_name')
        self.last_name = args.index('last_name')
        # self.phone = phone
        # self.email = email

    def contact(self):
        contact = f'Contact to "{self.first_name} {self.last_name} {self.phone}"'
        return contact

class BusinessContact(BusinessCard):
    """должен хранить информацию, связанной с работой человека - (должность, название компании, рабочий телефон)"""
    def __init__(self, job, company_name, phone_business):
        self.job = job
        self.company_name = company_name
        self.phone_business = phone_business

    def contact(self):
        contact = f'Contact to "{self.first_name} {self.last_name} {self.phone}"'
        return contact
    

    pass



def create_contacts():

    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company_name = fake.company()
    job = fake.job()
    email = fake.email()
    # addr = fake.street_address()
    # city = cities.get_random()
    phone = fake.random_number(digits=10)
    phone_business = fake.random_number(digits=7)

    # license = ''.join(random.choice('0123456789ABCDEF') for i in range(8))

    fake_agent = BusinessCard(first_name, last_name, company_name, job, email, phone, phone_business)
    return fake_agent



def generate_dict():
   resul = []
   for i in range(1, 100):
       fake_agent = create_contacts()
       resul.append({i: {"last_name": fake_agent.last_name, "first_name": fake_agent.first_name}})
       # print(f"First Name- {fake_agent.first_name}, Last Name- {fake_agent.last_name}, "
       #   f"Company- {fake_agent.company_name}, Job- {fake_agent.job}, Email- {fake_agent.email}")
   return resul


client_id_0 = create_contacts()
client_id_1 = create_contacts()
client_id_2 = create_contacts()
client_id_3 = create_contacts()
client_id_4 = create_contacts()
client_id_5 = create_contacts()



x=client_id_0.contact
print(x)

client_list = [client_id_0, client_id_1, client_id_2, client_id_3, client_id_4, client_id_5]

# print(client_list)
cliets_first_name_sorted = sorted(client_list, key=lambda client_id: client_id.first_name)
cliets_last_name_sorted = sorted(client_list, key=lambda client_id: client_id.last_name)
cliets_email_sorted = sorted(client_list, key=lambda client_id: client_id.email)
# print('',cliets_first_name_sorted, '\n', cliets_last_name_sorted, '\n', cliets_email_sorted)











