def solve(phrases: list):
    result = [] # список палиндромов    
    for phrase in phrases: # пройдите циклом по всем фразам
        phrase_without_spaces = phrase.replace(' ', '') # сохраните фразу без пробелов
        if phrase_without_spaces == phrase_without_spaces[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result