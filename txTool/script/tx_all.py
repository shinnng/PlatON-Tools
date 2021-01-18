from txTool.tx_tool import *


# 准备
main_address, main_private_key = 'atp1zkrxx6rf358jcvr7nruhyvr9hxpwv9uncjmns0', 'f51ca759562e1daf9e5302d121f933a8152915d34fcbc27e542baf256b5e4b74'


# **** 交易模块 ****
to_address, to_private_key = create_account()
# 普通交易
transfer(main_private_key, to_address, 20000 * 10 ** 18)
print(f'## Balance: {PLATON.getBalance(to_address)}')
# 锁仓交易
plan = [{'Epoch': 1, 'Amount': 5000 * 10 ** 18}, {'Epoch': 2, 'Amount': 5000 * 10 ** 18}, {'Epoch': 4, 'Amount': 10000 * 10 ** 18}]
create_restricting_plan(main_private_key, to_address, plan)
print(f'## Restricting: {PPOS.getRestrictingInfo(to_address)}')


# **** 质押模块 ****
node_url = 'http://192.168.120.122:6790'
node_id = 'd80caefe38ec4bfcb8bf99793f63da63662d0acf34c8adeb96ab89a3c6b96b4cf862d405febfa708d28f64895e755e1f60c2821124915f369746a78834a8b906'
bls_pubkey = '953b551558c581a12d73d0d2bdad1f05cc4a5cbf9c24925a7b2f333100f74d3bb2fa609d98c7836e32286b2e9f482908b4a7292cc13f6c85718f0e6bcab770594d60f47372341634d2d4b3abcf10f26bef2282091d410c59bdde5ea8d872a393'
staking_address, staking_private_key = create_account()
# 创建质押
transfer(main_private_key, staking_address, 20000 * 10 ** 18)
plan = [{'Epoch': 10, 'Amount': 5000 * 10 ** 18},
        {'Epoch': 20, 'Amount': 5000 * 10 ** 18},
        {'Epoch': 40, 'Amount': 10000 * 10 ** 18}]
create_restricting_plan(main_private_key, staking_address, plan)
create_staking(staking_private_key, 1, node_url, 10000 * 10 ** 18, 1000)
# 增持质押
transfer(main_private_key, staking_address, 20 * 10 ** 18)
plan = [{'Epoch': 1, 'Amount': 20 * 10 ** 18}]
create_restricting_plan(main_private_key, staking_address, plan)
increase_staking(staking_private_key, node_id, 0, 10 * 10 ** 18)
# 修改质押信息
edit_staking(staking_private_key, node_id, external_id='shinnng')
# 解除质押
# wait_block(40 * 4 * 2)      # 等待2个结算周期
# withdrew_staking(staking_private_key, node_id)


# **** 委托模块 ****
node_id = '7c31d0e2f716324c9051c322be59dd86194f28ad7b71e3bc3837062708b7207e82bed0d6e24691b9107549787b541e3c917ec7503e0ba3addd1340075188bad6'
delegation_address, delegation_private_key = create_account()
# 创建委托
transfer(main_private_key, delegation_address, 30 * 10 ** 18)
plan = [{'Epoch': 1, 'Amount': 80 * 10 ** 18}]
create_restricting_plan(main_private_key, delegation_address, plan)
delegation(delegation_private_key, node_id, 1, 20 * 10 ** 18)
# 领取委托分红
withdraw_delegate_reward(delegation_private_key)
# 撤销委托
undelegation(delegation_private_key, node_id, 10 * 10 ** 18)



# # **** 治理模块 ****
# upgrade_version = 4096
# upgrade_voting_rounds = 5
# # 升级提案
# staking_private_key = '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'
# node_id = '50b6d2f6490040ac0813d0aa0042d6020b0e537d5922805b00de7180bbdb29fca4877fdbf2d2dcd570b8ac9a904c02c69a60c9089239bfff04e0252886ef1158'
# create_version_proposal(staking_private_key, node_id, upgrade_version, upgrade_voting_rounds)
# # 提案投票
# proposals = get_proposal_list()
# proposal_id = proposals['Ret']['PIPID']
# node_list = [('http://192.168.120.121:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://192.168.120.122:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://192.168.120.123:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://192.168.120.124:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ]
# for node_url, private_key in node_list:
#     try:
#         version_proposal_vote(private_key, node_url, proposal_id, 1)
#     except Exception as e:
#         print(f'ERROR: {node_url}, {e}')
# # 版本声明
# node_list = [('http://192.168.120.121:6790', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://192.168.120.122:6790', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://192.168.120.123:6790', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://192.168.120.124:6790', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ]
# for node_url, private_key in node_list:
#     declear_version(private_key, node_url)


# **** 调试信息 ****
# print(PLATON.blockNumber)
# print(PLATON.getBalance('atx1h0ssa942rrwy7yt8m4tjcsvpkr5z5qhmwx55av'))
# print(PLATON.gasPrice)
# print(PPOS.getRestrictingInfo('atx1h0ssa942rrwy7yt8m4tjcsvpkr5z5qhmwx55av'))
# print(PLATON.getTransactionCount('atx1zkrxx6rf358jcvr7nruhyvr9hxpwv9unj58er9'))
# print(PLATON.waitForTransactionReceipt('0xda81aab7e6d9f5188081fbd281fd0eaaebef1f1be03ff2c98fd1f76c36c16ec5'))
# print(PLATON.getCode('atx1rdlcxzxk88e7k7mm0w93ald07g52l6pw97gzzz'))
# print(PPOS.getValidatorList())
# print(PPOS.getVerifierList())
# print(PPOS.getCandidateList())
# print(ppos.getCandidateInfo('bc9dabae54a13202ec765c1537c57b9f6659161596eae7c0344a606e9396c63c96a2a76aadc320100e9a56c5acdb8faddfb61733bddeff7b9f261ac54a46d775'))
# print(PIP.listProposal())
# print(pip.getProposal('0x9552914c57933ad207d2c028cf71445de40b99f3b088155f31f07bdc4ddab2e2')['Ret']['ActiveBlock'])
# print(pip.getAccuVerifiersCount('0x7991b9bb943c0fc67df975975e34602ca501610b31ea842079137c59be5e6b0d', PLATON.getBlock(PLATON.blockNumber)['hash'].hex()))
# print(PIP.getTallyResult('0x15e460705e953944b5523b4b26413d94d9ef9ef88e50e1911bf4e4f0ba4897a7'))
# print(PIP.getTallyResult('0x76c6f1d3af082174973da06c670b25095dcc6d5596488d5300fded83dd2b978a'))
# print(PIP.getActiveVersion())