class Account:

    def __init__(self, address: str, private_key: str, nonce: int):
        self.address = address
        self.private_key = private_key
        self.nonce = nonce