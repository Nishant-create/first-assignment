def test(n):
    return lambda x: x + n

string_joiner = test('bad')

string_joiner_1 = test('not so bad')

print(string_joiner('good'))
print(string_joiner('medium'))
print(string_joiner_1('good'))
print(string_joiner_1('medium'))

incrementor = test(50)

print(incrementor(1))
print(incrementor(5))