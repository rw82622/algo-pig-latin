exports.translate = function (word) {
  let wordList = word.split(" ");
  for (let index in wordList) {
    temp = wordList[index];
    if (temp[0].match(/[aeiou]/i)) {
      temp += "ay";
    } else {
      let vowelIndex = temp.indexOf(temp.match(/[aeio]/i));
      if (temp.match(/[!,.?;:]/)) {
        temp =
          temp.slice(vowelIndex, temp.length - 1) +
          temp.slice(0, vowelIndex) +
          "ay" +
          temp.slice(temp.length - 1);
      } else {
        temp = temp.slice(vowelIndex) + temp.slice(0, vowelIndex) + "ay";
      }
      if (wordList[index][0].match(/[A-Z]/)) {
        temp = temp[0].toUpperCase() + temp.slice(1).toLowerCase();
      }
    }
    wordList[index] = temp;
  }
  return wordList.join(" ");
};
