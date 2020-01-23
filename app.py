from flask import Flask, request

from auto_answer import get_data

from auto_answer import get_answer

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '欢迎试用人工智障问答系统'


@app.route('/recommend_answers')
def recommend_answers():
    question = request.args.get('question')
    print(question)
    answer_dict = get_answer(question.strip())
    result = {}
    for index, value in answer_dict:
        if index < 3:
            print(answer_dict[index])
            q = get_data()["question"][answer_dict[index][0]]
            s = get_data()["answer"][answer_dict[index][0]]
            result[q] = s
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
