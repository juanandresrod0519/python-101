import argparse

def main():
    args = get_args()
    word = args.word
    print("Hello-Basic")
    print(word)
    #1
    my_dogs = 2
    print(type(my_dogs))
    my_dogs = ["dog-1","dog-2"]
    print(type(my_dogs))
    my_dogs = 30.1
    print(type(my_dogs))
    #2
    word = 'narwhal'
    print(word[0])  #--> 'n'
    print('narwhal'[0]) #--> 'n'
    print(word[6]) # --> 'l'
    print(word[-1]) # --> 'l'
    #3 [start:stop]
    print(word[:3]) #--> 'nar'
    print(word[3:]) #--> 'whal'
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    print(alphabet[2:])
    print(alphabet[:4])
    print(alphabet[3:6])
    print(alphabet[::3])
    print(alphabet[2:7:2])
    #4
    print(word.upper())
    print(word.isupper())
    print(word.upper().isupper())
    print(len('narwhal'))
    #5
    char = word[0].lower()
    print(char)
    print(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')
    #6
    print('a' in 'aeiou')
    print('k' in 'aeiou')
    print("hello \nworld \tJA")
    #7 
    #String inmutability
    name = "Juan Andres"
    #name[0] = "p" ----> error
    name = "j" + name[1:]
    print(name)
    letter = 'A'
    print(letter * 23)

    s="Hello World"
    print(s.upper())
    words = s.split(' ')
    print(words)

    #String formatting
    print('Hola {} {}!'.format('Juan','Andres'))
    print('Hola {r} {f}!'.format(f='Felipe',r='Rod'))
    res = 100/777
    print('R:{}'.format(res))
    print('R:{r:1.3f}'.format(r=res))
    print('R:{r:10.3f}'.format(r=res))
    name = "Juan Andres"
    print(f'Hello {name}')

    print("Hello python")




def get_args():
    parser = argparse.ArgumentParser(description="Juan Andres",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word')
    return parser.parse_args()

if __name__ == '__main__':
    main()


# word = 'narwhal'
# word[0]  --> 'n'
# 'narwhal'[0] --> 'n'
# word[6] --> 'l'
# word[-1] --> 'l'
# [start:stop] 
# word[:3] --> 'nar'
# word[3:] --> 'whal'
# word.upper()
# word.isupper() --> F
# word.upper().isupper() --> T
# len('narwhal') --> 7

# word = 'octopus'
# char = word[0] --> 'o'

# type(char) --> <class 'str'>

# char == 'a' --> F
# char == 'o' --> T
# word = "hola" --> nothing ; word == "hola" --> T or F

# word = 'OCTOPUS'
# char = word[0]
# char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' --> F
# char = word[0].lower()
# char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' --> F

# 'a' in 'aeiou' --> T;  'b' in 'aeiou' --> F

#article = ''
#if word[0].lower() in 'aeiou':
#article = 'an'
#else:
#article = 'a'

#'Ahoy, Captain, {} {} off the larboard bow!'.format(article, word)
#f'Ahoy, Captain, {article} {word} off the larboard bow!'

#Positional:parser.add_argument('word', metavar='word', help='Word')

#word[0] in 'aeiouAEIOU'