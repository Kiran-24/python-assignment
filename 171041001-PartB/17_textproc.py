
def line_count(file):
    '''prints number of lines in a file'''
    file.seek(0,0)
    text = file.read()
    count = len(text.splitlines())
    print('number of lines is ',count)

def word_count(file):
    '''prints number of words in a file'''
    file.seek(0,0)
    text = file.read()
    count = len(text.split())
    print('number of words is ',count)
             
def character_count(file):
    '''prints number of characters
    (including space and newline) in a file'''
    file.seek(0,0)
    text = file.read()
    count = len(text)
    print('number of characters is ',count)

def main():
    try:
        input_file = open('input.txt','r')
        line_count(input_file)
        word_count(input_file)
        character_count(input_file)
        input_file.close()
    except IOError as e:
        print('I/O error: {0}'.format(e))      

if __name__ == '__main__':
    main()


