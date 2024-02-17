from faker import Faker

class LoginData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.user_name = str("JoannaJachowicz")
        self.password = str("TestyPython2024!")
        self.fake_password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

