import os
import re
from googletrans import Translator

translator = Translator()

directory = 'www.classcentral.com/'

# find all html files
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".html"):
            pathtofile = str(os.path.join(root, filename))

            print(pathtofile)
            # open html files
            with open(pathtofile, 'r') as f:
                html = f.read()

            pattern = r'<\s*a[^>]*>(.*?)<\s*/\s*a>'

            # find texts in html files
            string = re.findall(pattern, html)
            for i in string:
                try:
                    # translate html files strings
                    translated_string = translator.translate(text=i, src='en', dest='hindi')
                    print(translated_string.text)
                    html = html.replace(i, translated_string)

                    with open(pathtofile, "w") as f:
                        f.write(html)

                except:
                    continue




# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)
# hindi
