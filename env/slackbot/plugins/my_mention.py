# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import random

from libs import my_functions           # 外部関数の読み込み

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                              文字列中に':'はいらない
@respond_to('眠い')
def mention_func(message):
    message.reply('甘え') # メンション

@respond_to('できました')
def mention_func(message):
    message_list = ['ばかなの？','バリュー出た？','それのどこら辺にバリューあるか教えて貰ってもいい？','仕事してもらっていいすか？','ユーザビリティくそ悪くね？','あれまさかもう寝た？','あーそんなことしちゃうんだー次から3倍くらいロジカルにつめますね','(⋈◍＞◡＜◍)。✧','僕にできることがあったらなんでも言ってくださいね(⋈◍＞◡＜◍)。'] 
    message.reply(random.choice(message_list)) # メンション


@listen_to('辛い')
def listen_func(message):
    message.send('あーそんなことしちゃうんだー次から3倍くらいロジカルにつめますね')      # ただの投稿
    message.reply('甘え')                       # メンション

@listen_to('ねむすぎ')
def listen_func(message):
    message.reply('甘え')                       # メンション
