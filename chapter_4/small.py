from flask import Flask, redirect, request

app = Flask('basic app')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('https://www.google.com/search?q=%s' % request.args['q'])
    else:
        return '<h1>GET REQUST FROM FLASK!</h1>'


