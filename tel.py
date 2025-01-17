# -*- coding: utf-8 -*-
"""Telegram - bot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AjeEBMfnOTXGTJ7Zibu0zzVrP2R1mmdW
"""

TelegramBOT_TOKEN = '7868443675:AAFqWjFgk2KbR0P4nHwsf6en6Y_urqHp3Oo'

#Latest version Gemini API
import telebot
import os


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyB56p_5paUJyFyPvHdwXTlqFEEcoJpg0oA")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


bot = telebot.TeleBot(TelegramBOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Powerful BOT, Ask your questions")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
 try :
  print(message)
  response=chat_session.send_message(message.text)
  bot.reply_to(message, response.text)

 except Exception as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, "Sorry, I couldn't process your request.")

bot.polling()
