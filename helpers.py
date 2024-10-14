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
    def mod_create_order_body():
        body = Body.CREATE_ORDER_BODY.copy()
        response = BurgersApi.get_ingredients().json()
        ingredients_list = []
        for ingredient in response['data']:
            ingredients_list.append(ingredient['_id'])
        random_ingredients = random.choices(ingredients_list, k=2)
        body["ingredients"] = random_ingredients

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