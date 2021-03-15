import random
from client_sdk_python import Web3
from user import User
from utils import delegable_nodes, get_delegate_list_for_node, get_cfg


class Action(User):

    def __init__(self, total_account: int):
        super().__init__(total_account)
        self.delegate_counter = 0
        self.undelegate_counter = 0
        self.withdraw_reward_counter = 0

    # 使用随机账号和金额，委托随机节点
    def delegate(self, account):
        node = random.choice(delegable_nodes)
        balance_type = random.randint(0, 1)
        # balance_type = 0
        amount = int(random.uniform(10, 100) * 10 ** 18)
        self.logger.info(f"node: {node['NodeId']}, balance_type: {balance_type}, amount: {amount}")
        result = self.ppos.delegate(balance_type, node['NodeId'], amount, account.private_key, get_cfg("nonce", account.nonce))
        self.delegate_counter += 1
        return result['hash']

    # 使用随机账号和节点，解委托随机金额
    def undelegate(self, account):
        node = random.choice(delegable_nodes)
        node_id = node['NodeId']
        delegates_info = get_delegate_list_for_node(account.address, node_id)
        if not delegates_info:
            self.logger.info(f"Skip: The choice node is not delegated! node: {node_id}")
            return False
        delegate_info = random.choice(delegates_info)
        delegate = self.ppos.getDelegateInfo(delegate_info['StakingBlockNum'], account.address, node_id)['Ret']
        block_number = delegate['StakingBlockNum']
        max_amount = delegate['Released'] + delegate['ReleasedHes'] + delegate['RestrictingPlan'] + delegate['RestrictingPlanHes']
        amount = random.randint(10 * 10 ** 18, max_amount)
        self.logger.info(f"node: {node_id}, block_number: {block_number}, amount: {amount}")
        result = self.ppos.withdrewDelegate(block_number, node_id, amount, account.private_key, get_cfg("nonce", account.nonce))
        self.undelegate_counter += 1
        return result['hash']

    # 使用随机账号领取委托分红
    def withdraw_reward(self, account):
        self.logger.info(f'nonce: {account.nonce}')
        result = self.ppos.withdrawDelegateReward(account.private_key, get_cfg("nonce", account.nonce))
        self.withdraw_reward_counter += 1
        return result['hash']
