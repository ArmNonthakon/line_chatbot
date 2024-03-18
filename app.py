from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        payload = request.json
        reply_token = payload["events"][0]["replyToken"]
        print(reply_token)
        message = payload["events"][0]["message"]["text"]
        print(message)
        line_access_token = "insert_channel_access_token"
        
        if message == "text":
            reply_message = "Return Text"
            replyMessage(reply_token, reply_message, line_access_token)
            return request.json, 200
        elif message == "button":
            reply_message = "Return Button"
            replyButton(reply_token, reply_message, line_access_token)
            return request.json, 200
        elif message == "Carousel":
            reply_message = "Return Carousel"
            replyCarousel(reply_token, reply_message, line_access_token)
            return request.json, 200
        elif message == "quickReply":
            text_message = "Select an option:"
            quick_reply_items = [
                {
                    "type": "action",
                    "action": {
                        "type": "cameraRoll",
                        "label": "Send photo"
                    }
                },
                {
                    "type": "action",
                    "action": {
                        "type": "camera",
                        "label": "Open camera"
                    }
                }
            ]
            replyQuickReply(reply_token, text_message, quick_reply_items, line_access_token)
            return request.json, 200
    else:
        abort(400)

def replyMessage(reply_token, text_message, line_access_token):
    LINE_API = "https://api.line.me/v2/bot/message/reply"
    authorization = "Bearer {}".format(line_access_token)
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": authorization,
    }
    data = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text_message}],
    }
    r = requests.post(LINE_API, headers=headers, json=data)
    return r.json(), r.status_code

def replyButton(reply_token, text_message, line_access_token):
    LINE_API = "https://api.line.me/v2/bot/message/reply"
    authorization = "Bearer {}".format(line_access_token)
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": authorization,
    }
    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "template",
                "altText": "This is a buttons template",
                "template": {
                    "type": "buttons",
                    "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "Menu",
                    "text": "Please select",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/123",
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=123",
                        },
                        {
                            "type": "postback",
                            "label": "Add to cart",
                            "data": "action=add&itemid=123",
                        },
                        {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/123",
                        },
                    ],
                },
            }
        ],
    }
    r = requests.post(LINE_API, headers=headers, json=data)
    return r.json(), r.status_code

def replyCarousel(reply_token, text_message, line_access_token):
    LINE_API = "https://api.line.me/v2/bot/message/reply"
    authorization = "Bearer {}".format(line_access_token)
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": authorization,
    }
    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                            "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
                            "imageBackgroundColor": "#FFFFFF",
                            "title": "this is menu",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "http://example.com/page/123",
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Buy",
                                    "data": "action=buy&itemid=111",
                                },
                                {
                                    "type": "postback",
                                    "label": "Add to cart",
                                    "data": "action=add&itemid=111",
                                },
                                {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "http://example.com/page/111",
                                },
                            ],
                        },
                        {
                            "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
                            "imageBackgroundColor": "#000000",
                            "title": "this is menu",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "http://example.com/page/222",
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Buy",
                                    "data": "action=buy&itemid=222",
                                },
                                {
                                    "type": "postback",
                                    "label": "Add to cart",
                                    "data": "action=add&itemid=222",
                                },
                                {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "http://example.com/page/222",
                                },
                            ],
                        },
                    ],
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover",
                },
            }
        ],
    }
    r = requests.post(LINE_API, headers=headers, json=data)
    return r.json(), r.status_code

def replyQuickReply(reply_token, text_message, quick_reply_items, line_access_token):
    LINE_API = "https://api.line.me/v2/bot/message/reply"
    authorization = "Bearer {}".format(line_access_token)
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": authorization,
    }
    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": text_message,
                "quickReply": {
                    "items": quick_reply_items
                }
            }
        ],
    }
    r = requests.post(LINE_API, headers=headers, json=data)
    return r.json(), r.status_code

if __name__ == "__main__":
    app.run(debug=True)
