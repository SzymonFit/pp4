def addText(text):
    with open ("tekst.txt", "a") as file:
        file.write("\n" + text)


addText("Hello World!")