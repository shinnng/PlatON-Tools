import random
import time
from loguru import logger
from simple_tx import SimpleTx
from threading import Thread


# 基础信息生成
def create_accounts(num: int):
    accounts = {}
    for _ in range(num):
        address, private_key = tx.create_account()
        accounts[address] = private_key
    return accounts

def gen_nonce_dict(keys: list):
    nonces = {}
    for key in keys:
        nonces[key] = 0     # todo: get nonce
    return nonces

# 压测基本方法
def gen_request(account, nodes, ratio_setting):
    print(f'goto gen request!')
    r = random.randint(1, sum(ratio_setting))
    node_id = random.choice(nodes)
    balance_type = random.randint(0, 1)
    # 随机请求
    if r <= ratio_setting[0]:
        amount = random.randint(10, 100)
        tx.delegation(account[1], node_id, balance_type, amount)
    elif ratio_setting[0] < r <= sum(ratio_setting[0, 1]):
        amount = random.randint(10, tx.ppos.getDelegateInfo())
        tx.undelegation(account[1], node_id, amount)
    else:
        tx.withdraw_delegate_reward()

def recover_nonce():
    pass

def loader(account, nodes, duration, ratio_setting):
    ct = time.time()
    end = ct + duration * 1000
    while ct < end:
        try:
            gen_request(account, nodes, ratio_setting)
        except Exception as e:
            recover_nonce(account)          # todo: recover_nonce
            raise e
        ct = time.time()


if __name__ == '__main__':
    """
    使用方法：
    - 根据配置的请求时长、请求发送比例，运行简单压测
    """
    # 配置项
    rpc = 'http://192.168.120.121:6789'
    chain_id = 201018
    load_duration = 60  # 压测时长/s
    load_threads = 3  # 线程数
    load_ratio = (65, 30, 5)  # 几率配置
    cdf_address = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx'
    tx = SimpleTx(rpc, chain_id)
    # 基础信息生成
    accounts = create_accounts(load_threads)
    account_list = list(accounts.items())
    nodes = tx.get_delegable_nodes(cdf_address)
    assert nodes, 'Delegable nodes is empty!'
    # 创建多线程
    threads = []
    for i in range(load_threads):
        account = account_list[i]
        t = Thread(target=loader, name=f't{i}', args=(account, nodes, load_duration, load_ratio))
        threads.append(t)
    # 启动多线程
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
        logger.info(f'Thread [{thread.name}] start!')
    # 等待子线程运行完成
    for thread in threads:
        thread.join()
    print(f'All thread over!')
