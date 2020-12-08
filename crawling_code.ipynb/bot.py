import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from flask import request
from flask import Response

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ["SIGNING_SECRET"],'/slack/events', app)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)

@app.route("/music1", methods=["POST"])
def music1():
    user_id = request.form.get("user_id")
    channel_id = request.form.get("channel_id")
    client.chat_postMessage(channel=channel_id, text="멜론 플레이리스트 번호를 입력해주세요.")
    
    text = request.form.get("text")
    # seq = text
    
    
    
    
    return Response(), 200


if __name__ == "__main__":
    app.run(debug=True)