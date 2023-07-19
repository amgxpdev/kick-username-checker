import random
import string
import tls_client

def generate_random_username():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(4))

def make_request_and_save_valid(username):
    session = tls_client.Session(
        client_identifier="chrome112",
        random_tls_extension_order=True
    )

    url = "https://kick.com/api/v1/signup/verify/username"
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip",
        "accept-language": "de_DE",
        "connection": "Keep-Alive",
        "content-type": "application/json",
        "host": "kick.com",
        "user-agent": "okhttp/4.9.2",
        "x-kick-app-p-os": "android",
        "x-kick-app-p-v": "28",
        "x-kick-app-v": "1.0.43",
    }

    response = session.post(
        url,
        headers=headers,
        json={
            "username": username,
        },
    )

    if not response.text:
        with open("valid.txt", "a") as file:
            file.write(username + "\n")
        print(f"Valid username: {username}")
    else:
        print(f"Invalid username: {username}")

while True:
    random_username = generate_random_username()

    make_request_and_save_valid(random_username)
