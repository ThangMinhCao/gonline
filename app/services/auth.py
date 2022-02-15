import jwt
from settings import TOKEN_SECRET_KEY


def encode_token(room_id, player_id):
    """
    Encode a token with given IDs.

    :param room_id -> str: Id of the game room
    :param player_id -> str: Id of the new player
    """
    try:
        payload = {
            "room_id": room_id,
            "player_id": player_id
        }
        return jwt.encode(payload, TOKEN_SECRET_KEY, "HS256")
    except Exception as err:
        return err


def decode_token(token):
    """
    Decode the token to get room and player IDs.

    :param token -> str: The authentication token
    """
    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, "HS256")
        return payload
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")
