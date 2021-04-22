from client_sdk_python import Web3, HTTPProvider, WebsocketProvider

# 链基础设置
# rpc = 'ws://106.13.70.56:6791'
# provider = WebsocketProvider
# chain_id = 101
# main_address, main_private_key = 'lat12ew0apgax2mjq54wah8q05sl5rzryuqdzv6ar2', '776f6e3fd0856e71cb866bee579ceb46d628fbb8b73bf7458a0a445214705bee'
# cdf_address, cdf_private_key = 'lat156qwr6sywr8e0898zxja9lz9gn6cxnveswlwpw', ''

rpc = 'http://192.168.120.121:6789'
provider = HTTPProvider
chain_id = 100
hrp = 'lat'
main_address, main_private_key = 'lat1rzw6lukpltqn9rk5k59apjrf5vmt2ncv8uvfn7', 'f90fd6808860fe869631d978b0582bb59db6189f7908b578a886d582cb6fccfa'
cdf_address, cdf_private_key = 'lat1kvurep20767ahvrkraglgd9t34w0w2g059pmlx', ''


# 压测设置
load_threads = 1  # 压测线程数
load_accounts = 1  # 每个线程使用账户数
load_duration = 3600 * 24 * 7  # 压测时长/s
load_amount = 200000  # 压测账户的初始金额
load_funcs = ['transfer']  # 需要压测的请求,从action中选择
load_ratios = [1]  # 压测请求的发送比率
# is_hold_nonce = True  # todo: coding


# gas设置
tx_cfg = {"gas": 1000000, "gasPrice": 20000000000}


# 对象初始化
web3 = Web3(provider(rpc), chain_id=chain_id, hrp_type=hrp)
main_nonce = web3.platon.getTransactionCount(main_address)


