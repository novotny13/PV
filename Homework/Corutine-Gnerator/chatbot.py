def chatbot():
    yield "Ahoj jak se mas?"
    while True:
        odpoved = yield
        odpoved = odpoved.lower()
        if(odpoved =="konec"):
            yield "Loucim se"
            break
        elif(odpoved =="jak je"):
            yield "Mam se Dobre"
        else:
            yield "Nevim co tim myslis"



chat = chatbot()

print(next(chat))
next(chat)

print(chat.send("Jak je"))
next(chat)
print(chat.send("Pepa"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Jak je"))
next(chat)
print(chat.send("Konec"))

chat.close()