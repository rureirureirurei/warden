# warden
Auto-transfer funds from multiple eth/arbitrum accounts.

# Usage

1) Firstly, you'll have to create a `config.py` file. 

`request_delay_seconds` sets how often the script checks for balance updates for each account. 

`arbitrum_api_key` can be left unchanged.

`infura_api_key` should be set to your own value.

Here's an example:
```
accounts = [
    {
        'network': 'arbitrum',
        'arbitrum_api_key': 'https://arb1.arbitrum.io/rpc',
        'private_key': '1234567890123456789012345678901234567890123456789012345678901234',
        'public_key': '0x1234567890123456789012345678901234567890',
        'receiver': '0x1234567890123456789012345678901234567890',
        'request_delay_seconds': 1,
    },
    {
        'network': 'eth',
        'infura_api_key': 'https://mainnet.infura.io/v3/some_code_here',
        'private_key': '1234567890123456789012345678901234567890123456789012345678901234',
        'public_key': '0x1234567890123456789012345678901234567890',
        'receiver': '0x1234567890123456789012345678901234567890',
        'request_delay_seconds': 2,
    },
]
```

2) Install dependencies:
`pip install web3 multiprocess`

3) Run the script
`python3 main.py`

You should see something like this if everything runs correctly.
```
2023-04-21 00:50:30.637: Started watching 0x1234567890123456789012345678901234567890 with 0.00003178641 eth on the network arbitrum.

2023-04-21 00:50:30.668: Started watching 0x2224567890123456789012345678901234567890 with 0.00078276861 eth on the network eth.
```
4) Logging

All the important information will be saved to the `logs` file.
