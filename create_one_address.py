from web3 import Web3

w3 = Web3()
acct = w3.eth.account.create()
private_key = acct.privateKey.hex()
address = acct.address

print(private_key)
print(address)
