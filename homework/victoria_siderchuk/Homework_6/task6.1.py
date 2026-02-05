text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

text = text.replace(',', ' ,')
text = text.replace('.', ' .')

words = text.split()
words_ing = []

for word in words:
    if word == ',':
        words_ing.append(word)
    elif word == '.':
        words_ing.append(word)
    else:
        words_ing.append(word + 'ing')

my_text = ' '.join(words_ing)
my_text = my_text.replace(' ,', ',')
my_text = my_text.replace(' .', '.')

print(my_text)
