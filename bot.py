# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:39:36 2019

@author: Alla
"""

import telebot
import os
token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хелоооу!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if  (("нагад".lower() in  message.text.lower()) or ("напом".lower() in  message.text.lower()) or ("кину".lower()in  message.text.lower()) or ("кинь".lower()in  message.text.lower()) or ("кине".lower()in  message.text.lower()) or ("кида".lower() in  message.text.lower())
        or ("катьол".lower() in  message.text.lower()) 
        or ("котла".lower() in  message.text.lower()) 
        or ("котлу".lower() in  message.text.lower()) 
        or ("котел".lower() in  message.text.lower()) 
        or ("кател".lower() in  message.text.lower())
        or ("денис".lower() in  message.text.lower()) 
        or ("іванович".lower() in  message.text.lower()) 
        or ("котел".lower() in  message.text.lower()) 
        or ("кател".lower() in  message.text.lower())):
        bot.send_sticker(message.chat.id, 'CAADAgADMQADVQmNF3RfEYyhQu2FFgQ')
        if ( ("войтко".lower() in message.text.lower()) or  ("вв".lower() in  message.text.lower()) ):
            bot.send_sticker(message.chat.id, 'CAADAgADMAADrYBuEhAuCdx1v9JmFgQ') 
            if (("сапр".lower() in message.text.lower()) or ("романюк".lower()  in message.text.lower())):
                bot.send_sticker(message.chat.id, 'CAADAgADPgADVQmNF0FgXFWbTbaZFgQ')
        elif (("сапр".lower() in message.text.lower()) or ("романюк".lower()  in message.text.lower())):
            bot.send_sticker(message.chat.id, 'CAADAgADPgADVQmNF0FgXFWbTbaZFgQ')
    elif (("войтко".lower() in message.text.lower()) or  ("вв".lower() in  message.text.lower())):
        bot.send_sticker(message.chat.id, 'CAADAgADMAADrYBuEhAuCdx1v9JmFgQ') 
        if (("сапр".lower() in message.text.lower()) or ("романюк".lower()  in message.text.lower())):
            bot.send_sticker(message.chat.id, 'CAADAgADPgADVQmNF0FgXFWbTbaZFgQ')
    elif (("сапр".lower() in message.text.lower()) or ("романюк".lower()  in message.text.lower())):
        bot.send_sticker(message.chat.id, 'CAADAgADPgADVQmNF0FgXFWbTbaZFgQ')
        
bot.polling()