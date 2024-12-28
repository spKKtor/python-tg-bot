print('Input N1:')
n1 = input()
print('Input N2:')
n2 = input()


try:
    # d = int(n1) / int(n2)
    d = n1 / n2
    print(d)
except ZeroDivisionError:
    print('Ділення на нуль')
except TypeError:
    print('Що за нерозумний програміст?')
    d = int(n1) / int(n2)
    print('Переведено в INT: ',d)
finally:
    print('Блок винятків завершенно')

print('Програма працює')