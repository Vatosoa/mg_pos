import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def get_custom_pos_tag(word, tag, custom_pos_tags):
    if word in custom_pos_tags:
        return custom_pos_tags[word]
    return 'Tsy fantatra'

def pos_tag_sentence(sentence, custom_pos_tags):
    words = word_tokenize(sentence.lower())
    tagged_words = pos_tag(words)
    pos_tags_result = [(word, get_custom_pos_tag(word, tag, custom_pos_tags)) for word, tag in tagged_words]
    return pos_tags_result


def tokenizer(sentence):
    mots = nltk.word_tokenize(sentence)
    return mots
