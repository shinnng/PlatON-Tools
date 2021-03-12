import time
from client_sdk_python import HTTPProvider, Web3
from client_sdk_python import eth, ppos, pip
from client_sdk_python.middleware import geth_poa_middleware
from hexbytes import HexBytes
from client_sdk_python.packages.platon_account.account import Account
from loguru import logger


# 通用信息
class SimpleTx:
    tx_cfg = {'gasPrice': 3000000000000000}

    def __init__(self, rpc, chain_id):
        print("############################################")
        self.rpc = rpc
        self.chain_id = chain_id
        self.web3 = Web3(HTTPProvider(rpc), chain_id=chain_id)
        self.web3.middleware_stack.inject(geth_poa_middleware, layer=0)
        self.hrp = self.web3.net_type
        self.platon = eth.PlatON(self.web3)
        self.ppos = ppos.Ppos(self.web3)
        self.pip = pip.Pip(self.web3)

    # 创建账户
    def create_account(self):
        account = self.platon.account.create()
        address = account.address
        prikey = account.privateKey.hex()[2:]
        logger.info(f"create account = {address}, {prikey}")
        return address, prikey

    # 创建HD钱包
    # todo: coding
    # def create_hd_account():
    #     logger.info("==== create hd account =====")
    #     # account = self.web3.platon.account.(net_type=self.hrp)
    #     master_key, mnemonic = HDPrivateKey.master_key_from_entropy()
    #     logger.info(master_key)
    #     logger.info(mnemonic)
    #     root_keys = HDKey.from_path(master_key, "m/44'/206'/0'")
    #     logger.info(root_keys)
    #     acct_priv_key = root_keys[-1]
    #     logger.info(acct_priv_key)
    # for j in range(30):
    #     keys = HDKey.from_path(acct_priv_key, '{change}/{index}'.format(change=0, index=j))
    #     private_key = keys[-1]
    #     public_address = private_key.public_key.address('atp')
    #     keystores[public_address] = json.dumps(private_key._key.to_keyfile_json(password))
    #     privateKeys[public_address] = private_key._key.get_private_key()
    #     addresses_df.loc[(prikey_manager, account_use, wallet_type, i, j), :] = [public_address]

    def get_block(self):
        pass


    # 转账交易
    def transfer(self, from_privatekey, to_address, amount):
        from_address = Account.privateKeyToAccount(from_privatekey, self.hrp).address
        nonce = self.platon.getTransactionCount(from_address)
        transaction_dict = {
            "to": to_address,
            "gasPrice": self.web3.eth.gasPrice,
            "gas": 21000,
            "nonce": nonce,
            "data": '',
            "chainId": self.chain_id,
            "value": amount,
        }
        signedTransactionDict = self.web3.platon.account.signTransaction(
            transaction_dict, from_privatekey
        )
        data = signedTransactionDict.rawTransaction
        result = HexBytes(self.platon.sendRawTransaction(data)).hex()
        result = self.platon.waitForTransactionReceipt(result)
        logger.info(f'transfer result = {result}')
        return result

    # 锁仓交易
    def restricting(self, from_private_key, to_address, restricting_plan):
        # ppos.need_analyze = False
        result = self.ppos.createRestrictingPlan(to_address, restricting_plan, from_private_key)
        logger.info(f"restricting result = {result['code']}")
        return result

    # 创建质押
    def staking(self, staking_private_key, balance_type, node_url, amount=10 ** 18 * 2000000, reward_per=1000):
        w3 = Web3(HTTPProvider(node_url), chain_id=self.chain_id)
        version_info = w3.admin.getProgramVersion()
        version = version_info['Version']
        version_sign = version_info['Sign']
        node_info = w3.admin.nodeInfo
        node_id = node_info['id']
        bls_pubkey = node_info['blsPubKey']
        bls_proof = w3.admin.getSchnorrNIZKProve()
        benifit_address = Account.privateKeyToAccount(staking_private_key, self.hrp).address
        result = self.ppos.createStaking(balance_type, benifit_address, node_id, 'external_id', 'node_name', 'website',
                                         'details',
                                         amount, version, version_sign, bls_pubkey, bls_proof, staking_private_key,
                                         reward_per)
        logger.info(f"staking result = {result['code']}, {result}")
        return result

    # 增持质押
    def increase_staking(self, staking_private_key, node_id, balance_type, amount=10 ** 18 * 100):
        result = self.ppos.increaseStaking(balance_type, node_id, amount, staking_private_key)
        logger.info(f"incress staking result = {result['code']}, {result}")
        return result

    # 修改质押信息
    def edit_staking(self, staking_private_key, node_id, benifit_address=None, external_id=None, node_name=None,
                     website=None,
                     details=None, reward_per=None):
        result = self.ppos.editCandidate(staking_private_key, node_id, benifit_address, external_id, node_name, website,
                                         details,
                                         reward_per)
        logger.info(f"edit staking result = {result['code']}, {result}")
        return result

    # 解除质押
    def withdrew_staking(self, staking_private_key, node_id):
        result = self.ppos.withdrewStaking(node_id, staking_private_key)
        logger.info(f"withdrew staking result = {result['code']}, {result}")
        return result

    # 查询质押信息
    def get_candidate_info(self, node_id):
        result = self.ppos.getCandidateInfo(node_id)
        logger.info(f"get candidate info = {result['Code']}, {result}")

    # 创建委托
    def delegate(self, delegation_private_key, node_id, balance_type, amount=10 * 10 ** 18):
        result = self.ppos.delegate(balance_type, node_id, amount, delegation_private_key)
        logger.info(f"delegate result = {result['code']}, {result}")
        return result

    # 解除委托
    def undelegate(self, delegation_private_key, node_id, block_number, amount=1 * 10 ** 18):
        result = self.ppos.withdrewDelegate(block_number, node_id, amount, delegation_private_key)
        logger.info(f"undelegate result = {result['code']}, {result}")
        return result

    # 获取可委托节点列表
    def get_delegable_nodes(self, cdf_account):
        result = self.ppos.getCandidateList()
        delegable_nodes = [i for i in result['Ret'] if i['StakingAddress'] != cdf_account]
        result['Ret'] = delegable_nodes
        logger.info(f"get delegable nodes = {result['Code']}, {result}")
        return result

    # 查询委托信息
    def get_delegate_list(self, delegation_address):
        result = self.ppos.getRelatedListByDelAddr(delegation_address)
        logger.info(f"get delegate list = {result['Code']}, {result}")
        return result

    # 获取账户对某个节点的委托信息
    def get_delegate_list_for_node(self, address, node_id):
        delegated_list = []
        result = self.get_delegate_list(address)
        if result['Code'] == 0:
            for delegated_info in result['Ret']:
                if delegated_info['NodeId'] is node_id:
                    delegated_list.append(delegated_info)
            if delegated_list:
                result['Ret'] = delegated_list
            else:
                result = {'Code': 301203, 'Ret': 'Retreiving delegation related mapping failed:RelatedList info is not found'}
        logger.info(f"get delegated list for node = {result['Code']}, {result}")
        return result

    # 获取账户对某个节点的委托详情
    def get_delegate_info(self, address, node_id, block_number):
        result = self.ppos.getDelegateInfo(block_number, address, node_id)
        logger.info(f"get delegated info = {result['Code']}, {result}")
        return result

    # 领取委托分红
    def withdraw_delegate_reward(self, delegate_private_key):
        result = self.ppos.withdrawDelegateReward(delegate_private_key)
        logger.info(f"withdraw delegate result = {result['code']}, {result}")
        return result

    # 创建升级提案
    def version_proposal(self, node_private_key, node_id, upgrade_version, voting_rounds):
        result = self.pip.submitVersion(node_id, str(time.time()), upgrade_version, voting_rounds, node_private_key,
                                        self.tx_cfg)
        logger.info(f"version proposal result = {result['code']}, {result}")
        return result

    # 创建文本提案
    def text_proposal(self, node_private_key, node_id):
        result = self.pip.submitText(node_id, str(time.time()), node_private_key, self.tx_cfg)
        logger.info(f"text proposal result = {result['code']}, {result}")
        return result

    # 查询提案列表
    def get_proposal_list(self):
        result = self.pip.listProposal()
        logger.info(f"proposal list = {result['Code']}, {result}")
        return result

    # 提案投票
    def vote(self, node_private_key, node_url, proposal_id, vote_type):
        w3 = Web3(HTTPProvider(node_url), chain_id=self.chain_id)
        program_version = w3.admin.getProgramVersion()['Version']
        version_sign = w3.admin.getProgramVersion()['Sign']
        node_id = w3.admin.nodeInfo['id']
        # proposal_id = w3.pip.listProposal().get('Ret')[0].get('ProposalID')
        # assert proposal_id != ''
        logger.info(f'vote node: {node_url}, {node_id}')
        result = self.pip.vote(node_id, proposal_id, vote_type, program_version, version_sign, node_private_key)
        logger.info(f"vote result = {result['code']}, {result}")
        return result

    # 版本声明
    def declare_version(self, node_private_key, node_url):
        w3 = Web3(HTTPProvider(node_url), chain_id=self.chain_id)
        node_id = w3.admin.nodeInfo['id']
        program_version = w3.admin.getProgramVersion()['Version']
        version_sign = w3.admin.getProgramVersion()['Sign']
        result = self.pip.declareVersion(node_id, program_version, version_sign, node_private_key)
        logger.info(f"declare version result = {result['code']}, {result}")
        return result

    # 获取当前版本号
    def get_version(self):
        result = self.pip.getActiveVersion()
        logger.info(f'chain version = {result}')

    # 等待块高
    def wait_block(self, block_number):
        current_block = self.platon.blockNumber
        end_block = current_block + block_number
        while current_block < end_block:
            logger.info(f'wait block: {current_block} -> {end_block}')
            time.sleep(5)
            current_block = self.platon.blockNumber



if __name__ == '__main__':
    tx = SimpleTx('http://192.168.120.121:6789', 201018)
    address, private_key = 'lat1x84ksjuv2wgc7z0vksd2la7jyu4e469y5t8ves', '91e2830913698ebbd7c85c9dce4da6a96ca2fcd5b9bb9314637f0a99e830012c'
    node_id = '7c31d0e2f716324c9051c322be59dd86194f28ad7b71e3bc3837062708b7207e82bed0d6e24691b9107549787b541e3c917ec7503e0ba3addd1340075188bad6'
    tx.get_delegate_list(address)