from chatterbot import ChatBot
from flask import Flask,make_response
from flask_restful import Resource, Api
import json
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot(
    'Jovin',
    logic_adapters=[
        {
            'import_path': 'ApiLogic.ApiLogic'
        },
        {
            'import_path': 'CMDLogic.CMDLogic'
        }
    ],
)

app = Flask(__name__)
api = Api(app)

# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train(
#     "chatterbot.corpus.english.greetings"
# )


class ChatRes(Resource):
    def get(self,query):
        res = chatbot.get_response(query)
        return {'chatRes': str(res)}

api.add_resource(ChatRes, '/ChatRes/<query>')

if __name__ == '__main__':
    app.run(debug=True,port='5002')


# while True:
#     try:
#         str=input("The source of all answer... Ask Jovin\n")
#         response = chatbot.get_response(str)
#         print(response)
#
#     except(KeyboardInterrupt,EOFError,SystemExit):
#         break