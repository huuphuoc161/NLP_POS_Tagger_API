from flask import Flask, jsonify, request
from underthesea import pos_tag
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    sentence = request.args.get('sentence')
    print(sentence, 'sentence')
    result = pos_tag(sentence)
    data = []
    for x in result:
        word, tag = x
        if tag == 'CH':
            tag = word
        data.append([word, tag])

    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False)
