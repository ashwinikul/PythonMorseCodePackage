# PythonMorseCodePackage
This package is created for three applications: English Language to Morse Code,  Morse Code to English Language, English Language to Morse Code Sound
this Package is for Morse Code application


1) Msg to sound
wordToMorseSound(msg string)

2) Msg to Code
wordToMorseCode(msg string)

3) Code to Msg
morseCodetoLang(code string)
Constraint:
double space between letters
Three spaces between Words
example
'..---  ...--     ...  -  .-.  .  .  -     .-.  -..'
Output = '23 Street'


from MorseCode import morse

morse.wordToMorseCode('23 Street')
Out[99]: '..---  ...--     -  .-.  .  .  -'

morse.morseCodetoLang('..---  ...--     ...  -  .-.  .  .  -     .-.  -..')
Out[100]: '23 street rd '
