from simple_tx import SimpleTx
from random import uniform
import datetime, time

# 准备
# rpc = 'http://192.168.120.141:6789'
# rpc = 'http://10.1.1.51:7789'   # alaya
# chain_id = 201018
rpc = 'http://10.1.1.51:6789'   # platon
chain_id = 210423
hrp = 'lat'
# main_address, main_private_key = 'atp1cy2uat0eukfrxv897s5s8lnljfka5ewjj943gf', '3a4130e4abb887a296eb38c15bbd83253ab09492a505b10a54b008b7dcc1668'
# main_address, main_private_key = 'atp15mjtmjrra50v9542pacmpfcynp32tzjre7n9kc', 'c5f398ccf4ffa0dc19ae35bf2d1faf9b5d08f78ba5af0a6d22e46c7c59b8ad89'
main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
cdf_account = 'lat1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrdyjj2v'
tx = SimpleTx(rpc, chain_id, hrp)
w3 = tx.web3
# ============================+++++++++
# account_list = []
# prikey_list = []
# for i in range(27):
#
#     a, b = tx.create_account()
#     account_list.append(a)
#     prikey_list.append(b)
# # print(account_list)
# # print(prikey_list)
# # 转账
# for account in account_list:
#     print(account)
#     tx.transfer(main_private_key, account, 100100 * 10 ** 18)
# # 委托
# delegable_nodes = tx.get_delegable_nodes(cdf_account)
# for prikey in prikey_list:
#     print(prikey)
#     for node in delegable_nodes['Ret']:
#         print(node['NodeId'])
#         temp_amount = uniform(20, 40)
#         tx.delegate(prikey, node['NodeId'], 0, amount=w3.toWei(temp_amount, 'ether'))
# # ===========================================
# # 领取委托
# while datetime.datetime.now().day < 4 and datetime.datetime.now().hour < 18:
#     for i in prikey_list:
#         tx.withdraw_delegate_reward(i)
#     time.sleep(180)
# plan = [{'Epoch': 10, 'Amount': 5000 * 10 ** 18},
#         {'Epoch': 20, 'Amount': 5000 * 10 ** 18},
#         {'Epoch': 40, 'Amount': 10000 * 10 ** 18}]
# plan1 = [{'Epoch': 20, 'Amount': 1000 * 10 ** 18}]
# account = tx.create_account()[0]
# print(account)
account = 'atp1rhfrmz6prtr6ewky3lec3erujrxs8j70jej0ne'
prikey = 'f024d18eba2bf7a17fa7df824275d310e8d6097f644161658870501d6c61e2b2'
# account = 'atp100h2vwxzpwqgll0xa6ku85hm7ap7c07vyz5fva'
# tx.transfer(main_private_key, account, 10000000 * 10 ** 18)
# tx.restricting(prikey, 'atp100h2vwxzpwqgll0xa6ku85hm7ap7c07vyz5fva', plan1)
node_id = '77fffc999d9f9403b65009f1eb27bae65774e2d8ea36f7b20a89f82642a5067557430e6edfe5320bb81c3666a19cf4a5172d6533117d7ebcd0f2c82055499050'
staking_prikey = '690a32ceb7eab4131f7be318c1672d3b9b2dadeacba20b99432a7847c1e926e0'
blockNumber = tx.platon.blockNumber
print(blockNumber)
# list = []
# for i in range(10):
#         account = tx.create_account()
#         list.append(account)
# print(list)
# for i in list:
#         tx.transfer(main_private_key, i[0], 10100 * 10 ** 18)
node_id1 = '09ac1c54b6d4e87465eba8c17b149fc2b0add867f69253230c7ce843970ddbed57d79dac993cf89ca597dfe6bc63935e7429947b71f575a0ad63551c10e4a2ac'
# tx.increase_staking(main_private_key, node_id1, 0, amount=1000 ** 10 ** 18)
# tx.text_proposal(staking_prikey, node_id)
# tx.get_proposal_list()
#################################################################################
# 预计节点年化率计算 W/C * 当前周期的结算周期数 * 100%   新的 节点收益其他计算方式：累计到第n+4个结算周期结算区块节点收益当中的最高收益 减去 累计到第n个结算周期结算区块节点收益
# w_4 = (packreward * 10750 + staking_reward) * 4 * (1-0.7)
# w_4 = (2.7568181162214737e+27 - 2.7249462404552186e+27)/(10 ** 18)
# C_4 = 200000 * 4
# print(f'预计节点年化率：{(w_4/C_4) * 17 * 100} %')
#############################1,先给质押账户转钱；2，再进行节点质押###################################################
node_list = [
                 ('http://10.0.0.11:6789', '71348014a337e6af69de778691926ad45ded92ced6add92d0a1ca89512780365'),
                 ('http://10.0.0.12:6789', '745f7297e90fbc4bf7bc778060780565f62376c49bea7bc9f356f22ba15b987f'),
                 ('http://10.10.8.236:6789','466fc69afcb31e582ef45a96ba349a80472eedcc2898bb2ca638ac79e9dd9428'),
                 ('http://10.0.0.13:6789', 'd637e12e76c93e6a32b072176bddcb5bc72eca99511f58ae16737748b02474cc'),
                 ('http://10.0.0.30:6789', '32983d70ec55e896b722ba028f40342e92b37058e926db5d5678e5ecbd00a5c3'),
                 ('http://10.0.0.15:6789', '4123ebeb3b0ce97dd88c325de630d4673145e0f0d906930a00073d86a924af6e'),
                 ('http://10.0.0.29:6789', '72f1685e1cd2996802351e7bcc2d5f036a3229b2496bd97997230162170b7f0c'),
                 ('http://10.0.0.21:6789', '745d157b488cd9f8b234669174c91ed3ef9790acdb4ff4d145e42f30335c541e'),
                 ('http://10.0.0.28:6789', '7ee3eed846d1a48ffce1d8cbccb382bfa48af97337cb1d8d21dc749bce9e0518'),
                 ('http://10.0.0.27:6789', '195db97290ddf15c1139794eda41c22c4d4c31d8cfa1c3ae1b0271c556bacea5'),
                 ('http://10.0.0.18:6789', 'fba6c4821c556f938a6b93fbd7700e350e975b90498b613bdf3b432896f19cb3'),
                 ('http://10.0.0.24:6789', '184f70bc7ba1cb4eb900654fcfc95063dffe34ab2714e8616c27f194f292b4fd'),
                 ('http://10.10.8.238:6789', '2db653a3f3d691d5ce80bcdf1470f651b6ad639c8e21f5904460398c989a3513'),
                 ('http://10.0.0.26:6789', 'ca6fa21e008f1be74ad568a09c4a780c52695a06f3ea1cefe5097e119570fa76'),
                 ('http://10.0.0.14:6789', '924789383dab659ec8248b9017ec97fed199d3529fb0865a070e50b876f50019'),
                 ('http://10.0.0.25:6789', '89bdbc5d2a85ec38bc53a326ddaab467764f6b2e3e62861e3ed2fa9dd22da074'),
                 ('http://10.0.0.19:7789', '6553364dcc96713dea0e0fc8926a7b142691561c3c227f0935fc70abb62354f2'),
                 ('http://10.10.8.237:6789', '7bd1dfcda68f3df6035005e3281677e791f85f72534ff71a0bb785991a37cd30'),
                 ('http://10.10.8.240:6789', '5830638f7777eccaff1ae84078f97da6bd329bcb35528abb650d9f72c7196a6d'),
                 ('http://10.1.1.51:6789', 'f3a4d85a3111a2a810e33ffd67783201407070a8225c4e6406f509da78b64113'),
                 ('http://10.1.1.52:6789', 'f1cdae699706d3a0f2d3b3d5c0eb2a5557b6a38c1833a92fe71867391101c383'),
                 ('http://10.1.1.53:6789', 'dd2c03b8691c97dbfe6e0e3da4e55bd9555cb679e1bd988b9a66c7d458e78414'),
                 ('http://10.1.1.54:6789', '23764f7368ffc618f2a6be1093d3566aed7b5904bc414520e3473b635b581a9b'),
                 ('http://10.1.1.55:6789', '649f2034af4285a60de1c674e8a512a8acefe8b0ed11d115f3c24dcbf271801b'),
                 ('http://10.1.1.56:6789', '35eb95a91b816a974495c21349f1add4c3b89b8cf1b4e3029651a66fa7e56df8'),
                 ('http://10.1.1.57:6789', '6dc51af31ffd0295ceff4814920008449777820a788db6a1f140173fb2168ad4')
]
# for node_url, staking_prikey1 in node_list:
#         print(node_url)
#         tx.staking(staking_prikey1, 0, node_url, 100000 ** 10 ** 18, 1000)
tx.staking('6dc51af31ffd0295ceff4814920008449777820a788db6a1f140173fb2168ad4', 0, 'http://10.1.1.57:6789', 100000 ** 10 ** 18, 1000)
# tx.transfer(main_private_key, 'atp19yx3ym70jhlnrmau763unjx6usp848u288g5qk', 80000 * 10 ** 18)
# tx.vote('03a4130e4abb887a296eb38c15bbd83253ab09492a505b10a54b008b7dcc1666', 'http://192.168.120.145:6789', '0x077e1c1d1a377f44932b6150240d2ae19861ab2c5f8ad70f7ee56ce192a2aea8', 1)
# tx.pip.submitParam()
# proposal_id = '0x077e1c1d1a377f44932b6150240d2ae19861ab2c5f8ad70f7ee56ce192a2aea8'
# for node_url, staking_prikey1 in node_list:
#         tx.vote(staking_prikey, node_url, proposal_id, 1)



