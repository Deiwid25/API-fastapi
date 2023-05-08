from jwt import encode


def create_token(data: dict):
    token: str = encode(payLoad=data, ket="my-secret_key",algorithm="HS256")
    return token