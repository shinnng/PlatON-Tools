import logging
import time
from threading import currentThread, Lock
from client_sdk_python import Web3
from client_sdk_python.eth import PlatON
from client_sdk_python.ppos import Ppos
from hexbytes import HexBytes
from account import Account
from setting import main_private_key, load_amount, main_nonce
from utils import create_account, lock


class User:

    def __init__(self, web3: Web3, total_account: int):
        # 初始化线程日志
        log_file = currentThread().getName()
        self.logger = logging.Logger(log_file)
        fh = logging.FileHandler(filename=log_file, mode='a', encoding='utf-8')
        self.logger.addHandler(fh)
        # 初始化对象
        self.web3 = web3
        self.platon = PlatON(self.web3)
        self.ppos = Ppos(self.web3)
        self.ppos.need_analyze = False
        self.accounts = self.create_accounts(total_account)
        self.address_list = [i for i in self.accounts.keys()]

    # 创建初始账户
    def create_accounts(self, total) -> dict:
        global main_nonce, transfer_hash, restrict_hash
        accounts = {}
        for _ in range(total):
            address, private_key = create_account(self.web3)
            self.logger.info(f'new account: {address}, {private_key}')
            account = Account(address, private_key, 0)
            accounts[address] = account
            lock.acquire()      # 加锁
            # 转账
            self.transfer(address, load_amount * 10 ** 18, main_nonce, main_private_key)
            main_nonce = main_nonce + 1
            # 锁仓
            result = self.ppos.createRestrictingPlan(address, [{'Epoch': 2000, 'Amount': load_amount * 10 ** 18}], main_private_key, {"nonce": main_nonce})
            main_nonce = main_nonce + 1
            lock.release()      # 解锁
        self.platon.waitForTransactionReceipt(result['hash'])
        # time.sleep(5)
        return accounts

    # 转账交易
    def transfer(self, to, amount, nonce, private_key):
        transaction_dict = {
            "to": to,
            "gasPrice": self.platon.gasPrice,
            "gas": 21000,
            "nonce": nonce,
            "data": '',
            "chainId": self.web3.chain_id,
            "value": amount,
        }
        signedTransactionDict = self.platon.account.signTransaction(transaction_dict, private_key)
        data = signedTransactionDict.rawTransaction
        result = HexBytes(self.platon.sendRawTransaction(data)).hex()
        return result

    # 恢复nonce
    def recover_nonce(account):
        pass
