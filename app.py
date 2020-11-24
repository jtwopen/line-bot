#如何註冊Line機器人
#google搜尋 line messaging api
#登入之後Start using Messaging API
#按加號輸入provider
#寫python檔(SDK) software development kit
#搜尋 python line sdk
#pip install line-bot.sdk
#複製usage貼上subline
#複製貼上Api跟Webhook
#註冊heroku
#下載安裝 CLI
#Creat New app



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

line_bot_api = LineBotApi('Gy8s1VWqN2Kn8vGQhpulA83BRE+VIRPSyeeR28IBsS3eUjdJXZz46eUuK4muJrcakMJmRVXNmC82jgOFt5jaWkZbZK5KVMEOHGQkdYa/mbhrNVe+5grgO20fP7fvL6pWPyjLnNI9P0hQpwQoUyeSmwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dcdadc7384fa0aca8381440fcd35da6e')


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
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎'))


if __name__ == "__main__":
    app.run()