import random
import time
from loguru import logger
from simple_tx import SimpleTx
from threading import Thread


# 基础信息生成
def create_accounts(num: int):
    accounts = []
    for _ in range(num):
        address, private_key = tx.create_account()
        accounts.append((address, private_key))
    return accounts


def gen_nonce_dict(keys: list):
    nonces = {}
    for key in keys:
        nonces[key] = 0  # todo: get nonce
    return nonces


# 压测基本方法
def gen_request(account, nodes, ratio_setting):
    r = random.randint(1, sum(ratio_setting))
    node = random.choice(nodes)
    balance_type = random.randint(0, 1)
    # 随机请求
    if r <= ratio_setting[0]:
        amount = random.randint(10, 100) * 10 ** 18
        tx.delegation(account[1], node['NodeId'], balance_type, amount)
    elif ratio_setting[0] < r <= sum(ratio_setting[:2]):
        # max_amount = tx.ppos.getDelegateInfo()
        amount = random.randint(10, 20) * 10 ** 18
        tx.undelegation(account[1], node['NodeId'], amount)
    # else:
    #     tx.withdraw_delegate_reward()


def recover_nonce(account):
    pass


def loader(account, nodes, duration, ratio_setting):
    ct = time.time()
    end = ct + duration * 1000
    while ct < end:
        try:
            gen_request(account, nodes, ratio_setting)
        except Exception as e:
            recover_nonce(account)  # todo: recover_nonce
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
    load_duration = 10  # 压测时长/s
    load_threads = 3  # 线程数,也是压测账户数
    load_ratio = (65, 30, 5)  # 配置各请求的发送几率
    init_amount = 1000  # 账户中的初始金额/later
    main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
    cdf_address, cdf_private_key = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx', 'f767d379a652ab5cc8c85cd7fef1b00bffcec90697dcfd6c64991dd284cac4e9'
    tx = SimpleTx(rpc, chain_id)
    # 基础信息生成
    accounts = create_accounts(load_threads)
    for account in accounts:
        amount = init_amount * 10 ** 18
        tx.transfer(main_private_key, account[0], amount)
    nodes = tx.get_delegable_nodes(cdf_address)
    assert nodes, 'Delegable nodes is empty!'
    # 创建多线程
    threads = []
    for i in range(load_threads):
        account = accounts[i]
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
