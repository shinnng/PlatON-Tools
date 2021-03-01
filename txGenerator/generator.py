from random import randint, uniform, sample

import click
from client_sdk_python import Web3, HTTPProvider, eth as Eth, ppos as Ppos, admin as Admin, debug as Debug
from hexbytes import HexBytes
from ruamel import yaml

chain_id = 201030
w3_url = 'http://10.1.1.51:6789'
main_account_prikey = 'f51ca759562e1daf9e5302d121f933a8152915d34fcbc27e542baf256b5e4b74'
cdf_account = 'atx1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4xerq62'

w3 = Web3(HTTPProvider(w3_url), chain_id=chain_id)
platon = Eth.Eth(w3)
ppos = Ppos.Ppos(w3)
debug = Debug.Debug(w3)

# init_amount = lambda: w3.toWei(uniform(300, 500), 'ether')


# restricting_epoch = lambda: randint(1, 100)
# staking_amount = lambda: w3.toWei(uniform(2000000, 3000000), 'ether')
# reward_per = lambda: randint(0, 10000)
# delegate_amount = lambda: w3.toWei(uniform(10, 50), 'ether')
# withdrew_delegate_amount = lambda: w3.toWei(uniform(1, 10), 'ether')


#
def create_account():
    account_obj = platon.account.create(net_type=w3.net_type)
    account = {}
    account['address'] = account_obj.address
    account['privatekey'] = bytes(account_obj.privateKey).hex()
    print(f'created account: {account["address"]}')
    return account


def submit_transfer(from_private_key, to_address, amount):
    from_address = platon.account.privateKeyToAccount(from_private_key, w3.net_type).address
    # print(platon.getBalance(from_address))
    nonce = platon.getTransactionCount(from_address)
    transfer_dict = {
        "to": to_address,
        "gasPrice": platon.gasPrice * 2,
        "gas": 21000,
        "nonce": nonce,
        "data": '',
        "chainId": chain_id,
        "value": amount
    }
    signed_transfer_dict = platon.account.signTransaction(
        transfer_dict, from_private_key
    )
    data = signed_transfer_dict.rawTransaction
    tx_hash = HexBytes(platon.sendRawTransaction(data)).hex()
    result = platon.waitForTransactionReceipt(tx_hash)
    print(f'Transfer:{amount}, {from_address}, {to_address}')
    return result


def submit_restricting(from_private_key, to_address, amount, epoch):
    restricting_plan = [{'Epoch': epoch, 'Amount': amount}]
    result = ppos.createRestrictingPlan(to_address, restricting_plan, from_private_key)
    from_address = platon.account.privateKeyToAccount(from_private_key, w3.net_type).address
    print(f'Restricting: {amount}, {epoch}, {from_address}, {to_address}')
    return result


def submit_staking(type: int, w3_url, node_id, staking_private_key, benifit_address, bls_public_key, amount,
                   reward_per):
    """
        type: 0, 1
    """
    s_w3 = Web3(HTTPProvider(w3_url), chain_id=chain_id)
    s_platon = Eth.PlatON(s_w3)
    s_ppos = Ppos.Ppos(s_w3)
    s_admin = Admin.Admin(s_w3)
    program_version = s_admin.getProgramVersion()['Version']
    version_sign = s_admin.getProgramVersion()['Sign']
    bls_proof = s_admin.getSchnorrNIZKProve()
    bls_public_key = bls_public_key
    staking_address = s_platon.account.privateKeyToAccount(staking_private_key, w3.net_type).address
    result = s_ppos.createStaking(type, benifit_address, node_id, 'external', f'node_{randint(0, 100)}',
                                  'www.platon.com', 'details', amount,
                                  program_version,
                                  version_sign, bls_public_key, bls_proof, staking_private_key, reward_per)
    print(f'Staking: {result}, {amount}, {node_id[:5]}, {staking_address}')
    return result


def get_delegable_node():
    candidate_list = ppos.getCandidateList()['Ret']
    delegable_nodes = [i for i in candidate_list if i['StakingAddress'] != cdf_account]
    return delegable_nodes


def submit_delegate(type: int, node_id, delegate_private_key, amount):
    """
        type: 0, 1
    """
    result = ppos.delegate(type, node_id, amount, delegate_private_key)
    print(result)
    delegate_address = platon.account.privateKeyToAccount(delegate_private_key, w3.net_type).address
    print(f'Delegate: {result}, {amount}, {delegate_address} ==> {node_id}')
    return result


def submit_withdrew_delegate(node_id, staking_block_number, amount, delegate_private_key):
    result = ppos.withdrewDelegate(staking_block_number, node_id, amount, delegate_private_key)
    delegate_address = platon.account.privateKeyToAccount(delegate_private_key, w3.net_type).address
    print(f'withdrew_delegate: {result}, {amount}, {delegate_address} ==> {node_id}')


def submit_withdrew_delegate_reward(delegate_private_key):
    result = ppos.withdrawDelegateReward(delegate_private_key)
    delegate_address = platon.account.privateKeyToAccount(delegate_private_key, w3.net_type).address
    print(f'withdrew_delegate_reward: {result}, {delegate_address}')


def submit_withdrew_staking(node_id, staking_private_key):
    result = ppos.withdrewStaking(node_id, staking_private_key)
    staking_address = platon.account.privateKeyToAccount(staking_private_key, w3.net_type).address
    print(f'withdrew_staking: {result}, {staking_address}')


# 指令，使用-h查看帮助
@click.group()
def cli():
    pass


@cli.command()
@click.option('--number', type=int, prompt='account count')
@click.option('--tofile', type=click.Path(), prompt='save to file')
def makeaccount(number, tofile):
    account_list = []
    for i in range(number):
        account = create_account()
        account_list.append(account)
    with open(tofile, 'a') as f:
        yaml.dump(account_list, f, Dumper=yaml.RoundTripDumper)


@cli.command()
@click.option('--account', type=click.Path(exists=True), prompt='')
@click.option('--amount', type=float)
@click.option('--privatekey', type=str, prompt='')
def transfer(account, amount, privatekey):
    with open(account, 'r') as f:
        accounts = yaml.safe_load(f)
    amount_tmp = amount
    for account in accounts:
        if not amount:
            amount_tmp = uniform(80, 100)
        submit_transfer(privatekey, account['address'], w3.toWei(amount_tmp, 'ether'))


@cli.command()
@click.option('--account', type=click.Path(exists=True), prompt='')
@click.option('--amount', type=float, default=100)
@click.option('--epoch', type=int)
@click.option('--privatekey', type=str, prompt='')
def restricting(account, amount, epoch, privatekey):
    with open(account, 'r') as f:
        accounts = yaml.safe_load(f)
    amount = w3.toWei(amount, 'ether')
    epoch_tmp = epoch
    for account in accounts:
        if not epoch:
            epoch_tmp = randint(1, 10)
        submit_restricting(privatekey, account['address'], amount, epoch_tmp)


@cli.command()
@click.option('--config', type=click.Path(exists=True), prompt='')
def staking(config):
    with open(config, encoding='utf-8') as f:
        staking_info_list = yaml.safe_load(f)
    for staking_info in staking_info_list:
        w3_url = staking_info['w3_url']
        node_id = staking_info['node_id']
        type = staking_info['staking_type']
        staking_private_key = staking_info['staking_private_key']
        amount = Web3.toWei(staking_info['staking_amount'], 'ether')
        benifit_address = staking_info['benifit_address']
        bls_public_key = staking_info['bls_public_key']
        reward_per = staking_info['reward_per']
        submit_staking(type, w3_url, node_id, staking_private_key, benifit_address, bls_public_key, amount, reward_per)


@cli.command()
@click.option('--account', type=click.Path(exists=True), prompt='')
@click.option('--amount', type=float)
@click.option('--type', type=int)
def delegate(account, type, amount):
    delegable_nodes = get_delegable_node()
    length = len(delegable_nodes)
    num = 3 if 3 < length else length
    with open(account, 'r') as f:
        accounts = yaml.safe_load(f)
    amount_tmp = amount
    for account in accounts:
        samlpe_nodes = sample(delegable_nodes, num)
        for node in samlpe_nodes:
            if not amount:
                amount_tmp = uniform(50, 80)
            submit_delegate(type, node['NodeId'], account['privatekey'], w3.toWei(amount_tmp, 'ether'))


@cli.command()
@click.option('--account', type=click.Path(exists=True), prompt='test')
def withdrew_delegate_reward(account):
    with open(account, 'r') as f:
        accounts = yaml.safe_load(f)
    for account in accounts:
        submit_withdrew_delegate_reward(account['privatekey'])


@cli.command()
@click.option('--account', type=click.Path(exists=True), prompt='test')
@click.option('--amount', type=int)
def withdrew_delegate(account, amount):
    with open(account, 'r') as f:
        accounts = yaml.safe_load(f)
    amount_tmp = amount
    for account in accounts:
        delegate_list = ppos.getRelatedListByDelAddr(account['address'])['Ret']
        delegate_info = sample(delegate_list, 1)[0]
        staking_block_number = delegate_info['StakingBlockNum']
        node_id = delegate_info['NodeId']
        if not amount:
            amount_tmp = uniform(10, 50)
        submit_withdrew_delegate(node_id, staking_block_number, w3.toWei(amount_tmp, 'ether'), account['privatekey'])


@cli.command()
@click.option('--config', type=click.Path(exists=True), prompt='')
def withdrew_staking(config):
    with open(config, encoding='utf-8') as f:
        staking_info_list = yaml.safe_load(f)
    for staking_info in staking_info_list:
        node_id = staking_info['node_id']
        staking_private_key = staking_info['staking_private_key']
        submit_withdrew_staking(node_id, staking_private_key)


# 入口
if __name__ == '__main__':
    '''
    TODO：
    1、创建账户
    2、转账
    3、锁仓
    4、质押节点  //余额、锁仓
    6、委托节点  //余额、锁仓  //去除初始验证人
    7、赎回委托  //金额随机  //部分、全部
    8、领取分红
    9、撤销质押
    '''
    cli()
