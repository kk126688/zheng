from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['result'][0]['content']['from']
    text = decoded['result'][0]['content']['text']
    #print(json_line)
    print("使用者：",user)
    print("內容：",text)
    sendText(user,text)
    return ''

def sendText(user, text):
    LINE_API = 'https://trialbot-api.line.me/v1/events'
    CHANNEL_ID = '1573206486'
    CHANNEL_SERECT = '9913183f839ee9909aee3c3921d11ccf'
    MID = 'TE/KJSG1XwWP7gg8E0Mm00Eex5SHc+YsBvgqt8dpG8DxvW5d2ysQ7ves/3YQ1/ZemFQBpaPwlUverSqSODfjUJWuGPi2PZbVPvnjmcRtgh9NFMs9uJW21kK2/Zi5w2vKkb3pWi5Ec2Nl79rNIcNEegdB04t89/1O/w1cDnyilFU='

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': '1573206486',
        'X-Line-ChannelSecret': '9913183f839ee9909aee3c3921d11ccf',
        'X-Line-Trusted-User-With-ACL': 'TE/KJSG1XwWP7gg8E0Mm00Eex5SHc+YsBvgqt8dpG8DxvW5d2ysQ7ves/3YQ1/ZemFQBpaPwlUverSqSODfjUJWuGPi2PZbVPvnjmcRtgh9NFMs9uJW21kK2/Zi5w2vKkb3pWi5Ec2Nl79rNIcNEegdB04t89/1O/w1cDnyilFU='
    }

    data = json.dumps({
        "to": [user],
        "toChannel":1383378250,
        "eventType":"138311608800106203",
        "content":{
            "contentType":1,
            "toType":1,
            "text":text
        }
    })

    #print("送出資料：",data)
    r = requests.post(LINE_API, headers=headers, data=data)
    #print(r.text)

if __name__ == '__main__':
     app.run(debug=True)