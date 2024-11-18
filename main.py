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

    print(response)
    if response.status_code != 200:
        print("Invalid Wallet Address", sys.stderr)
        return 1

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify())

if __name__ == "__main__":
    main()