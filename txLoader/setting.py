from client_sdk_python import Web3, HTTPProvider, WebsocketProvider

# 链设置
rpc = 'ws://106.13.70.56:6791'
# rpc = 'http://192.168.120.121:6789'
chain_id = 101
web3 = Web3(WebsocketProvider(rpc), chain_id=chain_id)

# 压测设置
load_threads = 10  # 压测线程数
load_accounts = 10  # 每个线程使用账户数
load_duration = 1800  # 压测时长/s
load_amount = 20000  # 压测账户的初始金额
load_funcs = ['delegate', 'undelegate', 'withdraw_reward']  # 需要压测的请求,从action中选择
load_ratios = [7, 0, 0]  # 压测请求的发送比率
# is_hold_nonce = True  # todo: coding

# 账户设置
main_address, main_private_key = 'lat12ew0apgax2mjq54wah8q05sl5rzryuqdzv6ar2', '776f6e3fd0856e71cb866bee579ceb46d628fbb8b73bf7458a0a445214705bee'
main_nonce = web3.platon.getTransactionCount(main_address)
cdf_address, cdf_private_key = 'lat156qwr6sywr8e0898zxja9lz9gn6cxnveswlwpw', ''

# gas设置
tx_cfg = {"gas": 1000000, "gasPrice": 20000000000}
