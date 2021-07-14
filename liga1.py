import requests
from bs4 import BeautifulSoup

r = requests.get("https://lpf.ro/liga-1")
s1 = BeautifulSoup(r.text, "html.parser")

fisier = open("programariliga1.html", "w")

rand = s1.table.find("tr")
fisier.write('<html><head>Clasament</head><body><table><thead><tr style="color: red;">')
for tr in rand:
    fisier.write(f"<th>{tr.text}</th>")
fisier.write('</tr></thead><tbody>')
for tr in s1.table.select('tr')[1:]:
    fisier.write('<tr>')
    for x in tr.select('td'):
        fisier.write(f"<td>{x.text}</td>")
    fisier.write('</tr>')
fisier.write('</tbody></table></body></html>')

