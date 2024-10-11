from faker import Faker

from data import Body


class Helpers:

    @staticmethod
    def mod_create_user_body():
        faker = Faker()
        body = Body.CREATE_USER_BODY.copy()
        body['email'] = faker.email()
        body['password'] = faker.password(6)
        body['name'] = faker.first_name()

        return body

    @staticmethod
    def fake_email():
        faker = Faker()
        email = faker.email()

        return email

    @staticmethod
    def fake_password():
        faker = Faker()
        password = faker.password()

        return password