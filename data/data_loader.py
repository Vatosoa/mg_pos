import pandas as pd

def load_custom_pos_tags_from_file(file_path):
    data = pd.read_excel(file_path)
    #data = pd.read_csv(file_path)
    custom_pos_tags = {}
    for index, row in data.iterrows():
        tag = row['Tag']
        words = row['Words']
        if isinstance(words, str):
            word_list = words.split(',')
            for word in word_list:
                word = word.strip()
                custom_pos_tags[word] = tag
    return custom_pos_tags


# if you work in ubuntu, the path is like this
file_path = '/complete/path/to/your/project/data/custom_pos_tags.xlsx'
#file_path = '/complete/path/to/your/project/data/custom_pos_tags.csv'
custom_pos_tags = load_custom_pos_tags_from_file(file_path)