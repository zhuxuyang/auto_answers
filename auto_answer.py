import math
import jieba
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer


data = pd.read_csv("answer/answer.csv")

count_vec = CountVectorizer()


def get_word_List(question):
    sentence_seg = jieba.cut(question, cut_all=True, HMM=False)
    return " ".join(sentence_seg)


def count_cos_similarity(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return 0

    s = sum(vec_1[i] * vec_2[i] for i in range(len(vec_2)))
    den1 = math.sqrt(sum([pow(number, 2) for number in vec_1]))
    den2 = math.sqrt(sum([pow(number, 2) for number in vec_2]))

    b = (den1 * den2)
    if b == 0:
        return 0
    else:
        return s / b


def cos_sim(sentence1, sentence2):
    sentences = [sentence1, sentence2]
    v1 = count_vec.fit_transform(sentences).toarray()[0]
    v2 = count_vec.fit_transform(sentences).toarray()[1]
    r = count_cos_similarity(v1, v2)
    return r


def get_answer(user_question):
    result = {}
    for i in data.index:
        a = get_word_List(data["question"][i])
        b = get_word_List(user_question)
        if len(a) == 0 or len(b) == 0:
            continue
        score = cos_sim(a, b)
        result[i] = score
    s = sorted(result.items(), key=lambda d: d[1], reverse=True)
    return s


def get_data():
    return data

# while 1:
#     print("输入问题")
#     question = stdin.readline()
#     answer_dict = get_answer(question.strip())
#     print(answer_dict)
#     for index, value in answer_dict:
#
#         if index < 3:
#             print(answer_dict[index])
#             print(data["question"][answer_dict[index][0]])
#             print(data["answer"][answer_dict[index][0]])
#             print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     answer_dict = {}
