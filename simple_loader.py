import random
import time
import logging
from simple_tx import SimpleTx
import threading


class User:

    def __init__(self, tx, total_account: int, log_file: str):
        # self.tx = SimpleTx(rpc, chain_id)
        self.tx = tx
        self.accounts = self.create_accounts(total_account)
        self.delegable_nodes = delegable_nodes
        # self.delegable_nodes = tx.get_delegable_nodes(cdf_address)['Ret']
        # 记录线程日志
        self.logger = logging.Logger(log_file)
        fh = logging.FileHandler(filename=log_file, mode='a', encoding='utf-8')
        self.logger.addHandler(fh)

    # 记录线程日志
    def logger(self):
        pass

    # 创建初始账户
    def create_accounts(self, total):
        accounts = []
        for _ in range(total):
            address, private_key = self.tx.create_account()
            amount = 2000 * 10 ** 18
            plan = [{'Epoch': 5000, 'Amount': amount}]
            self.tx.transfer(main_private_key, address, amount)
            self.tx.restricting(main_private_key, address, plan)
            accounts.append([address, private_key, 0])
        return accounts

    # 灵活控制启动时的参数
    def start(self, duration, ratio_setting):
        current_time = time.time()
        end_time = current_time + duration
        # 随机选择用户请求
        while current_time < end_time:
            account = random.choice(self.accounts)
            try:
                self.random_request(account, ratio_setting)
            except Exception as e:  # todo: recover_nonce
                # recover_nonce(account)
                raise e
            current_time = time.time()

    # 选择压测方法
    def random_request(self, account, ratio_setting):
        r = random.randint(1, sum(ratio_setting))
        if r <= ratio_setting[0]:
            # 委托
            self._delegate(account)
        elif ratio_setting[0] < r <= sum(ratio_setting[:2]):
            # 减持/撤销委托
            self._undelegate(account)
        else:
            # 领取委托奖励
            self._withdraw_reward(account)

    def _delegate(self, account):
        self.logger.info('_delegate')
        private_key = account[1]
        node = random.choice(self.delegable_nodes)
        node_id = node['NodeId']
        balance_type = random.randint(0, 1)
        amount = int(random.uniform(10, 100) * 10 ** 18)
        self.tx.delegate(private_key, node_id, balance_type, amount)

    def _undelegate(self, account):
        self.logger.info('_undelegate')
        node = random.choice(self.delegable_nodes)
        address, private_key = account[0], account[1]
        node_id = node['NodeId']
        delegates_info = self.tx.get_delegate_list_for_node(address, node_id)
        if delegates_info['Code'] != 0:
            self.logger.info(f"The choice node is not delegated!")
            return
        delegate_info = random.choice(delegates_info['Ret'])
        delegate = tx.get_delegate_info(address, node_id, delegate_info['StakingBlockNum'])['Ret']
        block_number = delegate['StakingBlockNum']
        max_amount = delegate['Released'] + delegate['ReleasedHes'] + delegate['RestrictingPlan'] + delegate['RestrictingPlanHes']
        amount = random.randint(10 * 10 ** 18, max_amount)
        self.tx.undelegate(private_key, node_id, block_number, amount)

    def _withdraw_reward(self, account):
        self.logger.info('_withdraw_reward')
        private_key = account[1]
        self.tx.withdraw_delegate_reward(private_key)

    def recover_nonce(account):
        pass


if __name__ == '__main__':
    """
    使用方法：
    - 根据配置的请求时长、请求发送比例，运行简单压测
    """
    # 配置项
    rpc = 'http://192.168.120.121:6789'
    chain_id = 201018
    load_threads = 100       # 压测线程数
    load_accounts = 100     # 压测账户数，不低于线程数
    load_duration = 180     # 压测时长/s
    load_ratio = (4, 4, 2)  # 各请求的发送比率
    main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
    cdf_address, cdf_private_key = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx', 'f767d379a652ab5cc8c85cd7fef1b00bffcec90697dcfd6c64991dd284cac4e9'
    # 日志配置
    logging.basicConfig(filename='T-.log',
                        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %p',
                        level=logging.INFO)
    # 基础信息生成
    tx = SimpleTx(rpc, chain_id)
    delegable_nodes = tx.get_delegable_nodes(cdf_address)['Ret']
    # tx.ppos.need_analyze = False
    logging.info(f'Delegable nodes = {delegable_nodes}')
    assert delegable_nodes, 'Delegable nodes is empty!'
    # 创建多线程
    threads = []
    accounts_per_thread = int(load_accounts / load_threads)
    for i in range(load_threads):
        user = User(tx, accounts_per_thread, f'T{i}')
        t = threading.Thread(target=user.start, name=f'T{i}', args=(load_duration, load_ratio))
        threads.append(t)
    # 启动多线程
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
        logging.info(f'Thread [{thread.name}] start!')
    # 等待线程运行完成
    for thread in threads:
        thread.join()
    logging.info(f'All thread over!')
