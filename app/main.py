from flask import Flask
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/api_3/<inp>')
def api_3(inp):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(inp)
    return("{:-<40} {}".format(inp, str(score)))
    #return inp
    #return inp

if __name__ == '__main__':
  app.run()