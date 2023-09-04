# Author: Jacob Dawson

#!pip install googletrans==4.0.0-rc1
from googletrans import Translator
#from googletrans import LANGCODES
from translationData import *

translator = Translator()

def compareTranslations(language, inputTranslation, comparisonTranslation):
    autoTranslated = [
        translator.translate(m, src="en", dest=language).text.lower()
        for m in inputTranslation
    ]
    numSame = 0
    i = 0
    for a in autoTranslated:
        # translates the phrase word-for-word back into english (costly)
        """retranslatedSentence = " ".join(
            [
                translator.translate(word, src=language, dest="en").text.lower()
                for word in a.split()
            ]
        )"""

        # translates the sentence directly back into english (changing
        # grammar to match ours)
        retranslatedSentence = translator.translate(a, src=language, dest="en").text.lower()

        #print(retranslatedSentence)

        if retranslatedSentence == comparisonTranslation[i]:
            numSame += 1
        i += 1

    #print("numSame:", numSame)
    return numSame

for langCode in possibleLanguages:
    num = compareTranslations(langCode, manuallyTranslated, original)
    print(langCode, 'has this many matches with original:', num)
