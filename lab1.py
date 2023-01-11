import requests
from pathlib import Path

print(requests.__version__)

print(requests.get("http://google.com").text)

url = "https://raw.githubusercontent.com/MichaelLsh/cmput404-lab1/main/lab1.py"
r  = requests.get(url)

p = Path(__file__).with_name('lab01.py')
with p.open('w') as f:
    f.write(r.text)
print(r.text)
