import requests

while(True):
    ask = input('what crypto do you want? (example: BTC) \n')
    if len(ask) == 3:
        my_req = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair={}/USD' .format(ask.upper()))
        price = my_req.json()
        print('The current price is: ' ,price['last'])
        print('The lowest price in the previous 24 hours is: ' ,price['low'])
        print('The highest price in the previous 24 hours is: ' ,price['high'])
        ques = input('coninue? (y/n)')
        if ques == 'y':
            continue
        else:
            break
    else:
        print ('should be 3 words like BTC or ETH. not accepted BITCOIN or else ...')
        break



