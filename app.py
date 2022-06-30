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
    #投票による更新
    global kinoko_count, takenoko_count, messages
    if request.form.get('item')=='kinoko':
        kinoko_count+=1
    elif request.form.get('item')=='takenoko':
        takenoko_count+=1

    #メッセージの追加
    #python内のカウンタの更新
    messages.append(request.form.get('message'))
    if len(messages)>3:
        messages.pop(0)

    #vote.html内に渡す内容をつくる
    message_html=''
    for i in range(len(messages)):
        c='alert-warning ms-5' if i%2==0 else 'alert-success me-5'
        m=messages[i]
        message_html+=f'<div class="alert{c}" role="alert">{m}</div>\n'
        
    #進捗グラフの更新
    kinoko_percent=kinoko_count/(kinoko_count+takenoko_count)*100
    takenoko_percent=takenoko_count/(kinoko_count+takenoko_count)*100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
