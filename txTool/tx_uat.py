main_private_key = 'defc69adf94e2b01fcb6e47d50f2880ac864a98447f8b2c3640ce5d6d2600190'

# # **** 交易模块 ****
# from_address, from_private_key = create_account()
# to_address, to_private_key = create_account()
# addr_list = ['atx1w5wtf7fud8xppguaxeg68z4g3qe0p99yq863qr', 'atx1jt7zh76t9xdfnczz7usymwxmmfr9zza79p74jv', 'atx1999r47ahhuc4xhjdhppvgkyw3z03gu765vtx2u',
#  'atx1tuhqwl39xa3lgy5cv732tamxx0efteavk6qys7', 'atx1sh3xncmqdwlafptt9nsc3vv5zzcpufdue0lsua', 'atx1ytmtawyxxt0kd44nx772h9qqk3wl28u89hhsv0',
#  'atx14v68yv0a7a5jphvul2ehm24jt446lq6j2mmwcc', 'atx1ayzxme7s9apmaejvf6n83uk63ldjshv38809va', 'atx1x78f927l260rdp9erk8er3jhp26mfwcpfsm98z',
#  'atx1jxmdq2gxetydthddqqfrlr8mtm44afwhms2mmy', 'atx1xc4nl4s5m583xkcfwq4na32hvs7pz8r4a48q8t', 'atx1enmarze9cu2tzp37g9lg3fqkkkx752d2cm77ku',
#  'atx1g8yqegahap0c5jfxkdezl7nscrn0a0xxydf2ay', 'atx1tx358vuju4qag2mr92nl20552ysyzuhyxz88ke', 'atx177fthwhxecq5dn4m7j7v8hs7xprhcny45psjdf',
#  'atx14gt343vhqs74uesz06m3ugh6gnhzrethjyktgh', 'atx14kfvcwzet5gkxr0ur8057ne5wzhul98qg8r4sn', 'atx1smhd0m7nwkaextuuylf864vhmkl09k53jpg8vs',
#  'atx1cywdp07xr2cjhdcr8pp8vgz7j532epdck59atq', 'atx10pn9uxafqps54zj5r3a7ppfgzzee7w253nuy29', 'atx18r03ct2azfjsktrmndfxdvam58wlupgsnm7pvu',
#  'atx14lnu29vj0aulh3myqethsdq5uvyyuu9uxskgue', 'atx1ggmrtps9knqdhsm5y7pj844ktk4h68cgmqpcrx', 'atx1tyuyylmskkase20zmns7zsv3mw89skn2lwqctz',
#  'atx14tqp8t2f63x9fwgn4xvq26q5ehyrn0rv5lfp24', 'atx1glkegnc2l8mtfuet8x676gjk6s58lj9aa5k2e7', 'atx1ww44fcuk9xtlegfes7quueakcj7upr7h7rzd5x',
#  'atx1kv9gac3mpdzrg2qyrajfjlzq6j3defhrdgh8hs', 'atx1u4fpcvdu2px4kwesug69t70r2053gs7at44f9u', 'atx1xrnu97t2zehuwkyywrkq84n2ns6uyrrn5h8q2l']
# for addr in addr_list:
# transfer(main_private_key, 'atx1h0ssa942rrwy7yt8m4tjcsvpkr5z5qhmwx55av', 200 * 10 ** 18)
# create_hd_account()
# 普通交易
# transfer(main_private_key, 'atx1wz5as9rhsfdfl3n2fymhhfdvfg75c6ndq83xqu', 2100 * 10 ** 18)
# # 锁仓交易
# plan = [{'Epoch': 4, 'Amount': 4000 * 10 ** 18}, {'Epoch': 8, 'Amount': 4000 * 10 ** 18}]
# create_restricting_plan(main_private_key, "atx1wz5as9rhsfdfl3n2fymhhfdvfg75c6ndq83xqu", plan)
#
# print(f'## Balance: {self.platon.getBalance(address)}')
# print(f'## Restricting: {self.ppos.getRestrictingInfo(address)}')

# plan = [{'Epoch': 1, 'Amount': 80 * 10 ** 18}, {'Epoch': 2, 'Amount': 80 * 10 ** 18}]
# create_restricting_plan(private_key, address, plan)
#
# print(f'## Balance: {self.platon.getBalance(address)}')
# print(f'## Restricting: {self.ppos.getRestrictingInfo(address)}')
#
# plan = [{'Epoch': 1, 'Amount': 80 * 10 ** 18}, {'Epoch': 2, 'Amount': 80 * 10 ** 18}]
# create_restricting_plan(private_key, address, plan)
#
# print(f'## Balance: {self.platon.getBalance(address)}')
# print(f'## Restricting: {self.ppos.getRestrictingInfo(address)}')
# # **** 经济模型模块 ****
# node_id = 'd80caefe38ec4bfcb8bf99793f63da63662d0acf34c8adeb96ab89a3c6b96b4cf862d405febfa708d28f64895e755e1f60c2821124915f369746a78834a8b906'
# bls_pubkey = '61f437e6bdc2d61a45bb8a4df0dbdd5351075e89c575dc35647590f79f8d8d49e159d7a30a6c19166b249d26254d230b0cda80ff166484c47bc32c6e2a13fc5b9bf891d79843d3462ee5057ad34852c48cf73a2adbecab970b2a3dff0772e519'
# staking_address, staking_private_key = 'atp124kpacd6pnexkpx8kt5m4ttvmvskh9nq2rm9uu', '92ed41950614a755426f0d9b1d7a37fc917972e7dafd0880548218360c71f724'
# staking_address, staking_private_key = create_account()
# # delegation_address, delegation_private_key = 'atx16g303js6tushq236fhv5cmr8tw272cg9279tcl', 'b854c86a25498ce21035d3fabc7dbe784b4288ad3bd9580437bd0250014e40c1'
# # # 创建质押
# node_list = [('http://10.0.0.11:6789', '7fe5cc8f1c69b7b7e5b75224c7e8caa8db8b9c0d13d666ecd0703bca2409d690'),
#              ('http://10.0.0.12:6789', 'b61c15829a7684f67ee9cc960eb8c6140b7e3372517aa6180d4150a61e642eb7'),
#              ('http://10.0.0.13:6789', '7f677ee1f931a5eb7b0d8584d631153c1b8725ae1b6efdd9b5ab2e24b567e4d7'),
#              ('http://10.0.0.14:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.15:6789', '9a331ee9886f2c5f01b12cc664d85c3ed7e4dcf6a1f21574690bb4949bb6e24b'),
#              ('http://10.0.0.16:6789', '3a3fbabfddf9934c6ca1395b486db656be9e3a7fc66f7340a6332209432c3575'),
#              ('http://10.0.0.17:6789', '2c892dcaa800bce2ea75da443a87c31a57c6312910fa99fbc31d6d6a70302900'),
#              ('http://10.0.0.18:6789', 'dce1a70c69541d9c28c3e569fe308f55e9538a697a6547191d8530eba60acf28'),
#              ('http://10.0.0.19:6789', '2cc3620a96aceaadfa46e48395ac25265b9a134a8a9de93268adcf3f60ea745b'),
#              ('http://10.0.0.20:6789', '98786b14fc2ceaa30c00031023a5965161cad3a8dd5d941535e372b9632f029d'),
#              ('http://10.0.0.21:6789', '7f77176b29e777e7b855e84fc0688acd0a4093fe9d2cd44af59e751013d563d7'),
#              ('http://10.0.0.22:6789', '9956ba98090f318af998bae835d1ace3c9fdff2f2daae677d6670aaad9951df2'),
#              ('http://10.0.0.23:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.24:6789', 'b9eb78b6ef82688833677909c0806f505a5397f155301990640b3926ddc24a83'),
#              ('http://10.0.0.25:6789', '66c3de2b9827c604b00140165f952dc8fe591724f8707891ed86bc4f1cc0dc00'),
#              ('http://10.0.0.26:6789', '7e980742f62e5d54d05bad38c3c56268ccf34ff4be6b859d40493c9ebace1ce1'),
#              ('http://10.0.0.27:6789', '89f5ccee535c7ad4258724513e5bcfcd37debaf05ccf39ae2442f9b70878a696'),
#              ('http://10.0.0.28:6789', '04a4bb0ebd5fcc90a0aad99ae943b4a160fa18d615925474b211070fc89d94e4'),
#              ('http://10.0.0.29:6789', '7252ca84514f9be82a5afe3afb310e71f001e1bbe8addead526bc397ff92b1f6'),
#              ('http://10.0.0.30:6789', 'a2b4a7d2a0d118bf87dc9e61ba54b7a9b9ae989715d0ab3f26ade4cb131ba038'),
#              ('http://10.0.0.31:6789', 'a4a026cb5c7d10c7ebef0069528e43358b63de2dd707715b566fd177429d66b2'),
#              ('http://10.0.0.32:6789', '7cb35bcebe5900bcdc7ea7fd47486128f4b22b8ecd1595bb47e8f8866b190d17'),
#              ('http://10.0.0.33:6789', '4fe61a44da26bf1a09771f6b26d22a40e03250dc1ef2141208611485f0ea79d1'),
#              ('http://10.1.1.51:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.52:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.53:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.54:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.55:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.56:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.57:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.60:6789', '3f2ed71cba9c15decf008819a3c4d93dd0dffbb7888acb22ea4a0ad4c7bf35e8'),
#              ('http://10.10.8.236:6789', '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'),
#              ('http://10.10.8.237:6789', 'eeeaf73dc70973bf40ee0d70c0ba1b564d47d91a85a15230a1fa49045e0717e7'),
#              ('http://10.10.8.238:6789', '5a38bea58575713a3b5ac9f70070efb73763d4e316ecbc3fc9096f4dd629f564'),
#              ('http://10.10.8.240:6789', '2c00916d6c5a977b7e69125ceafeace1a9d545dd9a5ccd4b2fb16742e70d9cc3'),
#              ]
# for _, staking_private_key in node_list:
#     staking_address = Account.privateKeyToAccount(staking_private_key, self.hrp).address
#     transfer(main_private_key, staking_address, 10 * 10 ** 18)
#     plan = [{'Epoch': 10, 'Amount': 5000 * 10 ** 18},
#             {'Epoch': 20, 'Amount': 5000 * 10 ** 18},
#             {'Epoch': 30, 'Amount': 5000 * 10 ** 18},
#             {'Epoch': 40, 'Amount': 5000 * 10 ** 18}]
#     create_restricting_plan(main_private_key, staking_address, plan)
# print(platon.getBalance(staking_address))
# print(ppos.getRestrictingInfo(staking_address))
# node_list = [('http://10.0.0.11:6789', '7fe5cc8f1c69b7b7e5b75224c7e8caa8db8b9c0d13d666ecd0703bca2409d690'),
#              ('http://10.0.0.12:6789', 'b61c15829a7684f67ee9cc960eb8c6140b7e3372517aa6180d4150a61e642eb7'),
#              ('http://10.0.0.13:6789', '7f677ee1f931a5eb7b0d8584d631153c1b8725ae1b6efdd9b5ab2e24b567e4d7'),
#              ('http://10.0.0.14:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.15:6789', '9a331ee9886f2c5f01b12cc664d85c3ed7e4dcf6a1f21574690bb4949bb6e24b'),
#              ('http://10.0.0.16:6789', '3a3fbabfddf9934c6ca1395b486db656be9e3a7fc66f7340a6332209432c3575'),
#              ('http://10.0.0.17:6789', '2c892dcaa800bce2ea75da443a87c31a57c6312910fa99fbc31d6d6a70302900'),
#              ('http://10.0.0.18:6789', 'dce1a70c69541d9c28c3e569fe308f55e9538a697a6547191d8530eba60acf28'),
#              ('http://10.0.0.19:6789', '2cc3620a96aceaadfa46e48395ac25265b9a134a8a9de93268adcf3f60ea745b'),
#              ('http://10.0.0.20:6789', '98786b14fc2ceaa30c00031023a5965161cad3a8dd5d941535e372b9632f029d'),
#              ('http://10.0.0.21:6789', '7f77176b29e777e7b855e84fc0688acd0a4093fe9d2cd44af59e751013d563d7'),
#              ('http://10.0.0.22:6789', '9956ba98090f318af998bae835d1ace3c9fdff2f2daae677d6670aaad9951df2'),
#              ('http://10.0.0.23:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.24:6789', 'b9eb78b6ef82688833677909c0806f505a5397f155301990640b3926ddc24a83'),
#              ('http://10.0.0.25:6789', '66c3de2b9827c604b00140165f952dc8fe591724f8707891ed86bc4f1cc0dc00'),
#              ('http://10.0.0.26:6789', '7e980742f62e5d54d05bad38c3c56268ccf34ff4be6b859d40493c9ebace1ce1'),
#              ('http://10.0.0.27:6789', '89f5ccee535c7ad4258724513e5bcfcd37debaf05ccf39ae2442f9b70878a696'),
#              ('http://10.0.0.28:6789', '04a4bb0ebd5fcc90a0aad99ae943b4a160fa18d615925474b211070fc89d94e4'),
#              ('http://10.0.0.29:6789', '7252ca84514f9be82a5afe3afb310e71f001e1bbe8addead526bc397ff92b1f6'),
#              ('http://10.0.0.30:6789', 'a2b4a7d2a0d118bf87dc9e61ba54b7a9b9ae989715d0ab3f26ade4cb131ba038'),
#              ('http://10.0.0.31:6789', 'a4a026cb5c7d10c7ebef0069528e43358b63de2dd707715b566fd177429d66b2'),
#              ('http://10.0.0.32:6789', '7cb35bcebe5900bcdc7ea7fd47486128f4b22b8ecd1595bb47e8f8866b190d17'),
#              ('http://10.0.0.33:6789', '4fe61a44da26bf1a09771f6b26d22a40e03250dc1ef2141208611485f0ea79d1'),
#              ('http://10.1.1.51:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.52:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.53:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.54:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.55:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.56:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.57:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.60:6789', '3f2ed71cba9c15decf008819a3c4d93dd0dffbb7888acb22ea4a0ad4c7bf35e8'),
#              ('http://10.10.8.236:6789', '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'),
#              ('http://10.10.8.237:6789', 'eeeaf73dc70973bf40ee0d70c0ba1b564d47d91a85a15230a1fa49045e0717e7'),
#              ('http://10.10.8.238:6789', '5a38bea58575713a3b5ac9f70070efb73763d4e316ecbc3fc9096f4dd629f564'),
#              ('http://10.10.8.240:6789', '2c00916d6c5a977b7e69125ceafeace1a9d545dd9a5ccd4b2fb16742e70d9cc3'),
#              ]
# for node_url, staking_private_key in node_list:
#     create_staking(staking_private_key, 1, node_url, 20000 * 10 ** 18, 1000)
# # 增持质押
# transfer(main_private_key, staking_address, 10 * 10 ** 18)
# increase_staking(staking_private_key, node_id, 10 * 10 ** 18)
# # 修改质押信息
# benifit_address = Account.privateKeyToAccount(staking_private_key, self.hrp).address
# edit_staking(staking_private_key, node_id, external_id='shinnng')
# # 创建委托
# transfer(main_private_key, delegation_address, 11 * 10 ** 18)
# private_keys = ['f7a91ca4305a59ef93bf6f85eaecbdcb9cd5c5fc35c87c539855e4967faff0a0',
#               'b1b59658038c80d8f6f2b1f3d968417e938af6f5ea3c29d01aee4a4fb7f1a26f',
#               '798c9a1a06564f4d9533c3a1d6fb96348b62a92c049d16669b871896c3bcd873',
#               'ae5acd5e594a459bbe3faadc00ac64be79aa93251f0bd0243f05628a14657a2e',
#               '127e0451e60c9c1df551dc9050362ab9ab7deeafa160672857aaf00f2b8c0139',
#               '5d6514d3878eb2b98ae77d7d4cb687e17411f338fac61a5c24fb0e25d3499b45',
#               '7b4a75bd91933c30d15f5aab5ce79cd4f886373d307fa91619f1e145a5f5c622',
#               '4298456cd70c306cb4827f57bb59ec311b22d4694e8b4793344fcd2a96bafa7a',
#               '969502cd2da5aac9eab511c0f85fd544db48e4311f34a2037e8479b9b412f9c0',
#               'd01ccb8952c0107a5c49396bb7915ca6dbc1ad913b5e36370f540b5938f238c3',
#               '3832e25a1f6feb6eb5e8c26c66494c7c9467181a635b8fa38cc51dd040f40bae',
#               '2f98ef83dffae0ee71b9b5d9ad70901a671b6d718e36e8cbab9b9de6d6d76ecd',
#               '80d9a69bff3eb0131c6237365399666a09a6b2c77ac861b858cc7dbf16efbb54',
#               'e4633d9261cf53f5320e5af29273ba3a3e990d042b0f9dae89169db9e66b5a56',
#               '504523e07a4d5c6a2e44fa18df316bfedfe58dedfa5a29c20d7153e70fd99850',
#               'fbef6de59dd738e192dee8efbd96dc8a8432447173bbb835ecca43b39efd4b28',
#               '687e466709fff60a681d58a892532a4673baebcb10f59dc559328611cbb1e41f',
#               'b452ac93e4a65114eae569607460ae7b53a9f64c45c9e675ce79d7022fb2197c',
#               'a0e6c7d073c13df70f8b85a5b9f9bc137a3c75c489f03f1497cc34ae2947d97b',
#               '9085ec2a136adb886990419794528945f1b750fb770bf07e5778a124c6058c83',
#               '3c1d0950c6329ba7376a5e7d06713edd34012947aa95dd78c1954d56e5d5632e',
#               '71108275ade39f514162869f52183b19ce7ba70c9ac8ddccc86113e871fd1c03',
#               '3f2ed71cba9c15decf008819a3c4d93dd0dffbb7888acb22ea4a0ad4c7bf35e8',
#               '3a3fbabfddf9934c6ca1395b486db656be9e3a7fc66f7340a6332209432c3575',
#               '4fe61a44da26bf1a09771f6b26d22a40e03250dc1ef2141208611485f0ea79d1',
#               '7cb35bcebe5900bcdc7ea7fd47486128f4b22b8ecd1595bb47e8f8866b190d17',
#               'a4a026cb5c7d10c7ebef0069528e43358b63de2dd707715b566fd177429d66b2',
#               'c8cfb8fbc397a11dc5b9c3ce61b9498166edd1051abb4c30f61fa948d1cbba0c',
#               'da3b9c8577dd8dbcc67cd5f48a1f73d49b17d6b8d6c8a5b5a7a5b1c21426d072',
#               'f417f4f91fa92708ffa23174b8c1526c81a51d7bbc600825f70280b6b4ada66b']
# node_id = '50b6d2f6490040ac0813d0aa0042d6020b0e537d5922805b00de7180bbdb29fca4877fdbf2d2dcd570b8ac9a904c02c69a60c9089239bfff04e0252886ef1158'
# for private_key in private_keys:
#     delegation(private_key, node_id, 10000 * 10 ** 18)
# # 撤销委托
# amout = random.randint(1, 10)
# undelegation(delegation_private_key, node_id, amout)
# # 领取委托分红
# withdraw_delegate_reward(delegation_private_key)
# # 解除质押
# wait_block(40 * 4 * 2)
# withdrew_staking(staking_private_key, node_id)

# # **** 治理模块 ****
# upgrade_version = 3584
# upgrade_voting_rounds = 10
# # # # 升级提案
# staking_private_key = '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'
# node_id = '50b6d2f6490040ac0813d0aa0042d6020b0e537d5922805b00de7180bbdb29fca4877fdbf2d2dcd570b8ac9a904c02c69a60c9089239bfff04e0252886ef1158'
# create_version_proposal(staking_private_key, node_id, upgrade_version, upgrade_voting_rounds)
# get_proposal_list()
# create_test_proposal(staking_private_key, node_id)
# get_proposal_list()
# # 提案投票
# node_list = [('http://10.0.0.11:6789', '7fe5cc8f1c69b7b7e5b75224c7e8caa8db8b9c0d13d666ecd0703bca2409d690'),
#              ('http://10.0.0.12:6789', 'b61c15829a7684f67ee9cc960eb8c6140b7e3372517aa6180d4150a61e642eb7'),
#              ('http://10.0.0.13:6789', '7f677ee1f931a5eb7b0d8584d631153c1b8725ae1b6efdd9b5ab2e24b567e4d7'),
#              ('http://10.0.0.14:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.15:6789', '9a331ee9886f2c5f01b12cc664d85c3ed7e4dcf6a1f21574690bb4949bb6e24b'),
#              ('http://10.0.0.16:6789', '3a3fbabfddf9934c6ca1395b486db656be9e3a7fc66f7340a6332209432c3575'),
#              ('http://10.0.0.17:6789', '2c892dcaa800bce2ea75da443a87c31a57c6312910fa99fbc31d6d6a70302900'),
#              ('http://10.0.0.18:6789', 'dce1a70c69541d9c28c3e569fe308f55e9538a697a6547191d8530eba60acf28'),
#              ('http://10.0.0.19:6789', '2cc3620a96aceaadfa46e48395ac25265b9a134a8a9de93268adcf3f60ea745b'),
#              ('http://10.0.0.20:6789', '98786b14fc2ceaa30c00031023a5965161cad3a8dd5d941535e372b9632f029d'),
#              ('http://10.0.0.21:6789', '7f77176b29e777e7b855e84fc0688acd0a4093fe9d2cd44af59e751013d563d7'),
#              ('http://10.0.0.22:6789', '9956ba98090f318af998bae835d1ace3c9fdff2f2daae677d6670aaad9951df2'),
#              ('http://10.0.0.23:6789', '971bd2cf5c08841ef7ea08f2a863c4fdfe70bfacaa1ff87800c889a0ecab462a'),
#              ('http://10.0.0.24:6789', 'b9eb78b6ef82688833677909c0806f505a5397f155301990640b3926ddc24a83'),
#              ('http://10.0.0.25:6789', '66c3de2b9827c604b00140165f952dc8fe591724f8707891ed86bc4f1cc0dc00'),
#              ('http://10.0.0.26:6789', '7e980742f62e5d54d05bad38c3c56268ccf34ff4be6b859d40493c9ebace1ce1'),
#              ('http://10.0.0.27:6789', '89f5ccee535c7ad4258724513e5bcfcd37debaf05ccf39ae2442f9b70878a696'),
#              ('http://10.0.0.28:6789', '04a4bb0ebd5fcc90a0aad99ae943b4a160fa18d615925474b211070fc89d94e4'),
#              ('http://10.0.0.29:6789', '7252ca84514f9be82a5afe3afb310e71f001e1bbe8addead526bc397ff92b1f6'),
#              ('http://10.0.0.30:6789', 'a2b4a7d2a0d118bf87dc9e61ba54b7a9b9ae989715d0ab3f26ade4cb131ba038'),
#              ('http://10.0.0.31:6789', 'a4a026cb5c7d10c7ebef0069528e43358b63de2dd707715b566fd177429d66b2'),
#              ('http://10.0.0.32:6789', '7cb35bcebe5900bcdc7ea7fd47486128f4b22b8ecd1595bb47e8f8866b190d17'),
#              ('http://10.0.0.33:6789', '4fe61a44da26bf1a09771f6b26d22a40e03250dc1ef2141208611485f0ea79d1'),
#              ('http://10.1.1.51:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.52:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.53:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.54:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.55:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.56:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.57:6789', '64bc85af4fa0e165a1753b762b1f45017dd66955e2f8eea00333db352198b77e'),
#              ('http://10.1.1.60:6789', '3f2ed71cba9c15decf008819a3c4d93dd0dffbb7888acb22ea4a0ad4c7bf35e8'),
#              ('http://10.10.8.236:6789', '95ebd28147804fda08d6f6cbb690a3650e0415e0474ab9b08ab8d6e3650929cf'),
#              ('http://10.10.8.237:6789', 'eeeaf73dc70973bf40ee0d70c0ba1b564d47d91a85a15230a1fa49045e0717e7'),
#              ('http://10.10.8.238:6789', '5a38bea58575713a3b5ac9f70070efb73763d4e316ecbc3fc9096f4dd629f564'),
#              ('http://10.10.8.240:6789', '2c00916d6c5a977b7e69125ceafeace1a9d545dd9a5ccd4b2fb16742e70d9cc3'),
#              ]
# proposal_id = '0x81c474e16f42abd200138b0f54438793afd545bb733dd3af44844a46f0e0ae44'
# for node_url, private_key in node_list:
#     try:
#         version_proposal_vote(private_key, node_url, proposal_id, 1)
#     except Exception as e:
#         print(f'ERROR: {node_url}, {e}')
# # 查询提案
# get_proposal_list()
# # 版本声明
# node_list = [('http://10.0.0.20:6789', '98786b14fc2ceaa30c00031023a5965161cad3a8dd5d941535e372b9632f029d'),
#              ]
# for node_url, private_key in node_list:
#     print(declear_version(private_key, node_url))
# # **** 调试信息 ****
# print(self.platon.blockNumber)
# print(self.platon.getBalance('atx1h0ssa942rrwy7yt8m4tjcsvpkr5z5qhmwx55av'))
# print(platon.gasPrice)
# print(self.ppos.getRestrictingInfo('atx1h0ssa942rrwy7yt8m4tjcsvpkr5z5qhmwx55av'))
# print(platon.getTransactionCount('atx1zkrxx6rf358jcvr7nruhyvr9hxpwv9unj58er9'))
# print(platon.waitForTransactionReceipt('0xda81aab7e6d9f5188081fbd281fd0eaaebef1f1be03ff2c98fd1f76c36c16ec5'))
# print(platon.getCode('atx1rdlcxzxk88e7k7mm0w93ald07g52l6pw97gzzz'))
# print(self.ppos.getValidatorList())
# print(self.ppos.getVerifierList())
# print(self.ppos.getCandidateList())
# print(ppos.getCandidateInfo('bc9dabae54a13202ec765c1537c57b9f6659161596eae7c0344a606e9396c63c96a2a76aadc320100e9a56c5acdb8faddfb61733bddeff7b9f261ac54a46d775'))
# print(self.pip.listProposal())
# print(pip.getProposal('0x9552914c57933ad207d2c028cf71445de40b99f3b088155f31f07bdc4ddab2e2')['Ret']['ActiveBlock'])
# print(pip.getAccuVerifiersCount('0x7991b9bb943c0fc67df975975e34602ca501610b31ea842079137c59be5e6b0d', self.platon.getBlock(self.platon.blockNumber)['hash'].hex()))
# print(self.pip.getTallyResult('0x15e460705e953944b5523b4b26413d94d9ef9ef88e50e1911bf4e4f0ba4897a7'))
# print(self.pip.getTallyResult('0x76c6f1d3af082174973da06c670b25095dcc6d5596488d5300fded83dd2b978a'))
# print(self.pip.getActiveVersion())