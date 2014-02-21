import random
import requests
import bleach

text = ""
mark = {}
start = "gentoo"
endtxt = ""

for j in range(0, 11):
    r = requests.get("http://a.4cdn.org/g/" + str(j) + ".json")
    for i in r.json()["threads"]:
        try:
            soup = i["posts"][0]["com"]
            soup.replace("<br/>", " ")
            soup = bleach.clean(soup, tags={}, attributes={}, styles={}, strip=True, strip_comments=True)
            soup = soup.replace("&gt;", " ").lower()
            text += soup + ""
        except KeyError:
            pass

try:
    for i, j in enumerate(text.split(" ")):
        try:
            n = str(text.split(" ")[i+1])
            j = str(j)
        except UnicodeEncodeError:
            pass
        try:
            mark[j].append(n)
        except KeyError:
            mark.update({j: [n]})
except IndexError:
    pass

c = start
endtxt += start + " "
for i in range(0, 50):
    r = random.randint(0, len(mark[c]) - 1)
    endtxt += mark[c][r] + " "
    c = mark[c][r]

print endtxt