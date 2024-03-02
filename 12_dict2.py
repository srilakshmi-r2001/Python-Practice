fav_lang=dict()
for i in range(0,4):
    name=input("Enter your name:\n")
    lang=input("Enter your mother tongue:\n")
    fav_lang.update({name:lang})
print(fav_lang)