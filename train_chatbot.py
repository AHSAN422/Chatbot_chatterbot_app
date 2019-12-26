from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os
import glob


bot = ChatBot('Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ListTrainer')
files = glob.glob('./data/*.yml')
for file in files:
    convData = open(r'./' + file, encoding='latin-1').readlines()
    # First, lets train our bot with some data
    trainer = ListTrainer(bot)
    # for chatterbot corpus data plz uncomment line no 15
    # trainer = ChatterBotCorpusTrainer(bot)

    # train the data
    trainer.train(convData)
    # Now we can export the data to a file
    trainer.export_for_training('./my_export.json')


