from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[

        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "threshold": 0.60,
            "default_response": "I am sorry, but I do not understand."
        },
      'chatterbot.logic.MathematicalEvaluation',
      ###'chatterbot.logic.TimeLogicAdapter',
      ##"chatterbot.logic.BestMatch"
    ]
                  )

    ListTrainer(bot)
    while True:
        if usrText.strip()!= 'bye':
            result = bot.get_response(usrText)
            reply = str(result)
            return(reply)
        if usrText.strip() == 'bye':
            return('I am dying.......Bye... ')
            break


class ChatServer(WebSocket):

    def handleMessage(self):
        #get message reponse.
        message = self.data
        response = get_response(message)
        self.sendMessage(response)
        #status of the server connected
    def handleConnected(self):
        print(self.address, 'connected')
        # status of the server closed
    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
