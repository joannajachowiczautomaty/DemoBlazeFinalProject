from faker import Faker

class OrderData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.fake_name = fake.name()
        self.fake_credit_card_number = fake.credit_card_number()
