from instagrapi import Client

USERNAME = "mynameispravinbhai"
PASSWORD = "Pass@121212"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
print("✅ session.json saved successfully.")
