# encoding: utf-8
import re


with open('./raw.txt') as file:
    contents = file.read()


class Conversion(object):
    def __init__(self, pattern, replacement):
        self.pattern = re.compile(r'\b{}\b'.format(pattern))
        self.replacement = replacement

    def process(self, text):
        return re.sub(self.pattern, self.replacement, text)

conversions = [
    Conversion('male', 'white'),
    Conversion('female', 'black'),

    Conversion('woman', 'black person'),
    Conversion('women', 'black people'),
    Conversion('man', 'white man'),
    Conversion("men’s rights", "white rights"),
    Conversion("men’s", "white people’s"),
    Conversion('men', 'white people'),
    Conversion('white white man', 'white man'),  # Heh, a little too on-the-nose
    Conversion('Men', 'White people'),
    Conversion('Male', 'White'),

    Conversion('gender', 'race'),
    Conversion('sexes', 'races'),
    Conversion('sexual', 'racial'),
    Conversion('feminists', 'civil rights workers'),
    Conversion('feminist', 'civil rights worker'),

    Conversion('Mgtow', 'Wgtow'),
    Conversion('MIG-tow', 'WIG-tow'),
    Conversion('marriage', 'mixing'),
    # Conversion('technology', 'banking'),
    # Conversion('tech', 'banking'),
    # Conversion('Silicon Valley', 'Wall Street'),
    # Conversion('Google', 'Goldman Sachs'),
    # Conversion('Yahoo', 'Morgan Stanley'),
    # Conversion('chip maker Nvidia', 'investment firm Fidelity'),
    # Conversion('engineer', 'analyst'),
    # Conversion('computers, games, consoles', 'analysis, candlestick charts, futures'),
    # Conversion('engineering', 'investing'),

    Conversion('they uniquely face', 'they uniquely face, difficulties that underrepresented groups can easily sympathize with'),
]

translated = contents
for converstion in conversions:
    translated = converstion.process(translated)

with open('./output.txt', 'w') as file:
    file.write(translated)

