# Rewrite this in Unit Test

from pig_latin import translate

print(f"translates a word beginning with a vowel: {translate('apple') == 'appleay'}")
print(f"translates a word beginning with a consonant: {translate('banana') == 'ananabay'}")
print(f"translates a word beginning with two consonants: {translate('cherry') == 'errychay'}")
print(f"translates two words: {translate('eat pie') == 'eatay iepay'}")
print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
print(f"translates many words: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")
print(f"Asserts that capitalized words are still capitalized and punctuations stay in place: {translate('The quick, agile brown fox!') == 'Ethay ickquay, agileay ownbray oxfay!'}")