# Author: Jacob Dawson

#!pip install googletrans==4.0.0-rc1
from googletrans import Translator, LANGCODES

translator = Translator()

# two corpi to translate to/from, the original song:
original = [
    "Alert, alert!",
    "DJ Crazy Times" "If you want parties to be making",
    "Have some noise",
    "Bratislava!",
    "All the women in the world",
    "Let me see your beautiful faces",
    "Oh, I've got an idea",
    "World peace!",
    "When the pleasure is a dream on a secret love",
    "And the people wanna make a fun",
    "We are losing control on a floor tonight",
    "Take your heart into a unicorn",
    "If the sky is not green, but the sky is blue",
    "Have a passion in a million way",
    "Touch it, make it twice, before I cry",
    "Heaven is a time today",
    "Put your hands up in the air",
    "All of the dream, how does it mean?",
    "When the rhythm is glad",
    "There is nothing to be sad",
    "Danger and dance",
    "Clapping the hands",
    "When we out in the space",
    "On the planet of the bass",
    "Life, it never die",
    "Women are my favorite guy",
    "Sex, I'm wanting more",
    "Tell the world, 'Stop the war'",
    "Boom, hear the bass go zoom",
    "Have a body, feel the groove",
    "Cyber system overload",
    "Everybody movement",
    "All of the dream, how does it mean?",
    "When the rhythm is glad",
    "There is nothing to be sad",
    "Danger and dance",
    "Clapping the hands",
    "When we out in the space",
    "On the planet of the bass",
    "Hello, are you at phone?",
    "Yes, it's true, yes, it's true",
    "Are you the girl of the love?",
    "Yes, I am a girl",
    "I love you and feel groove",
    "I love you too",
    "I want the sex on the phone",
    "I am so alone in the night",
    "Goodbye",
    "Goodbye",
    "And tonight, I will never die",
    "That is good to me as well as that",
]

# and our "standard english" translation:
manuallyTranslated = [
    "Alert, alert!",
    "DJ Crazy Times, If you want to throw a party",
    "Make some noise",
    "Bratislava!",
    "All the women in the world",
    "Let me see your beautiful faces",
    "Oh, I've got an idea",
    "World peace!",
    "When your secret love is like a dream",
    "And people are having fun",
    "We are losing control on the floor tonight",
    "You are as rare as a unicorn",
    "If the sky is not green, but the sky is blue",
    "Have great passion",
    "Touch me again, before I cry",
    "Heaven is when I'm with you",
    "Put your hands up in the air",
    "What do these dreams mean?",
    "When the rhythm is good",
    "There is no reason to be sad",
    "Danger and dance",
    "Clap your hands",
    "When we're out in space",
    "On the planet of the bass",
    "Life never dies",
    "I love women",
    "Sex, I want more",
    "Tell the world, 'Stop the war'",
    "Boom, hear the bass go zoom",
    "In your body, feel the groove",
    "Cyber system overload",
    "Everybody move",
    "What do these dreams mean?",
    "When the rhythm is good",
    "There is no reason to be sad",
    "Danger and dance",
    "Clap your hands",
    "When we're out in space",
    "On the planet of the bass",
    "Hello, are you there?",
    "Yes, I am",
    "Are you the girl of my dreams?",
    "Yes, I am a girl",
    "I love you and feel groovy",
    "I love you too",
    "I want phone sex",
    "I am so alone in the night",
    "Goodbye",
    "Goodbye",
    "And tonight, I will not die",
    "That is good with me as well",
]

# both 51 lines long
# print(len(original))
# print(len(manuallyTranslated))

# ensure that both are in lowercase:
original = [o.lower() for o in original]
manuallyTranslated = [m.lower() for m in manuallyTranslated]

# make some selections? Here's the full list to choose from:
allLanguages = {
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "azerbaijani": "az",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "chichewa": "ny",
    "chinese (simplified)": "zh-cn",
    "chinese (traditional)": "zh-tw",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "filipino": "tl",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "haitian creole": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "he",
    "hindi": "hi",
    "hmong": "hmn",
    "hungarian": "hu",
    "icelandic": "is",
    "igbo": "ig",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "korean": "ko",
    "kurdish (kurmanji)": "ku",
    "kyrgyz": "ky",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lithuanian": "lt",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "mongolian": "mn",
    "myanmar (burmese)": "my",
    "nepali": "ne",
    "norwegian": "no",
    "odia": "or",
    "pashto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "scots gaelic": "gd",
    "serbian": "sr",
    "sesotho": "st",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "telugu": "te",
    "thai": "th",
    "turkish": "tr",
    "ukrainian": "uk",
    "urdu": "ur",
    "uyghur": "ug",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zulu": "zu",
}

# realistically it's probably these european ones:
possibleLanguages = {
    "albanian": "sq",
    "armenian": "hy",
    "azerbaijani": "az",
    "basque": "eu",
    "belarusian": "be",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "esperanto": "eo",
    "estonian": "et",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "hungarian": "hu",
    "icelandic": "is",
    "irish": "ga",
    "italian": "it",
    "kazakh": "kk",
    "kyrgyz": "ky",
    "latin": "la",
    "latvian": "lv",
    "lithuanian": "lt",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "maltese": "mt",
    "norwegian": "no",
    "odia": "or",
    "polish": "pl",
    "portuguese": "pt",
    "romanian": "ro",
    "russian": "ru",
    "scots gaelic": "gd",
    "serbian": "sr",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "swedish": "sv",
    "turkish": "tr",
    "ukrainian": "uk",
    "uzbek": "uz",
    "welsh": "cy",
    "yiddish": "yi",
}
# just the codes:
possibleLanguages = list(possibleLanguages.values())


def compareToOriginal(language, inputTranslation):
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

        if retranslatedSentence == original[i]:
            numSame += 1
        i += 1

    #print("numSame:", numSame)
    return numSame

for langCode in possibleLanguages:
    num = compareToOriginal(langCode, manuallyTranslated)
    print(langCode, 'has this many matches with original:', num)
