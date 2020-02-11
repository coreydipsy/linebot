from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Wst7uV8PMkV9Ve0u2s72kCMX7LtDkj8OZJ04jWzgnc6yMJsWyDCtldAzuQpOqLsaaXJDwei1xqUixmglhxhyD+wzI6ToiadI5dCBgs4XiIMZBGyxjVdYerac6QDQUmG/pPn5Ulqllp+wABoYJ7US7QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2bf2c6185ba6947098f004f0d02edf06')



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()