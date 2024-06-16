def character_count(word):
    character_statistic = {}

    for character in word:
        if character in character_statistic:
            character_statistic[character] += 1
        else:
            character_statistic[character] = 1
    return character_statistic


print(character_count('smiles'))
print(character_count('Happiness'))
