import re

def translate(word_or_phrase):
  word_list = word_or_phrase.split(" ")
  for i in range(len(word_list)):
    temp = word_list[i]
    if re.search("[aeiou]", temp[0]):
      temp += 'ay'
    else:
      vowelIndex = re.search("[aeio]", temp).start()
      if re.search("[!,.?;:]", temp):
        temp = temp[vowelIndex:len(temp)-1]+temp[0:vowelIndex]+'ay'+temp[len(temp)-1]
      else:
        temp = temp[vowelIndex:]+temp[0:vowelIndex]+'ay'
      if re.search("[A-Z]", word_list[i][0]):
        temp = temp[0].upper()+temp[1:].lower()
    word_list[i] = temp
  return " ".join(word_list)