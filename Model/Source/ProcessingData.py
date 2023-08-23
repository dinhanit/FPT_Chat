from pyvi import ViTokenizer
import json
path = 'DataSet/train/'
data = path+'sents.txt'
# Open the JSON file for reading
with open('Dictionary/spell_correct_word.json', 'r') as file:
    spell_correct_word = json.load(file)
with open('Dictionary/translate_english.json', 'r') as file:
    translate_english = json.load(file)
with open('Dictionary/emoji.json', 'r') as file:
    emoji = json.load(file)
with open('Dictionary/translate_emoticons.json', 'r') as file:
    translate_emoticons = json.load(file)
with open('Dictionary/emoticon.json', 'r') as file:
    emoticon = json.load(file)

with open('Dictionary/stopword.txt','r',encoding='utf8') as file:
    StopWords = [line.strip() for line in file.readlines()]
with open('Dictionary/Dictionary_Vietnamese.txt','r',encoding='utf8') as file:
    MainDict = [line.strip() for line in file.readlines()]
with open('Dictionary/pro_noun.txt','r',encoding='utf8') as file:
    pro_noun = [line.strip() for line in file.readlines()]
with open(data,'r',encoding='utf8') as file:
    lines = [ViTokenizer.tokenize(line.strip()) for line in file.readlines()]

ProcessedData = []
for line in lines:
    result=''
    words = line.split(" ")
    for word in words:
        if (word in MainDict):
            if word not in StopWords:
                result+=word+' '
        else:
            if word not in pro_noun:
                if word in list(translate_english.keys()):
                    result += translate_english[word] + ' '
                elif word in list(translate_emoticons.keys()):
                    result += translate_emoticons[word] + ' '
                elif word in list(emoji.keys()):
                    result += emoji[word] + ' '
                elif word in list(emoticon.keys()):
                    result += emoticon[word] + ' '
                elif word in list(spell_correct_word.keys()):
                    result += spell_correct_word[word] + ' '
                else:
                    with open('wrongspell.txt','a',encoding='utf8') as f:
                        f.write(word+'\n')

    ProcessedData.append(result)

with open(path+"sentsPro.txt", "w", encoding='utf8') as file:
    for line in ProcessedData:
        file.write(str(line).replace('_',' ') + "\n")
