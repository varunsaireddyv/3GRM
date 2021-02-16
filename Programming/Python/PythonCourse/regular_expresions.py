#matches a string that has an a followed by one or more b's
import re
Txt_Input=input('enter a word to run    ')
def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched'

print(text_match(Txt_Input))
