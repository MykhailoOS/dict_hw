# Task1

# txt_dict = {}
# text = input("text= ")
#
# txt_dict[text.count(text)] = text
# print(txt_dict)

#Task2
translations = {
    'hi': 'привіт',
    'book': 'книга',
    'house': 'дім',
    'car': 'машина'
}
word = input("= ")
if word not in translations:
    print("В словнику немає такого слова")
else:

    get_translate = translations.get(word)
    print(get_translate)