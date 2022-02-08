import jwt
from settings import TOKEN_SECRET_KEY


def encode_token(game_id, player_id):
    try:
        payload = {
            "game_id": game_id,
            "player_id": player_id
        }
        return jwt.encode(payload, TOKEN_SECRET_KEY, "HS256")
    except Exception as err:
        return err


def decode_token(token):
    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, "HS256")
        return payload
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")
