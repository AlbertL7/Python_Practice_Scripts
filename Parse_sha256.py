import requests
import re
r = requests.get("https://www.trendmicro.com/content/dam/trendmicro/global/en/research/23/h/mmrat-carries-out-bank-fraud-via-fake-app-stores/IOC_stealthy-android-malware-mmrat-carries-out-bank-fraud-via-fake-app-stores.txt")

sha256 = []

for i in r:
    if isinstance(i, bytes):
        i = i.decode('utf-8')
        
    match = re.search(r"\b[A-Fa-f0-9]{64}\b", i)

    if match:
        sha256.append(match.group())

print(" \n".join(sha256))
