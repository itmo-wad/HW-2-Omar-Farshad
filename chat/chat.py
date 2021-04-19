from flask import Flask, render_template,request
import re

app = Flask(__name__)



@app.route('/', methods=['Get','POST'])
def index():
      
      msg=''
 # user receive the message from the 'botmsg' and get the reply 'mymsg'     
      if request.method == 'POST':
          getdata = request.form.get("botmsg")
          msg = request.form.get("mymsg")
          
          user = 'Me : '+ getdata + '\n'
          
          msg = msg + user
		#answers from the Bot is from the dictionary, answers could be found under the automated messages
          keywords = {
              
              'Hello.\n  How are you ?':['.*hello.*','^hi$','.*good morning.*','.*good afternoon.*','.*good evening.*'],
			  'My name is omar.\n':['.*what is your name.*','.*name.*'],
              'I am fine.': ['.*how are you.*'],
			  'well, i dont know)': ['.*old.*','.*age.*','.*birth.*'],
              'you are welcome.':['.*pleasure is mine.*'],
              'bye':['.*bye.*']

           }
          # search in the dictionary and try to find a suitable answer by usinf reqular expressions
          found = 0
          bot = 'Bot: '
          for key,value in keywords.items():
              rr = re.compile('|'.join(value),re.IGNORECASE)
              if re.search(rr, getdata):
                  bot = bot + key + '\n'
                  found = 1
                  break
         #default msg  
          if found == 0 :
                 bot = bot+ 'Sorry, I did not understand(\n'
                 
          msg = msg + bot + '\n'         
                   
      return render_template('index.html',dialog=msg)
      

   
if __name__ == '__main__':

    app.run( port='50099',threaded=True)
