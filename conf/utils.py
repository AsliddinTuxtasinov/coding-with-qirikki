import hashlib

USERS = {"asil-bro": "2e68f4bea90cf8a5659e3c07a621b90ddfe67e17cf4a0673bc7dd6f38cda3e54"}


def check_password(hash_password: str, password: str) -> bool:
    password = hashlib.sha256(password.encode()).hexdigest()
    if hash_password == password:
        return True
    return False
