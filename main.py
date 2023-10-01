# Task1

txt_dict = {}
text = input("text= ")

txt_dict[text.count(text)] = text
print(txt_dict)

# Task2
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

# Task3



contact_list = {}
while True:
    main_menu = input("\n\nПривіт!Це програма для збереження контактів."
                      "Вибери дію:\nadd - додати новий контак,\n"
                      "show - переглянути створені контакти,\n"
                      "del - видалити контакт;\n"
                      "exit - вихід\n"
                      ">>> ")

    if main_menu.lower() == "add":
        new_contact = input("ім'я =")
        new_tel_num = input("num =")
        contact_list[new_contact] = new_tel_num


    elif main_menu.lower() == "show":
        for key, value in contact_list.items():
            print(key, value)



    elif main_menu.lower() == "del":
        del_name = input("напишіть ім'я контакта який буде видаленим... ")
        del contact_list[del_name]

    elif main_menu == "exit":
        print("Goodbye!")
        break

    else:
        print("Error111")
#
cash = {
    "dollar_price": 0.02735,
    "euro_price": 0.02586,
    "zloty_price": 0.11962
}
qst = input("Це конвертер валют!Вибери дію:\nd - долар, e - євро, z - польскі злоти")
if qst.lower() == "d":
    print("Поточний курс",cash.get("dollar_price"))
    dollar = cash.get("dollar_price")
    grn_for_dollar = int(input("Напишіть вашу суму в грн> "))
    grn_to_dollar = grn_for_dollar * dollar
    print(grn_to_dollar)

elif qst.lower() == "z":
    print("Поточний курс", cash.get("zloty_price"))
    zloty = cash.get("zloty_price")
    grn_for_zloty = int(input("Напишіть вашу суму в грн> "))
    grn_to_zloty = grn_for_zloty * zloty
    print(grn_to_zloty)

elif qst.lower() == "e":
    print("Поточний курс", cash.get("euro_price"))
    euro = cash.get("euro_price")
    grn_for_euro = int(input("Напишіть вашу суму в грн> "))
    grn_to_euro = grn_for_euro * euro
    print(grn_to_euro)

else:
    print("Error444")

