# This script all made by Asa [ http://asaxyz.herokuapp.com ]
# Thats mean you can't modified or remove the Copyright 2k20
# This just for learn
# So please respect me by not removing Myname

"""BISSMILLAHIRRAHMANIRRAHIM"""
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json, pafy , pytz , humanize , time
from humanfriendly import format_timespan, format_size, format_number, format_length
from datetime import datetime, timedelta
from time import sleep
import errno
import os
from flex import flexTemplate
import sys, random, requests
import tempfile
import urllib, urllib3, urllib.parse, codecs
from urllib.parse import quote
from bs4 import BeautifulSoup
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)
app = Flask(__name__)
line_bot_api = LineBotApi('A9uKhm5nRYsvPjw3eY4XSrD4ot5iDkYwyqxMNuBS214JslXDVNfM3W4X6tISFGqsDm0Op6NqXEMQP4CKPJp8VmRb5j3C6hA1/un8dlsYEjn23EXzCjEkL+uKDJlJzSLPrfMhZde88eBgjyikhXwV0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a4c434cc1cb774e0184c1f561ba5e427')
flex = flexTemplate()
botStart = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
with open('by.json', 'r') as fp:
    wait = json.load(fp)
ugh = {
    "midLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "tokenLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "certLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "groupId": "111",
    "senderByMid": "111",
    "senderByGroup": "111"
}
#===================[ LINKE STARTO ]=====================	
@app.route('/')
def helo():
    return 'Hello This Is App Official Account Line For Bots By Asa Xyz Idline: guaksa :D'
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:handler.handle(body, signature)
    except InvalidSignatureError:abort(400)
    return 'OK'
@handler.add(PostbackEvent)
def handle_postback(event):
	if event.postback.data == 'ping':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text='Pong'))
	elif event.postback.data == 'datetime_postback':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
	elif event.postback.data == 'date_postback':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text=event.postback.params['date']))
@handler.add(JoinEvent)
def handle_join(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Joined this {}'.format(event.source.type)))
@handler.add(LeaveEvent)
def handle_leave():
	app.logger.info("Got leave event")
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Leave this {}'.format(event.source.type)))
@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Member join this {}'.format(event.source.type)))
	#line_bot_api.reply_message(
		#event.reply_token,
		#TextSendMessage(text='Joined this {} {}'.format(event.source.type,event.source.room_id)))
@handler.add(MemberLeftEvent)
def handle_member_left(event):
	app.logger.info("Got memberLeft event")
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Leaves this {}'.format(event.source.type)))
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	"""
	text message 
	"""
	text = event.message.text.lower()

	"""
	sender ID
	"""
	sender = event.source.user_id

	"""
	Group ID
	"""
	gid = event.source.sender_id
	
	"""
	BOT
	"""
	line = line_bot_api
#===============================================================================[ ARSYBAI FUNC ]
	def getProfile(sender):
		profile = line_bot_api.get_profile(sender).display_name
		"""
		argument:
		- display_name
		- status_message
		"""
		return profile

	def restartBot():
		print ("[ INFO ] BOT RESTART")
		python = sys.executable
		os.execl(python, python, *sys.argv)

	def failOverAPI():
		try:
			result = requests.get("https://api.boteater.xyz",timeout=0.5)
			if result.status_code == 200:
				return "https://api.boteater.xyz"
			else:
				return "https://api.boteater.us"
		except:
			return "https://api.boteater.us"

	def sendMessage(tx):
		"""
		easy sending a message
		param :
		- text/message (str)
		"""
		ggg = TextSendMessage(text=tx)
		return(line_bot_api.reply_message(event.reply_token,ggg))

	def sendMessageSender(tx):
		"""
		easy sending a message to Sender
		param :
		- text/message (str)
		"""
		line_bot_api.push_message(sender, TextSendMessage(text=tx))

	def sendMessageGroup(tx):
		"""
		easy sending a message to Group
		param :
		- text/message (str)
		"""
		line_bot_api.push_message(gid, TextSendMessage(text=tx))

	def sendMessageGroupV2(tx):
		"""
		easy sending a message to Group
		param :
		- text/message (str)
		"""
		gid2 = "{}".format(ugh["groupId"])
		line_bot_api.push_message(gid2, TextSendMessage(text=tx))

	def sendAudio(audio):
		"""
		Sending a audio
		param :
		- audio URL (mp3/m4a)
		"""
		message = AudioSendMessage(original_content_url=audio,duration=240000)
		line_bot_api.reply_message(event.reply_token, message)

	def sendVideo(thumb, video):
		"""
		Sending a Video
		param :
		- Video URL (must url)
		- Thumbnail URL (image url)
		"""
		message = VideoSendMessage(original_content_url=thumb,preview_image_url=video)
		line_bot_api.reply_message(event.reply_token, message)

	def sendMessageV2(lst):
		"""
		Send Message more than one
		param :
		- Message List
		"""
		return(line_bot_api.reply_message(event.reply_token,lst))

	def carouselMapping(contents):
		"""
		DO NOT CHANGE THIS MADAFAKA!
		"""
		this = {"type": "carousel","contents": contents}
		return this

	def sendFlex(alt, contents):
		"""
		SEND A FLEX MESSAGE
		param :
		- list flex message (max 10)

		this will automatically send with carousel :3
		"""
		message = FlexSendMessage(alt_text="{}".format(str(alt)), contents=carouselMapping(contents))
		line.reply_message(event.reply_token,message)

	def sendImage(url):
		"""
		Sending a Image
		param :
		- Image URL (must url)
		"""
		message = ImageSendMessage(original_content_url='{}'.format(str(url)),preview_image_url='{}'.format(str(url)))
		line_bot_api.reply_message(event.reply_token, message)
		
	def quickItem(label, tx):
		qi = QuickReplyButton(action=MessageAction(label=label, text=tx))
		return qi
	def sendMessageWithQuickReply(tx,items):
		message = TextSendMessage(text=tx,quick_reply=QuickReply(items=items))
		line_bot_api.reply_message(event.reply_token, message)
#===============================================================================[ STARTO ]
	if text == 'quickReply':
		"""
		This is for send Text message with quick reply
		"""
		items = [quickItem('Hello','Hello')]
		sendMessageWithQuickReply('hi',items)
	
	if text == 'huy':
		"""
		this is example if u just want to send a text message
		"""
		sendMessage('Wayaaeee~')

        if text == 'key':
                sendMessage('''Keyword BARRYZTA:
1. Cara Kerja
2. Pricelist
3. Format orderan
4. Payment
5. Own & admin
6. Pendapatan / upah
7. Rekor''')

	if text == 'byes':
		sendMessage('See u next time~\n{}'.format(event.source.group_id))
		line_bot_api.leave_group(event.source.group_id)

	if text == 'quota':
		quota = line_bot_api.get_message_quota()
		line_bot_api.reply_message(
			event.reply_token, [TextSendMessage(text='type: ' + quota.type),TextSendMessage(text='value: ' + str(quota.value))])

	if text == 'test':
		line_bot_api.multicast(
		[event.source.user_id], [
		TextSendMessage(text='THIS IS A MULTICAST MESSAGE'),])

	if text.lower().startswith('pc '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		line_bot_api.multicast([event.source.user_id],
		[TextSendMessage(text='{}'.format(q)),])

	if text == 'myid' or text == 'id' or text == 'userid':
		sendMessage('This Your UserID:\n{}'.format(event.source.user_id))

	if text.lower().startswith('bc '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		line_bot_api.broadcast([TextSendMessage(text='{}'.format(q)),])

	elif text == 'pict':
		sendImage("https://i.postimg.cc/nzRRpFMd/LOGO-z-Asa-BOT.jpg")

	elif text == 'carousel':
		carousel_template = CarouselTemplate(columns=[
			CarouselColumn(text='hoge1', title='fuga1', actions=[
				URIAction(label='Go to line.me', uri='https://line.me'),
				PostbackAction(label='ping', data='ping')
			]),
			CarouselColumn(text='hoge2', title='fuga2', actions=[
				PostbackAction(label='ping with text', data='ping', text='ping'),
				MessageAction(label='Translate Rice', text='米')
			]),
		])
		template_message = TemplateSendMessage(
			alt_text='Carousel alt text', template=carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)

	elif text == 'reply token':
		sendMessage("{}".format(event.reply_token))

	elif text == 'carousel img':
		image_carousel_template = ImageCarouselTemplate(columns=[
			ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
				action=DatetimePickerAction(label='datetime',
					data='datetime_postback',
					mode='datetime')),
			ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
				action=DatetimePickerAction(label='date',
					data='date_postback',
					mode='date'))
		])
		template_message = TemplateSendMessage(
			alt_text='ImageCarousel alt text', template=image_carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)

	elif text == 'token':
		link_token_response = line_bot_api.issue_link_token(event.source.user_id)
		line_bot_api.reply_message(
			event.reply_token, [
				TextSendMessage(text='link_token: ' + link_token_response.link_token)
			]
		)

	if text == 'me':
		name = line_bot_api.get_profile(sender).display_name
		status = line_bot_api.get_profile(sender).status_message
		pict = line_bot_api.get_profile(sender).picture_url
		anu = sender
		ret_ = "╭─「 This You 」"
		ret_ += "\n├ DisplayName : {}".format(name)
		ret_ += "\n├ StatusMessage : {}".format(status)
		ret_ += "\n├ UserID : {}".format(anu)
		ret_ += "\n├ PictURL : {}".format(pict)
		ret_ += "\n╰─「 Test 」"
		sendImage(pict)
		sendMessageGroup(ret_)

	if text.lower().startswith('exec'):
		try:
			sep = text.split("\n")
			cond = text.replace(sep[0] + "\n","")
			exec(cond)
		except Exception as error:
			sendMessage(error)

	if text == 'gc':
		gid = '{}'.format(event.source.group_id)
		anu = sender
		gcc = line_bot_api.get_group_member_profile(gid, anu)
		print(gcc)
		line_bot_api.push_message(gid, TextSendMessage(text='Hello World!'))
		line_bot_api.push_message(sender, TextSendMessage(text='Hello World!'))
		line_bot_api.push_message(gid, TextSendMessage(text='Hello World!'))

	if text == 'uy':
		sendMessageSender("Uy")
		sendMessageGroup("Uy2")

	if text == 'gcc':
		gid = '{}'.format(event.source.group_id)
		anu = sender
		gcc = line_bot_api.get_group_member_ids(gid)
		print(gcc.member_ids)

	if text == 'restart':
		sendMessage("Success reboot...")
		restartBot()

	if text == 'runtime':
		timeNow = time.time()
		runtime = timeNow - botStart
		runtime = format_timespan(runtime)
		sendMessage("「 Runtime 」\n"+str(runtime))

	if text == 'quotes twitch':
		r = requests.get("https://api.haipbis.xyz/randomtwitchquotes")
		data = r.text
		data = json.loads(data)
		qts1 = "{}".format(data["quotes"])
		strm = "{}".format(data["streamer"])
		r2 = requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(qts1))
		data = r2.text
		data2 = json.loads(data)
		qts2 = "{}".format(data2["result"]["translated"])
		ret_ = "╭─「 Quotes Twitch 」"
		ret_ += "\n├ Quotes EN : {}".format(qts1)
		ret_ += "\n├ Quotes ID : {}".format(qts2)
		ret_ += "\n├ Streamer : {}".format(strm)
		ret_ += "\n╰─「 Test 」"
		sendMessage(ret_)

	if text.lower().startswith('zodiaks '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		r = requests.get("https://api.fckveza.com/zodiak?query={}&apikey=AsaTZZK".format(str(q)))
		data=r.text
		data=json.loads(data)
		hasil = "╭─「 Zodiak 」"
		hasil += "\n├ Zodiak : "+str(data["result"][0]["zodiak"])
		hasil += "\n├ Ramalan Asmara : " +str(data["result"][0]["ramalan"]["asmara"])
		hasil += "\n├ Ramalan Kehidupan : " +str(data["result"][0]["ramalan"]["hidup"])
		hasil += "\n├ Ramalan Keuangan : " +str(data["result"][0]["ramalan"]["keuangan"])
		hasil += "\n├ Nomor Keberuntungan : " +str(data["result"][0]["ramalan"]["nomorKeberuntungan"])
		hasil += "\n╰─「 Test 」"
		sendMessage(hasil)

	if text.lower().startswith('ig '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		r = requests.get("https://asaxyz.herokuapp.com/instagram?username={}".format(str(q)))
		data=r.text
		data=json.loads(data)
		user = data["result"]["username"]
		name = data["result"]["fullname"]
		bio = data["result"]["bio"]
		bio2 = data["result"]["bio_link"]
		followers = data["result"]["followers"]
		following = data["result"]["following"]
		post = data["result"]["post"]
		private = data["result"]["private"]
		pict = data["result"]["profile_img"]
		message = [{
  "type": "bubble",
  "size": "kilo",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "{}".format(pict),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Profile",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ]
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [],
                "size": "xl",
                "wrap": True,
                "text": "{}".format(name),
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "User : {}".format(user),
                    "margin": "lg",
                    "size": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Bio : {}".format(bio),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Bio Link : {}".format(bio2),
                    "color": "#ffffffde",
                    "size": "md",
                    "margin": "md",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "Bio",
                      "uri": "{}".format(bio2)
                    }
                  },
                  {
                    "type": "text",
                    "text": "Followrs : {}".format(followers),
                    "size": "md",
                    "margin": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Following : {}".format(following),
                    "size": "md",
                    "margin": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Post : {}".format(post),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Private : {}".format(private),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  }
                ],
                "borderColor": "#ffffff",
                "borderWidth": "4px"
              }
            ],
            "paddingAll": "13px",
            "backgroundColor": "#ffffff1A",
            "cornerRadius": "2px",
            "margin": "xl"
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": "#464F69",
    "borderColor": "#000000",
    "borderWidth": "5px",
    "cornerRadius": "sm"
  }
}]
		sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)

	if text == 'heyy':
		"""
		this is example if you want to send more than one message
		"""
		message1 = TextSendMessage(text='Halo babang')
		message2 = TextSendMessage(text='Ngape lo?')
		#and more (Max 5)
		sendMessageV2([message1,message2])

	if text == 'flex':
		"""
		This is example for send a flex message
		( template in flex.py file )
		"""
		message = [flex.contoh()] #use []
		sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)

	if text == 'carouselk':
		"""
		This is example for send a flex message carousel
		( template in flex.py file )
		"""
		message = [flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh()]
		#just add more template :3 (Max 10)
		sendFlex(alt='THIS IS CAROUSEL MESSAGE', content=message)

#===============================================================================[ END ]
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""ALHAMDULILLAH"""
