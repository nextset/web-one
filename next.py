from flask import Flask
app = Flask(__name__)

@app.route('/')
def pw():
    import random
    pas1 = list('1234567890')
    pas2 = list('ABCDEFGHIGKLMNOPQRSTUVYXWZ')
    pas3 = list('abcdefghigklmnopqrstuvyxwz')
    random.shuffle(pas1)
    random.shuffle(pas2)
    random.shuffle(pas3)
    passwd = ''.join([random.choice(pas1) for x in range(4)] + [random.choice(pas2) for x in range(1)] + [random.choice(pas3) for x
                                                                                             in range(1)])
    return passwd


if __name__ == "__main__":
    app.run(host="0.0.0.0")