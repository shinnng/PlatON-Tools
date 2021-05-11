from simple_tx import SimpleTx
from random import uniform
import datetime, time

# 准备
rpc = 'http://192.168.120.141:6789'
# rpc = 'http://10.1.1.51:7789'
chain_id = 201018
main_address, main_private_key = 'atp1cy2uat0eukfrxv897s5s8lnljfka5ewjj943gf', '3a4130e4abb887a296eb38c15bbd83253ab09492a505b10a54b008b7dcc1668'
# main_address, main_private_key = 'atp15mjtmjrra50v9542pacmpfcynp32tzjre7n9kc', 'c5f398ccf4ffa0dc19ae35bf2d1faf9b5d08f78ba5af0a6d22e46c7c59b8ad89'
cdf_account = 'atp1w5gf9pqkdsnurdtuc0azkmunue3jnltfsd6t4t'
tx = SimpleTx(rpc, chain_id)
w3 = tx.web3
# ============================+++++++++
# account_list = []
# prikey_list = []
# for i in range(1000):
#
#     a, b = tx.create_account()
#     account_list.append(a)
#     prikey_list.append(b)
# print(account_list)
# # print(prikey_list)
# # 转账
# for account in account_list:
#     print(account)
#     tx.transfer(main_private_key, account, 100 * 10 ** 18)
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
plan = [{'Epoch': 10, 'Amount': 5000 * 10 ** 18},
        {'Epoch': 20, 'Amount': 5000 * 10 ** 18},
        {'Epoch': 40, 'Amount': 10000 * 10 ** 18}]
plan1 = [{'Epoch': 20, 'Amount': 1000 * 10 ** 18}]
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
tx.get_proposal_list()
#################################################################################
# 预计节点年化率计算 W/C * 当前周期的结算周期数 * 100%   新的 节点收益其他计算方式：累计到第n+4个结算周期结算区块节点收益当中的最高收益 减去 累计到第n个结算周期结算区块节点收益
# w_4 = (packreward * 10750 + staking_reward) * 4 * (1-0.7)
# w_4 = (2.7568181162214737e+27 - 2.7249462404552186e+27)/(10 ** 18)
# C_4 = 200000 * 4
# print(f'预计节点年化率：{(w_4/C_4) * 17 * 100} %')
################################################################################
node_list = [
                 # ('http://10.0.0.11:6789', '7fe5cc8f1c69b7b7e5b75224c7e8caa8db8b9c0d13d666ecd0703bca2409d690'),
                 # ('http://10.0.0.12:6789', 'b61c15829a7684f67ee9cc960eb8c6140b7e3372517aa6180d4150a61e642eb7'),
                 # ('http://10.10.8.236:6789', '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'),
                 # ('http://10.0.0.13:6789', '7f677ee1f931a5eb7b0d8584d631153c1b8725ae1b6efdd9b5ab2e24b567e4d7'),
                 # ('http://10.0.0.30:6789', 'a2b4a7d2a0d118bf87dc9e61ba54b7a9b9ae989715d0ab3f26ade4cb131ba038'),
                 # ('http://10.0.0.15:6789', '9a331ee9886f2c5f01b12cc664d85c3ed7e4dcf6a1f21574690bb4949bb6e24b'),
                 # ('http://10.0.0.29:6789', '7252ca84514f9be82a5afe3afb310e71f001e1bbe8addead526bc397ff92b1f6'),
                 # ('http://10.0.0.21:6789', '7f77176b29e777e7b855e84fc0688acd0a4093fe9d2cd44af59e751013d563d7'),
                 # ('http://10.0.0.28:6789', '04a4bb0ebd5fcc90a0aad99ae943b4a160fa18d615925474b211070fc89d94e4'),
                 # ('http://10.0.0.27:6789', '89f5ccee535c7ad4258724513e5bcfcd37debaf05ccf39ae2442f9b70878a696'),
                 # ('http://10.0.0.18:6789', 'dce1a70c69541d9c28c3e569fe308f55e9538a697a6547191d8530eba60acf28'),
                 # ('http://10.0.0.24:6789', 'b9eb78b6ef82688833677909c0806f505a5397f155301990640b3926ddc24a83'),
                 # ('http://10.10.8.238:6789', '5a38bea58575713a3b5ac9f70070efb73763d4e316ecbc3fc9096f4dd629f564'),
                 # ('http://10.0.0.26:6789', '7e980742f62e5d54d05bad38c3c56268ccf34ff4be6b859d40493c9ebace1ce1'),
                 # ('http://10.0.0.14:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
                 # ('http://10.0.0.25:6789', '66c3de2b9827c604b00140165f952dc8fe591724f8707891ed86bc4f1cc0dc00'),
                 ('http://10.0.0.19:7789', '81132acd872ba593952eb466e2cef64917364a87abe93002e406d0b3776117fe'),
                 ('http://10.10.8.237:6789', '5cf2ba2565cab9288faa3b663618859676b88edf3eecd299b20435bb28d3baa1'),
                 ('http://10.10.8.240:6789', '2c1714ebf5156bae778ba34e23eb4c81dee9acad3aa8dbcfc54943ff58bbe038'),
                 ('http://10.1.1.51:6789', 'e150bb825babbe07c60724719785a3787542b1b18a5cbd87a6e0fe5bd0c71f3f'),
                 ('http://10.1.1.52:6789', '81f644f846f14eb303d9eb3bb1f9b0e0f69cd48c0c8c0148ae48f087e0c77eef'),
                 ('http://10.1.1.53:6789', '57b58af483c233bc91f3ba6da2d641fb230248a4810fe07a58338a6ef161295b'),
                 ('http://10.1.1.54:6789', '82b718d0eeb1dc348018a481f880bb790c9cfa0788487744c83e42a088c9f1e8'),
                 ('http://10.1.1.55:6789', 'fbda4ef667175e0a65c6ea58bf6a6ee396a5ec671c9e1c8a0bfac32c6a7750bf'),
                 ('http://10.1.1.56:6789', 'e8ff6c3f4b547ccf48176afbdb9d35ef21e6f4fb7c9d622f867848d3d875aa62'),
                 ('http://10.1.1.57:6789', 'cdd95ca62c5ca1bf5c5d0212768e2b5576f0cf1812fe6b32da63696ca3c6d318')
                 ]
# for node_url, staking_prikey1 in node_list:
#         print(node_url)
#         tx.staking(staking_prikey1, 0, node_url, 10000 ** 10 ** 18, 1000)
# tx.staking('81132acd872ba593952eb466e2cef64917364a87abe93002e406d0b3776117fe', 0, 'http://10.0.0.19:7789', 10000 ** 10 ** 18, 1000)
# tx.transfer(main_private_key, 'atp19yx3ym70jhlnrmau763unjx6usp848u288g5qk', 80000 * 10 ** 18)
tx.vote('03a4130e4abb887a296eb38c15bbd83253ab09492a505b10a54b008b7dcc1666', 'http://192.168.120.145:6789', '0x077e1c1d1a377f44932b6150240d2ae19861ab2c5f8ad70f7ee56ce192a2aea8', 1)
tx.pip.submitParam()
proposal_id = '0x077e1c1d1a377f44932b6150240d2ae19861ab2c5f8ad70f7ee56ce192a2aea8'
for node_url, staking_prikey1 in node_list:
        tx.vote(staking_prikey, node_url, proposal_id, 1)



