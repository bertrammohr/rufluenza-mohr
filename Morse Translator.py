import subprocess

igang = 1

while igang == 1:
    print ("Skriv venligst en sætning som kan oversættes til Morse kode.")
    output = []
    tekst = input("-->")
    tekst = tekst.lower()
    tekstLength = len(tekst)
    for i in range (0, tekstLength):
        if tekst[i] == "a":
            output.append(".-")
        elif tekst[i] == "b":
            output.append("-...")
        elif tekst[i] == "c":
            output.append("-.-.")
        elif tekst[i] == "d":
            output.append("-..")
        elif tekst[i] == "e":
            output.append(".")
        elif tekst[i] == "f":
            output.append("..-.")
        elif tekst[i] == "g":
            output.append("--.")
        elif tekst[i] == "h":
            output.append("....")
        elif tekst[i] == "i":
            output.append("..")
        elif tekst[i] == "j":
            output.append(".---")
        elif tekst[i] == "k":
            output.append("-.-")
        elif tekst[i] == "l":
            output.append(".-..")
        elif tekst[i] == "m":
            output.append("--")
        elif tekst[i] == "n":
            output.append("-.")
        elif tekst[i] == "o":
            output.append("---")
        elif tekst[i] == "p":
            output.append(".--.")
        elif tekst[i] == "q":
            output.append("--.-")
        elif tekst[i] == "r":
            output.append(".-.")
        elif tekst[i] == "s":
            output.append("...")
        elif tekst[i] == "t":
            output.append("-")
        elif tekst[i] == "u":
            output.append("..-")
        elif tekst[i] == "v":
            output.append("...-")
        elif tekst[i] == "w":
            output.append(".--")
        elif tekst[i] == "x":
            output.append("-..-")
        elif tekst[i] == "y":
            output.append("-.--")
        elif tekst[i] == "z":
            output.append("--..")
        elif tekst[i] == "0":
            output.append("-----")
        elif tekst[i] == "1":
            output.append(".----")
        elif tekst[i] == "2":
            output.append("..---")
        elif tekst[i] == "3":
            output.append("...--")
        elif tekst[i] == "4":
            output.append("....-")
        elif tekst[i] == "5":
            output.append(".....")
        elif tekst[i] == "6":
            output.append("-....")
        elif tekst[i] == "7":
            output.append("--...")
        elif tekst[i] == "8":
            output.append("---..")
        elif tekst[i] == "9":
            output.append("----.")
        elif tekst[i] == " ":
            output.append(" ")
        else:
            output.append(tekst[i])
    print(*output)
    txt = *output
    subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)
    print("Copied to clipboard")
    slutter = 1
    while slutter == 1:
        slut = input("1. Vil du forsætte? Eller 2. Vil du stoppe? ")
        if slut == "1":
            slutter = 0
        elif slut == "2":
            slutter = 0
            igang = 0
