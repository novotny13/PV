import random
def upper(text):
    return text.upper()
def smily(text):
    return text.replace(' ', ';)')
def switch_v(text):
    return text.replace('v', 'w').replace('V', 'W')
def append_astrics(text):
    return "*"+str(text)+"*"
def replace_one_with_many(text):
    return text.replace('?', '???').replace('!', '!!!!!')

funky_functions = (upper, smily, switch_v, append_astrics, replace_one_with_many)

def funky_format(text):
    for _ in range(3):
        funkcion = funky_functions[random.randint(0,len(funky_functions)-1)]
        text = funkcion(text)

    return text
print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))