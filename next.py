from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)


def pw():
    import random
    pas2 = list('ABCDEFGHIGKLMNopqrstuvyxwz123456')
    pas3 = list('abcdefghigklmnOPQRSTUVYXWZ7890')
    random.shuffle(pas2)
    random.shuffle(pas3)
    passwd = 'WN_' + ''.join([random.choice(pas2) for x in range(11)] + [random.choice(pas3) for x in range(11)])
    return passwd


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    a = [pw() for x in range(85)]

    return render_template('index.html', a=a)


if __name__ == "__main__":
    app.run(host='0.0.0.0')