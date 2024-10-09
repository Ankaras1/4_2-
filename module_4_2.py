def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() #Ничего не выводит
inner_function() #Не работает
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function() #Выводит, если inner_function вызывается в себе

