from flask import Flask, render_template, request
app = Flask(__name__)

kinoko_count=3
takenoko_count=5
messages=['Hi1','Hi2']
@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    #進捗グラフの更新
    kinoko_percent=kinoko_count/(kinoko_count+takenoko_count)*100
    takenoko_percent=takenoko_count/(kinoko_count+takenoko_count)*100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
