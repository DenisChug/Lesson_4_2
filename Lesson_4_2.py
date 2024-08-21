def test_function():
    def inner_function():
        return print('Я в области видимости функции test_function')
    inner_function()


test_function()
inner_function() #Не определено имя функции, т.к. она находиться внутри функции test_function():
# Как вариант, если необходимо вызывать данную функцию в другом месте, это вынести ее из функции test_function()

#def inner_function():
#    return print('Я в области видимости функции test_function')

#def test_function():
#    inner_function()

#inner_function()