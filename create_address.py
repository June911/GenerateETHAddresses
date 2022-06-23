from web3 import Web3
import json

NUM_OF_ADDRESSES = 3


def create_addresses(NUM_OF_ADDRESSES, include_public_key=True):
    """
    create ethereum addresses, save as json file, can be read by json.loads()

    Args:
        NUM_OF_ADDRESSES (_type_): number of addresses to genrate
        include_public_key (bool, optional): _description_. Defaults to True.
    """
    w3 = Web3()

    if include_public_key:
        list_addresses = []
        for i in range(NUM_OF_ADDRESSES):
            acct = w3.eth.account.create()
            list_addresses.append(
                {"address": acct.address, "private_key": acct.privateKey.hex()}
            )
        with open("addresses.json", "w") as fp:
            json.dump(list_addresses, fp)
    else:
        list_private_key = []
        for i in range(NUM_OF_ADDRESSES):
            acct = w3.eth.account.create()
            list_private_key.append(acct.privateKey.hex())
        with open("private_key.json", "w") as fp:
            json.dump(list_private_key, fp)


def main():
    create_addresses(NUM_OF_ADDRESSES)


if __name__ == "__main__":
    main()
