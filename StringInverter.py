def StringInverter(string):
    if string is None:
        return ''
    if len(string) == 0:
        return ''
    if len(string) == 1:
        return string
    return string[::-1]
'''
Your task is to implement a suite of tests in Pytest that will test all the possible behaviors of the invert function, as described above

Your suite of tests will be run against multiple (wrong and correct) 
implementations of invert function.

'''
# create tests for the invert function uing the pytest framework
def test_invert_single_character():
    assert StringInverter('a') == 'a'

def test_invert_empty_string():
    assert StringInverter('') == ''

def test_invert_none():
    assert StringInverter(None) == ''

def test_invert_single_character_with_space():
    assert StringInverter('a ') == 'a '

def test_invert_single_character_with_tab():
    assert StringInverter('a\t') == 'a\t'

def test_invert_single_character_with_newline():
    assert StringInverter('a\n') == 'a\n'

def test_invert_single_character_with_carriage_return():
    assert StringInverter('a\r') == 'a\r'






print(StringInverter("example"))
# How to connect from one container to another within the same Docker network?


# What is the purpose of using EXPOSE command in Dockerfile?
# EXPOSE command is used to expose a port on the host machine to the container.





