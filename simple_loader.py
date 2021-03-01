import time

from simple_tx import SimpleTx
from random import randint, sample
from threading import Thread

"""
使用方法：
- 根据配置的请求时长、请求发送比例，运行简单压测
"""

# 配置项
rpc = 'http://0.0.0.0:6789'
load_duration = 3600  # 压测时长
load_threads = 30  # 线程数
load_ratio = (65, 30, 5)  # 几率配置
cdf_address = 'atx1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4xerq62'
tx = SimpleTx(rpc)


# 基础信息生成
def create_accounts(num: int):
    accounts = {}
    for _ in range(num):
        address, private_key = tx.create_account()
        accounts['address'] = private_key
    return accounts


def gen_nonce_dict(keys: list):
    nonces = {}
    for key in keys:
        # todo: get nonce
        nonces[key] = 0
    return nonces


accounts = create_accounts(load_threads)
# nonce_manager = gen_nonce_dict(accounts.keys())  # coding
nodes = tx.get_delegable_nodes(cdf_address)


# 压测基本方法
def gen_request(address):
    r = randint(1, sum(load_ratio))
    node_id = sample(nodes, 1)
    balance_type = randint(0, 1)
    # 随机请求
    if r <= load_ratio[0]:
        amount = randint(10, 100)
        tx.delegation(accounts[address], node_id, balance_type, amount)
    elif load_ratio[0] < r <= sum(load_ratio[0, 1]):
        amount = randint(10, tx.ppos.getDelegateInfo())
        tx.undelegation(address, node_id, amount)
    else:
        tx.withdraw_delegate_reward()


def recover_nonce():
    pass


def load(address, duration):
    ct = time.time()
    end = ct + duration * 1000
    while ct > end:
        try:
            gen_request(address)
        except Exception as e:
            # todo: recover_nonce
            recover_nonce(address)
        ct = time.time()


# 多线程压测
for i in range(load_threads):
    address = accounts[i]
    Thread(load, name=f't{i}', args=(address, load_duration)).start()
