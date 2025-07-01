from instagrapi import Client

USERNAME = "mynameispravinbhai"
PASSWORD = "Mynameispravin@122"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
print("✅ session.json saved successfully.")
