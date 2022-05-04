import requests
import random

def divar_bomber(number):
    bold = '\033[1m'

    heads = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '*/*'
        },
    ]
    rhead = random.choice(heads)
    divarnumber = {"phone": number}
    divar = 'https://api.divar.ir/v5/auth/authenticate'

    try:
        req = requests.post(divar, json=divarnumber, headers=rhead)
        return req.status_code
    except:
        return 404


