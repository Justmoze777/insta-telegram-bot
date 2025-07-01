from instagrapi import Client

USERNAME = "mynameispravin"
PASSWORD = "Mynameispravin"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
print("✅ session.json saved successfully.")
