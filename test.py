import spacy

nlp = spacy.load('en_core_web_sm')

input_sentence = "QQ is cutiest human in the world"
doc = nlp(input_sentence)

for token in doc:
    print(token.text, token.pos_)
    # print (type(token.pos_))