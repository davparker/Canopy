def countVowels(s):
    string = s
    vowels = 'aeiou'
    count = 0
    i = 0
    while i < len(string):
        if string[i].lower() in vowels:
            count += 1
            print('vowel: ' + string[i])
        i += 1
    return count