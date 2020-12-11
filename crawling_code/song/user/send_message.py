
import requests
import json

def send_msg(webhook, dj, channel='#dss', username='DJ'):
    dj = str(dj[['Artist', 'Title', 'Genre']].values)
    payload = {"channel": channel, "username": username, "text": dj}
    requests.post(webhook, data=json.dumps(payload))
