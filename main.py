while True:
    stroka = input('Введите строку: ')
    stroka1 = stroka.split()
    poisk = input('Введите образец поиска: ')

    for word in stroka1:
        word = list(word)
        a = word[-len(poisk):]
        b = ''.join(a)
        c = ''.join(word)
        if b == poisk:
            print(c)
