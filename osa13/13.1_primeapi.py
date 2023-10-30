from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    for x in range(2,int(luku)):
        if x != luku:
            if luku % x == 0:
                return {
                    "number" : luku,
                    "isPrime" : False
                    }
    return {
        "number" : luku,
        "isPrime" : True
        }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)