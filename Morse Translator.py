import subprocess

igang = 1
morseCodes = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "æ": ".-.-",
    "ø": "---.",
    "å": ".--.-",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

while igang == 1:
    print("Skriv venligst en sætning som kan oversættes til Morse kode.")
    print("Hvis du vil stoppe programmet, så skriv 'stop'")

    sentence = input("Skriv her: ")

    if sentence == "stop":
        igang = 0
        print("Programmet er stoppet")
        break
    else:
        sentence = sentence.lower()
        sentence = list(sentence)
        morseSentence = []
        for i in sentence:
            if i == " ":
                morseSentence.append(" ")
            else:
                morseSentence.append(morseCodes[i])
        morseSentence = " ".join(morseSentence)
        print(morseSentence)
