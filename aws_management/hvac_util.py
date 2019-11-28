import hvac
import json

client=hvac.Client(url="http://127.0.0.1:8200")
print("Is authentication succeded :",client.is_authenticated())

read_secrets=client.secrets.kv.read_secret_version(path="aws")["data"]["data"]
access_key=read_secrets["access_key"]
access_secret=read_secrets["access_secret"] 