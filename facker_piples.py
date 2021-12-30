import time
from faker import Faker



def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"times = {dt}")
        return res

    return wrapper
# @test_time
# def get_nod(a , b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# @test_time
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#     return a

# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)
# res2 = get_fast_nod(26765, 1000000)
# res = get_nod(654643, 10000007574575)
# if res > res2:
#     print(True)
# else:
#     print(False)
# print(res, res2)
class Night_Club:

    def __init__(self, first_name, last_name, company_name, job, email):
       self.first_name = first_name
       self.last_name = last_name
       self.company_name = company_name
       self.job = job
       self.email = email
       # self._values = len((self.first_name + " " + self.last_name))



    @property
    def lens(self):
        # lens = f'{self.first_name} {self.last_name}'
        # self._values = len(lens)
        x = len((self.first_name + " " + self.last_name))
        contact = f'Contact to "{self.first_name} {self.last_name} {self.email}"'
        # print(contact)
        return x

    @lens.setter
    def contact(self):
        pass
        # print(values)
        # contact = f'Contact to "{self.first_name} {self.last_name} {self.email}"'
        # print(contact)
        # return contact




def generate():
   fake = Faker()

   first_name = fake.first_name()
   last_name = fake.last_name()
   company_name = fake.company()
   job = fake.job()
   email = fake.email()
   # addr = fake.street_address()
   # city = cities.get_random()
   # phone = fake.random_number(digits=10)
   # license = ''.join(random.choice('0123456789ABCDEF') for i in range(8))

   night_club = Night_Club(first_name, last_name, company_name, job, email)
   return night_club


@test_time
def generate_dict():
   resul = []
   for i in range(1, 100):
       fake_agent = generate()
       resul.append({i: {"last_name": fake_agent.last_name, "first_name": fake_agent.first_name}})
       # print(f"First Name- {fake_agent.first_name}, Last Name- {fake_agent.last_name}, "
       #   f"Company- {fake_agent.company_name}, Job- {fake_agent.job}, Email- {fake_agent.email}")
   return resul


client_id_0 = generate()
client_id_1 = generate()
client_id_2 = generate()
client_id_3 = generate()
client_id_4 = generate()
client_id_5 = generate()


print(type(client_id_0.contact))
x=client_id_0.contact
print(x)

client_list = [client_id_0, client_id_1, client_id_2, client_id_3, client_id_4, client_id_5]

# print(client_list)
cliets_first_name_sorted = sorted(client_list, key=lambda client_id: client_id.first_name)
cliets_last_name_sorted = sorted(client_list, key=lambda client_id: client_id.last_name)
cliets_email_sorted = sorted(client_list, key=lambda client_id: client_id.email)
# print('',cliets_first_name_sorted, '\n', cliets_last_name_sorted, '\n', cliets_email_sorted)


# print(len(client_id_0))

# # Using @property decorator
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value...")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("Temperature below -273 is not possible")
#         self._temperature = value
#
#
# # create an object
# human = Celsius(37)
#
# print(human.temperature)
#
# print(human.to_fahrenheit())
#
# coldest_thing = Celsius(-300)