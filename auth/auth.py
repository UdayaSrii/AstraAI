import hashlib


USERS = {

    "demo@gmail.com":
    hashlib.sha256(
        "password123".encode()
    ).hexdigest()

}



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def login(
        email,
        password
):

    if email in USERS:

        return (
            USERS[email]
            ==
            hash_password(password)
        )


    return False