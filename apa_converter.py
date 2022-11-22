#This is just a dumb program I made because I'm tired of de-capitalizing the titles of articles for school formatting.

import pyperclip

'----------------------------------------------------------------------------------------------------------'

def alreadyCopied(): #This function will copy what is already in your clipboard.
    phrase = pyperclip.paste()
    apa_phrase = phrase.capitalize()
    pyperclip.copy(apa_phrase)
    print('I have copied the article to your clipboard')
    exit()

def needToCopy(): #This function allows the user to manually paste text in for formatting
    phrase = input('Please paste in what you want formatted: ')
    apa_phrase = phrase.capitalize()
    pyperclip.copy(apa_phrase)
    print('I have copied the article to your clipboard')
    exit()

def main(): #This program only exists to help me insert my article heads into my essays for formatting
    is_copy = input('Is the text you want to format copied to your clipboard now?(y/n): ')
    if is_copy == 'y':
        alreadyCopied()
    elif is_copy == 'n':
        needToCopy()
    else:
        print('Error 404: Please relaunch program and try again. Beep boop.')
        main()

main()