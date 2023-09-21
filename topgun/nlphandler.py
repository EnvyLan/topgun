
from copy import copy

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def workflow_map():
    return [
        {
            "words": "Calculate total amount invoices",
            "workflow_name": "logic app1",
            "threshold": 0.52
        },
        {
            "words": "check company name match",
            "workflow_name": "logic app2",
            "threshold": 0.52
        },
        {
            "words": "check company number match",
            "workflow_name": "logic app3",
            "threshold": 0.52
        }
    ]


def find_top1(words):
    scope = 0
    workflow = None
    emb = model.encode(words)
    for x in workflow_map():
        _scope = util.cos_sim(emb, model.encode(x.get("words")))
        if _scope.storage().tolist()[0] <= x.get("threshold"):
            continue
        if _scope > scope:
            scope = _scope
            workflow = copy(x)
    if workflow is None:
        raise Exception("can not found any match workflow")

    return workflow, scope


def handler_words(words):
    s1 = word_tokenize(words)
    print(s1)
    s2 = [x for x in s1 if x not in set(stopwords.words("english"))]
    print(s2)

    print(nltk.pos_tag(s2))
    for x in s2:
        print(wordnet.synsets(x)[0].lemmas())


if __name__ == '__main__':
    mywords = "Calculate for me the total amount of these invoices"

    # hanlder_words(mywords)

    sentences = ["Calculate for me the total amount of these invoices"]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    emb1 = model.encode("Calculate total amount invoices")
    emb2 = model.encode("help me to Calculate total amount of these invoices")
    emb3 = model.encode("please help me to calculate the total for this cost receipt charges")
    emb4 = model.encode("help me figure out the total cost for this bill")
    print(util.cos_sim(emb1, emb2))
    print(util.cos_sim(emb1, emb3))
    print(util.cos_sim(emb1, emb4))

    emb4 = model.encode("help me to check company name does match")
    emb5 = model.encode("help me to check company number does match")
    print("name & number")
    b = util.cos_sim(emb5, emb4)

    handler_words("hanlder_words(help me to check company name does match")
    # hanlder_words("help me verify does company name right")
