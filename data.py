class Url:

    BASE_URL = "https://stellarburgers.nomoreparties.site"
    LOGIN_URL = f"{BASE_URL}/login"
    REGISTER_URL = f"{BASE_URL}/register"
    USER_PROFILE_URL = f"{BASE_URL}/account/profile"
    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
    ORDER_FEED_URL = f"{BASE_URL}/feed"


class Body:

    CREATE_USER_BODY = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
    }


class Endpoint:

    CREATE_USER_ENDPOINT = '/api/auth/register'
    DELETE_USER_ENDPOINT = '/api/auth/user'