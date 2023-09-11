import os

os.system('clear')

substituicoes = {
    'q': '/',
    'w': ',',
    'e': '.',
    'r': 'h',
    't': 'x',
    'y': 'w',
    'u': 'l',
    'i': 't',
    'o': 'c',
    'p': 'p',
    'a': 'i',
    's': 'e',
    'd': 'a',
    'f': 'o',
    'g': 'u',
    'h': 'm',
    'j': 'd',
    'k': 's',
    'l': 'r',
    'ç': 'n',
    'z': 'y',
    'x': ';',
    'c': 'j',
    'v': 'b',
    'b': 'k',
    'n': 'q',
    'm': 'v',
    'nothing': '@'
}

Resubstituicoes = {
    '/': 'q',
    ',': 'w',
    '.': 'e',
    'h': 'r',
    'x': 't',
    'w': 'y',
    'l': 'u',
    't': 'i',
    'c': 'o',
    'p': 'p',
    'i': 'a',
    'e': 's',
    'a': 'd',
    'o': 'f',
    'u': 'g',
    'm': 'h',
    'd': 'j',
    's': 'k',
    'r': 'l',
    'n': 'ç',
    'y': 'z',
    ';': 'x',
    'j': 'c',
    'b': 'v',
    'k': 'b',
    'q': 'n',
    'v': 'm',
    '#': ' ',
    '@': ' ',
    'nothing': '-'
}

print('1 - Convert \n2 - Text')
op = int(input('Digite a opção desejada: '))

if op == 1:

    def convert(i, table):
        outputText = []
        for caracter in i:
            if caracter == ' ':
                outputText.append(table['nothing'])
            else:
                outputText.append(table.get(caracter, caracter))
            os.system('clear')
                
        return '#'.join(outputText)



    textClear = input('Digite o texto: ')

    textList = list(textClear)

    outputText = convert(textList, substituicoes)

    print(outputText)

elif op == 2:

    def Reconvert(i, table):
        textNormal = []
    
        for caracter in i:
            if caracter == ' ':
                textNormal.append(table['nothing'])
            else:
                textNormal.append(table.get(caracter, caracter))
            
            os.system('clear')

        return ''.join(textNormal)

    textInput = input('Cole o texto a ser descriptografado: ')

    textSepa = list(textInput)

    for x in textSepa.copy():
        if x == '#':
            textSepa.remove(x)

    textNormal = Reconvert(textSepa, Resubstituicoes)
    print(textNormal)
