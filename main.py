txt = 'This is Latin letters and numbers 123'
n_txt = txt[:34]
b = n_txt.lower()
c = n_txt.strip()
vowels = 0
consonants = 0
print(txt)
for i in b and c:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' \
            or i == 'u' or i == 'y' or i == 'а' or i == 'е' \
            or i == 'і' or i == 'о' or i == 'и' or i == 'у'\
            or i == 'A' or i == 'E' or i == 'I' or i == 'O'\
            or i == 'U' or i == 'Y' or i == 'А' or i == 'Е'\
            or i == 'І' or i == 'О' or i == 'И' or i == 'У':
        vowels = vowels + 1
    elif i != ' ':
        consonants = consonants + 1
print('Кількість голосних букв:', vowels)
print('Кількість приголосних букв:', consonants)
if vowels >> consonants:
    print('Голосних більше у цьому тексті.')
else:
    print('Приголосних більше у цьому тексті.')