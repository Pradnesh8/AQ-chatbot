import csv
try:
    from chatterbot import ChatBot
except:
    pass
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request,render_template

app = Flask(__name__)


def getCustomTrainData():
    with open('educhatbot-data - Sheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        train_data=[]
        for row in csv_reader:
            if line_count != 0:
                train_data.append(row[0])
                train_data.append(row[1])
            line_count += 1
    return train_data
def chatBotresp(ip):
    chatbot=ChatBot('Bot',
                database_uri='sqlite:///database.db',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.90
                    }
                ]
                )
    return(chatbot.get_response(ip))



@app.route("/")
def ind():
    return render_template("home.html")

@app.route("/resp/<msg>")
def resp(msg):
    output=str(chatBotresp(msg))
    return output
    #print(output,type(output))
    #return "hi"




if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
#train_data=getCustomTrainData()
#trainer1 = ListTrainer(chatbot)
#trainer1.train(train_data)
#trainer2 = ChatterBotCorpusTrainer(chatbot)
#trainer2.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations")
#print(chatbot.get_response('what is intake for computer engineering?'))
#print(chatbot.get_response('what is name of college?'))

#
#database_uri='sqlite:///database.db'
#confidence
#logic_adapters=[
#        'chatterbot.logic.MathematicalEvaluation',
#        'chatterbot.logic.TimeLogicAdapter'
#    ]
#logic_adapters=[
#        {
#            'chatterbot.logic.MathematicalEvaluation',
#            'chatterbot.logic.TimeLogicAdapter',
#            'import_path': 'chatterbot.logic.BestMatch',
#            'default_response': 'I am sorry, but I do not understand.',
#            'maximum_similarity_threshold': 0.50
#        }
#    ]
#trainer.train(
#    "chatterbot.corpus.english.greetings",
#    "chatterbot.corpus.english.conversations"
#)

##trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train(
#    "chatterbot.corpus.english"
#)
