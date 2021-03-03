import random
import time

from client_sdk_python import Account
from loguru import logger
from simple_tx import SimpleTx
from threading import Thread


# 基础信息生成
def create_accounts(num: int):
    logger.info(f'======== create accounts ========')
    accounts = []
    for _ in range(num):
        address, private_key = tx.create_account()
        accounts.append((address, private_key))
    return accounts


def gen_nonce_dict(keys: list):
    logger.info(f'======== gen nonce dict ========')
    nonces = {}
    for key in keys:
        nonces[key] = 0  # todo: get nonce
    return nonces


# 压测请求生成
def delegate(private_key, node_id):
    logger.info(f'======== delegate ========')
    balance_type = random.randint(0, 1)
    amount = int(random.uniform(10, 100) * 10 ** 18)
    tx.delegate(private_key, node_id, balance_type, amount)


def undelegate(private_key, node_id):
    logger.info(f'======== undelegate ========')
    address = Account.privateKeyToAccount(private_key, 'lat').address
    delegates = tx.get_delegate_list_for_node(address, node_id)
    if delegates['Code'] != 0:
        logger.info(f"The choice node is not delegated!")
        return
    rd = random.choice(delegates['Ret'])
    delegate = tx.get_delegate_info(address, node_id, rd['StakingBlockNum'])['Ret']
    block_number = delegate['StakingBlockNum']
    max_amount = delegate['Released'] + delegate['ReleasedHes'] + delegate['RestrictingPlan'] + delegate['RestrictingPlanHes']
    amount = random.randint(10 * 10 ** 18, max_amount)
    tx.undelegate(private_key, node_id, block_number, amount)


def withdra_reward(private_key):
    logger.info(f'======== withdra reward ========')
    tx.withdraw_delegate_reward(private_key)


# 压测过程方法
def gen_request(account, nodes, ratio_setting):
    # 参数准备
    address, private_key = account[0], account[1]
    node = random.choice(nodes)
    node_id = node['NodeId']
    # 随机请求
    r = random.randint(1, sum(ratio_setting))
    if r <= ratio_setting[0]:
        delegate(private_key, node_id)  # 委托
    elif ratio_setting[0] < r <= sum(ratio_setting[:2]):
        undelegate(private_key, node_id)  # 减持/撤销委托
    else:
        withdra_reward(private_key)  # 领取委托奖励


def recover_nonce(account):
    pass


def loader(account, nodes, duration, ratio_setting):
    ct = time.time()
    end = ct + duration
    while ct < end:
        try:
            gen_request(account, nodes, ratio_setting)
        except Exception as e:  # todo: recover_nonce
            # recover_nonce(account)
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
    load_threads = 10  # 线程数,也是压测账户数
    load_ratio = (60, 30, 10)  # 配置各请求的发送几率
    init_amount = 1000  # 账户中的初始金额/later
    main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
    cdf_address, cdf_private_key = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx', 'f767d379a652ab5cc8c85cd7fef1b00bffcec90697dcfd6c64991dd284cac4e9'
    tx = SimpleTx(rpc, chain_id)
    # 基础信息生成
    accounts = create_accounts(load_threads)
    for account in accounts:
        amount = init_amount * 10 ** 18
        tx.transfer(main_private_key, account[0], amount)
        plan = [{'Epoch': int(load_duration / 20) + 1, 'Amount': amount}]
        tx.restricting(main_private_key, account[0], plan)
    nodes = tx.get_delegable_nodes(cdf_address)['Ret']
    logger.info(f'nodes = {nodes}')
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
        logger.info(f'Thread [{thread.name}] start!')
        thread.start()
    # 等待子线程运行完成
    for thread in threads:
        thread.join()
    print(f'All thread over!')
