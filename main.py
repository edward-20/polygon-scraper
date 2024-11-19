'''
main file for program
'''
import sys
import requests
from bs4 import BeautifulSoup

def main():
    '''
    main
    '''
    wallet_address = input("Please input a valid wallet address: ")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(f"https://polygonscan.com/address/{wallet_address}#tokentxns", headers=headers, timeout=10)

    if response.status_code != 200:
        print("Invalid Wallet Address", sys.stderr)
        return 1

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr')

    print("transaction hash | age | from | in/out | to | amount | token")
    for row in rows:
        # second td is transaction hash
        cells = row.find_all('td')
        print(len(cells))
        # transaction_hash = cells[1].find('a')['href']
        # print(transaction_hash)
        # age = cells[4]
        # sender = cells[6]
        # in_out = cells[7]
        # to = cells[8]
        # amount = cells[9]
        # token = cells[10]
        # p


if __name__ == "__main__":
    main()