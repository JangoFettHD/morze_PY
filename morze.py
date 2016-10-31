morze = {'a': '.-', 'b': '-...', 'w': '.--', 'g': '--.', 'd': '-..', 'e': '.', 'v': '...-', 'z': '--..', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'x': '-..-', 'y': '-.--', 'p': '.--.',
         'r': '.-.', 's': '...',
         't': '-', 'u': '..-', 'f': '..-.', 'h': '....', 'c': '-.-.', 'q': '--.-'}


def translate(name):
    name = name.lower().replace('ь', '').replace('ъ', '')

    transtable = (
        (u"щ", u"sch"),
        (u"ё", u"yo"),
        (u"ж", u"zh"),
        (u"ц", u"ts"),
        (u"ч", u"ch"),
        (u"ш", u"sh"),
        (u"ы", u"yi"),
        (u"ю", u"yu"),
        (u"я", u"ya"),
        (u"а", u"a"),
        (u"б", u"b"),
        (u"в", u"v"),
        (u"г", u"g"),
        (u"д", u"d"),
        (u"е", u"e"),
        (u"з", u"z"),
        (u"и", u"i"),
        (u"й", u"j"),
        (u"к", u"k"),
        (u"л", u"l"),
        (u"м", u"m"),
        (u"н", u"n"),
        (u"о", u"o"),
        (u"п", u"p"),
        (u"р", u"r"),
        (u"с", u"s"),
        (u"т", u"t"),
        (u"у", u"u"),
        (u"ф", u"f"),
        (u"х", u"h"),
        (u"э", u"e"),
    )
    for symb_in, symb_out in transtable:
        name = name.replace(symb_in, symb_out)
    return name


def input_int(str="", err='\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m'):
    while True:
        inp = ""
        try:
            inp = int(input(str))
        except ValueError:
            print(err)
        if isinstance(inp, int):
            return inp


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


a = -1
while a != 0:
    a = input_int("Выберите: \n1) морзе -> текст\n2) текст -> морзе\n>>")

    if a == 1:
        inp = input("Введите морзе: ").split(" ")
        temp_string = ""
        for i in range(len(inp)):
            temp_string += str((get_key(morze, inp[i])))
        print(temp_string)
    if a == 2:
        inp1 = input("Введите слова: ")
        inp1 = translate(str(inp1)).split(" ")
        # print(inp1)
        temp_string1 = ""
        for i in range(len(inp1)):
            for l in range(len(inp1[i])):
                temp_string1 += morze[inp1[i][l]]
                temp_string1 += str(" ")
        temp_string1 = temp_string1[:-1]
        print(temp_string1)
