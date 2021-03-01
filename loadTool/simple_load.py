from txTool.core.core import *
from random import randint, sample

"""
使用方法：
- 根据配置的请求时长、请求发送比例，运行简单压测
"""

# 配置项
load_duration = 3600
load_threads = 30
load_ratio = (6, 3, 1)
cdf_address = ''

# 基础信息生成
def create_users(user_count):
    for i in range(1, user_count):
        users = {}
        address, private_key = create_account()
        users['address'] = private_key
    return users

def gen_nonce_dict(user_dict: dict):
    nonces = {}
    for k, _ in user_dict:
        # TODO: get nonce
        nonce = 0
        nonces[k] = nonce

user_dict = create_users(load_threads)
nonce_dict = gen_nonce_dict(user_dict)
nodes = get_delegable_nodes(cdf_address)


    return

# 压测方法
delegation(address, node_id, balance_type, amount)



# 压测线程
r = randint(1, 100)
