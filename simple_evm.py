from functools import wraps

from alaya import Web3
from alaya.contract import ContractFunction
from alaya.packages.platon_account.signers.local import LocalAccount
from alaya.utils.abi import filter_by_name


def deploy(web3: Web3, bytecode: str, abi: str, account: LocalAccount, **constructor_args):
    nonce = web3.eth.getTransactionCount(account.address)
    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    transaction = {
        'gas': 4012388,
        'gasPrice': 100000000,
        "chainId": web3.chain_id,
        "nonce": nonce,
    }
    data = contract._encode_constructor_data(kwargs=constructor_args)
    transaction["data"] = data
    signed_tx = web3.eth.account.signTransaction(transaction, account.privateKey).rawTransaction
    tx_hex = web3.eth.sendRawTransaction(signed_tx)
    receipt = web3.eth.waitForTransactionReceipt(tx_hex)
    address = receipt['contractAddress']
    return Contract(web3, bytecode, abi, address, account)


class Contract:

    def __init__(self, web3: Web3, bytecode: str, abi: str, address: str, account: LocalAccount = None):
        self.web3 = web3
        self.bytecode = bytecode
        self.abi = abi
        self.address = address
        self.account = account
        self.contract = web3.eth.contract(abi=abi, bytecode=bytecode)
        self.functions = self.contract.functions
        self.events = self.contract.events
        self._set_functions(self.contract.functions)
        self._set_events(self.contract.events)
        self._set_fallback(self.contract.fallback)

    def _set_functions(self, functions):
        for func in functions:
            # 通过方法名获取方法
            warp_function = self._function_wrap(getattr(functions, func))
            setattr(self, func, warp_function)

    def _set_events(self, events):
        for event in events:
            # 通过方法名获取方法
            warp_event = self._event_wrap(getattr(events, event))
            setattr(self, event, warp_event)

    def _set_fallback(self, fallback):
        if type(fallback) is ContractFunction:
            warp_fallback = self._fallback_wrap(fallback)
            setattr(self, fallback, warp_fallback)
        else:
            self.fallback = fallback

    def _function_wrap(self, func):
        @wraps(func)
        def call_selector(*args, **kwargs):
            fn_abi = filter_by_name(func.fn_name, self.abi)
            assert len(fn_abi) == 1, 'The method cannot be found in the ABI'
            if fn_abi[0].get('stateMutability') == 'view':
                tx = {
                    'chainId': self.web3.chain_id,
                    'nonce': self.web3.eth.getTransactionCount(self.account.address),
                    'gas': 9424776,
                    'value': 0,
                    'gasPrice': 1000000000,
                    'to': self.address
                }
                txn = func(*args, **kwargs).buildTransaction(tx)
                return self.web3.eth.call(txn)
            else:
                tx = {
                    'chainId': self.web3.chain_id,
                    'nonce': self.web3.eth.getTransactionCount(self.account.address),
                    'gas': 9424776,
                    'value': 0,
                    'gasPrice': 1000000000,
                    'to': self.address
                }
                txn = func(*args, **kwargs).buildTransaction(tx)
                signed_txn = self.web3.eth.account.signTransaction(txn, private_key=self.owner.privateKey.hex())
                tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
                return self.web3.eth.waitForTransactionReceipt(tx_hash)

        return call_selector

    def _event_wrap(self, func):
        @wraps(func)
        def call_selector(*args, **kwargs):
            return func.processReceipt(*args, **kwargs)

        return call_selector

    def _fallback_wrap(self, func):
        @wraps(func)
        def call_selector(*args, **kwargs):
            tx = {
                'chainId': self.web3.chain_id,
                'nonce': self.web3.eth.getTransactionCount(self.account.address),
                'gas': 9424776,
                'value': 0,
                'gasPrice': 1000000000,
                'to': self.address
            }
            txn = func(*args, **kwargs).buildTransaction(tx)
            signed_txn = self.web3.eth.account.signTransaction(txn, private_key=self.owner.privateKey.hex())
            tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
            return self.web3.eth.waitForTransactionReceipt(tx_hash)

        return call_selector
