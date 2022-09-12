import requests

BLOCKCHAIN_API_SINGLE_ADDRESS = 'https://blockchain.info/rawaddr/'
BLOCKCHAIN_API_MULTI_ADDRESS = 'https://blockchain.info/multiaddr?active='

def retrieve_address_data(address):
    """
    Make an API request and retrieve address data from blockchain.
    """
    url = BLOCKCHAIN_API_SINGLE_ADDRESS + address
    req = requests.get(url=url)
    address_data = parse_address_data(req.json())
    return address_data


def retrieve_multi_address_data(addresses):
    """
    Make an API request and retrieve data for the give addresses."""
    url = BLOCKCHAIN_API_MULTI_ADDRESS + "|".join(addresses)
    req = requests.get(url=url)
    res_data = req.json()
    data = []
    for address_data in res_data.get("addresses"):
        data.append(parse_address_data(address_data))
    return data

def parse_address_data(data):
    address_data = {
        'address': data['address'],
        'address_hash': data.get('hash160') or data.get('base58'),
        'total_transactions': data['n_tx'],
        'total_received': data['total_received'],
        'total_sent': data['total_sent'],
        'final_balance': data['final_balance'],
        'txs_hash': [tx['hash'] for tx in data.get('txs')]
    }
    return address_data