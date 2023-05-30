import requests

def getStock(search_type):
    headers = {
        'Host': 'xenx.vip',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
    return requests.get(f'https://xenx.vip/stock?name={search_type}', headers=headers)

def genAccount(search_type, UserID):
    headers = {
        'Host': 'xenx.vip',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
    return requests.get(f'https://xenx.vip/gen?name={search_type}&user={UserID}', headers=headers)

  print(genAccount('SEARCH_TYPE_HERE', 'DISCORD_ID_HERE').text)
