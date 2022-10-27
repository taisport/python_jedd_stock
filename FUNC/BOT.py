# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:32:14 2019

@author: taisport
"""

import requests
import telegram

proxies = {
   'http': 'http://wtwong:czmHa$6191$@10.35.236.13:8080',
   'https': 'http://wtwong:czmHa$6191$@10.35.236.13:8080',
}

def bot_private_sendtext(bot_message):
	
	### Send text message
	bot_token = '629634909:AAHH8VJq7FJm4lZQ1Qwm61tlUgXVteCLzzo'
	bot_chatID = '293583438'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
    
    
def bot_hkinvest_sendtext(bot_message):
	
	### Send text message
	bot_token = '645967483:AAEBtt615aZi8FbIIsiJSlLuqdPpeQV-NEs'
	bot_chatID = '293583438'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
   
   
def bot_waigorcomment_sendtext(bot_message):
	
	### Send text message
	bot_token = '736528014:AAGw-AhdEzyPQqDya8Mnmrpl5WZSIIsLMMw'
	bot_chatID = '-1001377563113'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
    
    
def bot_hkstockmeetingdividend_sendtext(bot_message):
	
	### Send text message
	bot_token = '757554985:AAFcbfo8HFWYDDzOrRBss0-pbD0y5dnIkyg'
	bot_chatID = '293583438'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
    
    
def bot_waigorpatcomment_sendtext(bot_message):
	
	### Send text message
	bot_token = '736528014:AAGw-AhdEzyPQqDya8Mnmrpl5WZSIIsLMMw'
	bot_chatID = '-1001497602419'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
    
    
def bot_bearcow_photo(PHOTO_PATH):
	
	### 港股牛熊BOT + 牛熊指數軍團 Send Photo
	bot_token = '5390486474:AAHVMi23OieQBno8RHmSID2Ws0JHsmGeGGM'
	bot_chatID = '-1001609540617'
	bot=telegram.Bot(token=bot_token)
	bot.send_photo(chat_id=bot_chatID,photo=open(PHOTO_PATH,'rb'))


def bot_bearcow_msg(bot_message):
	
	### 港股牛熊BOT + 牛熊指數軍團 Send Msg
	bot_token = '5390486474:AAHVMi23OieQBno8RHmSID2Ws0JHsmGeGGM'
	bot_chatID = '-1001609540617'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	#requests.get(send_text)
    

def bot_test_msg(bot_message):
	
	bot_token = '1084524723:AAEYEeQmhLJsrq94bGImprA8tFxK8QOUQVE'
	bot_chatID = '-824545705'
	#send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	#requests.get(send_text,  proxies = proxies)

	proxy = telegram.utils.request.Request(proxy_url=proxies)
	bot = telegram.Bot(token=bot_token, request=proxy);
	bot.send_message(chat_id=bot_chatID, text='USP-Python has started up!')