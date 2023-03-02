import os
import re
from googletrans import Translator
from bs4 import BeautifulSoup
translator = Translator()

directory = 'www.classcentral.com/'

# find all html files
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith("contact.html"):
            pathtofile = str(os.path.join(root, filename))

            print(pathtofile)
            # open html files
            with open(pathtofile, 'r+') as f:
                html = f.read()

                # pattern = r'<\s*a[^>]*>(.*?)<\s*/\s*a>'

                # find texts in html files
                #string = re.findall(pattern, html)
                soup = BeautifulSoup(html, 'html.parser')


                allowlist = [
                    'p'
                ]

                soup.find_all(allowlist)
                text = soup.get_text('&#', strip=True)
                full_text = text.split("&#")
                print(full_text)


                for i in full_text:
                    try:
                        # translate html files strings
                        translated_string = translator.translate(text=i, src='en', dest='hindi')
                        if translated_string == i:
                            continue
                        else:
                            print(i, translated_string.text)
                            html = html.replace(i, translated_string.text)
                    except:
                        print(i)
                        continue

                #write translated html back to file
                f.seek(0)
                f.write(html)
                f.truncate()



# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)
# hindi
