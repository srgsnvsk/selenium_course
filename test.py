import faker

f = faker.Faker()

email = f.email()
password = f.password()
print(email, password)
