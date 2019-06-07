#!/usr/bin/env python
# -*- coding: utf-8 -*-
#um abraço pro tio Naufel
import time
import telepot
#Reference: http://unicode.org/emoji/charts/full-emoji-list$
falante = u'🔊'
naufalante = falante+falante+falante
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'recebi isso: %s' % command 
    print 'do chat: %s' % chat_id
    
    if command == naufalante:
        bot.sendSticker(chat_id, 'CAADAQADJwEAAiSbWAa1_wzLlUwZdwI')
    elif command == 'aaaa':
        bot.sendMessage(chat_id, 'aaaaaaaaaaaaaaaaaaaaaaaa')

bot = telepot.Bot('TOKEN')

MessageLoop(bot, handle).run_as_thread()
print 'aaaaaaaaaaaaaAAAAAAAAAAA'

while 1:
    time.sleep(10)
