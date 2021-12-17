import time
from faker import Faker

fake = Faker()

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"times = {dt}")
        return res

    return wrapper


@test_time
def get_nod(a , b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

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
# def test_users(n=50):
#     fake = Faker(locale='de_DE')
#     fake.seed(42)
#
#     users = []
#     for i in xrange(n):
#         u = User()
#         u.first_name = fake.first_name()
#         u.last_name = fake.last_name()
#         u.email_address = fake.email()
#         u.password = u.original_password = fake.password()
#         u.tracking_key = fake.random_number(digits=6)
#
#         users.append(u)
#
#     return users

def valueset(self, nbvalues):
    """
    Generate the values
    """
    values = []

    f = Faker()
    for i in range(1,2):
        values.append({"company": f.company(),
                       "name": f.name()[:300],
                       "street_address": f.street_address()[:300],
                       "email": "{}".format( f.email()),
                       "value": f.random_number(),
                       "vali": f.random_number(),
                       "country": f.country()[:100],
                       "latitude": f.latitude(),
                       "longitude": f.longitude(),
                       "city": f.city()[:50],
                       "city_suffix": f.city_suffix()[:20],
                       "locale": f.locale()[:8],
                       })

    return values
@test_time
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

fake_agent = generate()
fake_agent2 = generate()

for i in range(1, 100):
    fake_agent = generate()
    print(f"First Name- {fake_agent.first_name}, Last Name- {fake_agent.last_name}, "
      f"Company- {fake_agent.company_name}, Job- {fake_agent.job}, Email- {fake_agent.email}")
