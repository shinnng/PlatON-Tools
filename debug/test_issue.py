import time

from web3 import Web3

from simple_tx import SimpleTx


def assert_code(result, code):
    '''
    assert the ErrorCode
    :param result:
    :param code:
    :return:
    '''
    if isinstance(result, int):
        assert result == code, "code error，expect：{}，actually:{}".format(code, result)
    else:
        assert result.get('code') == code or result.get('Code') == code, "code error，expect：{}，actually:{}".format(code, result)

# url = 'http://192.168.16.121:6789'
# tx = SimpleTx(url, 210423, 'lat')
# tx = SimpleTx(url, 201018)
url = 'http://10.1.1.51:7789'
tx = SimpleTx(url, 201018, 'atp')
# print(tx.web3.getAddressHrp)


# main_private_key = 'fdda94655b33fd7f6953f5c4801110ecb2191fe280a0ba97edb8c66af4390363'
#
# with open(r'C:\PlatON\PlatON_code\PlatON_Tools\PlatON-Tools\accounts', 'r') as f1:
#     accounts = f1.readlines()
#     for i in range(0, len(accounts)):
#         accounts[i] = accounts[i].rstrip('\n')
#     for i in accounts:
#         tx.transfer(main_private_key, i, Web3.toWei(2, 'ether'))
# for i in range(1):
#     address, private_key = tx.create_account()
#     print(address)
#     print(private_key)
account = 'atp1zkrxx6rf358jcvr7nruhyvr9hxpwv9uncjmns0'  # 平行测试网最有钱的账户
pri_key = 'f51ca759562e1daf9e5302d121f933a8152915d34fcbc27e542baf256b5e4b74'
#


#零出块：
# node_id = '4f652a67cccdad5d66914f84245b924606e532e4ad53f755a714dc4d6d6c50c778680bdb0688fb920b390c74a8f0e8c5354e4abb5c86a6ac6e46d5fb96f48eed'
# delegate1, private_key = tx.create_account()
# delegate1, private_key = 'atp1fxlcgd6jmaqhl5da4p9l7kstvy7cqcm6t70vm8', '137a7e0daaa13f744c1dd5fce3e231f3515c2d7ec533fa308c8ba2aa409d25bf'
# print('创建账户信息：', delegate1, private_key)   #创建账户信息： atp1fxlcgd6jmaqhl5da4p9l7kstvy7cqcm6t70vm8 137a7e0daaa13f744c1dd5fce3e231f3515c2d7ec533fa308c8ba2aa409d25bf
# balance_befor = tx.platon.getBalance(delegate1)
# print(f'balance_befor={balance_befor}')
# result = tx.transfer(pri_key, delegate1, tx.web3.toWei(30000, 'ether'))
# print(f'result={result}')
# balance_befor = tx.platon.getBalance(delegate1)
# print(f'balance_befor={balance_befor}')
#
# result = tx.delegate(private_key, node_id, 0, tx.web3.toWei(20000, 'ether'))
# assert_code(result, 0)
# balance_befor = tx.platon.getBalance(delegate1)
# print(f'balance_befor={balance_befor}')

# candidatelist = tx.ppos.getCandidateList()
# print(f'candidatelist={candidatelist}')  #candidatelist={'Code': 0, 'Ret': [{'NodeId': '4f652a67cccdad5d66914f84245b924606e532e4ad53f755a714dc4d6d6c50c778680bdb0688fb920b390c74a8f0e8c5354e4abb5c86a6ac6e46d5fb96f48eed', 'BlsPubKey': '4593bc05cac99bdeeaab133d9f0b28166f54494c7e94909b5f38b23bc0e7ac89a026f54380546e1fc4fa874170506309acd635b833663886d5127a2ba6168066e11e630a058ca643e4b3a555e46207c2dd4f4d02c18683ef69b813dbb6801799', 'StakingAddress': 'atp1xp4gc4cpd5udnpu8m62acww4s9slj4shlcxlc3', 'BenefitAddress': 'atp1xp4gc4cpd5udnpu8m62acww4s9slj4shlcxlc3', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3495, 'Shares': 40000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 1, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x43c33c1937564800000', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '50b6d2f6490040ac0813d0aa0042d6020b0e537d5922805b00de7180bbdb29fca4877fdbf2d2dcd570b8ac9a904c02c69a60c9089239bfff04e0252886ef1158', 'BlsPubKey': 'fa3f659d12a71b22bf9b9388290fdc733c1c980fef2e3d7a53c38c2164c2206fbf42c831434291e80b4b0b837e6091003277a8abfb4168e24885625dbae6e3f140cd45d6735d22069c13f0d8f668d2fb206c3d6349816c890cda1f6525f4d610', 'StakingAddress': 'atp1aff2klzdu65p357n9arsc08txt8yqf3ehzmef9', 'BenefitAddress': 'atp1aff2klzdu65p357n9arsc08txt8yqf3ehzmef9', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3502, 'Shares': 20007000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 1, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x6124fee993bc0000', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '104005f1bb2cefa6059be68d8f7b6dd0ed7b325688c88c6d03be8df471e5979b3d45157835cc2795566855392eb77274b61b3197f3dba129350cd2f61b6f9a0a', 'BlsPubKey': '54e7e96e67b50f1d7d8967df7b8504e2f11ce1ac095289e52a752a65ee57343de2f4f917120ada9c374e742e0af9ec119f8f36994904f1da6ce708df5d7c2eea27f21136f0e69b5668175303efd35ad6e5033d0056ce87027e5f7cb9b8f6c60b', 'StakingAddress': 'atp1gv2ndhhp9dkskyvfkh4yn9gpfwrw6jwqnpz800', 'BenefitAddress': 'atp1gv2ndhhp9dkskyvfkh4yn9gpfwrw6jwqnpz800', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3498, 'Shares': 20005000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 1, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x4563918244f40000', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'ab4ad6c878bd0dd4ef1acda8866b44a69a361571169656eb05c71348bee4f120b22d2dce7e005fce0cffd2a303b0aec31cbed98fea1eb62ac0c580c8d5ed320f', 'BlsPubKey': '34aaf549ecc9c66c749321c2c2468df50849401baf41e3a73ee5502463d631b93a95ab0fbe7076dc6fe3383df594e505bb058510df84617d2b54330cb2005e937761f43e59702908c0f9945f9131996685889735c6cb251ea2018ab51e1bff90', 'StakingAddress': 'atp12mmuna05xrz3j98kc0xma7svmqa43ypmmzngtv', 'BenefitAddress': 'atp12mmuna05xrz3j98kc0xma7svmqa43ypmmzngtv', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3505, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'e22443bf4ce6df86f8e80a2344fde41d9eee5f5b1519018dbc80db4fa1b4a667c9d57a20e3ad052fbb056cb973c71666d495697ef55e7eefb7f6ac40ae890cbf', 'BlsPubKey': '639fcf4b476c576575bdce0f1e613767bab567e0911f22832a0be6f6919d9ef7caf7c9815b210881de7f1daf0b533f14ade9a88c14c68114d4186380e288bc91431ca2b7014ff036f504afc5afa787ef722b54c5876a15ce69d7f69e7dd8b089', 'StakingAddress': 'atp1r5mj72gwqy6euud6qgu4ynuqllwey8q440afse', 'BenefitAddress': 'atp1r5mj72gwqy6euud6qgu4ynuqllwey8q440afse', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3508, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '11eab80256df34cff9c5f72ad6433cddd5adf064308c20e5465187905facb6915d7b4c0e28b0b6f0d66db02b36ed3247a73bb5c7384cd1a5dd0458e7c3ddbad5', 'BlsPubKey': '8f35932c70ff747d92094094737fede64bef57f7aaaca64c437bc660bb6e1c0691f05f8839def8deb854d8f5881c8007080e4adb2cc68c01380be2942376223cf81f1e3f3ff67003967bb8c8b3c8f50fe9b753aeea0c63d17c71ea3b05332282', 'StakingAddress': 'atp1dxwpanvuwngh0j3faueptg2k8r8vj4kks93qmc', 'BenefitAddress': 'atp1dxwpanvuwngh0j3faueptg2k8r8vj4kks93qmc', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3512, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '13ffe2d815e71eaa00295406953b6c612aeeee10d02de1cb46d73e39bda6075cabfabc3e430522d9139a0721449bd1c0ef084c2f6ed098b5ae8e693b1fed3699', 'BlsPubKey': 'a5807ca85b4f25b05c2a1cd1a270852a289ea022f81bac7e9a929377ac64ceb7ccd4fccb61e0053bb485f6d91708c2085f8dc4fc0c177883b2ba8604223a81b4cf6ea0e36774761bb46f69198770e9610d11571280a8d5407dd6f5c765b8df0c', 'StakingAddress': 'atp1824t4qssauqzrgnw8au8zhdsxej4vtrs26xmjr', 'BenefitAddress': 'atp1824t4qssauqzrgnw8au8zhdsxej4vtrs26xmjr', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3515, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '0e24ed1691cca1431d0bf77a8ab5f065bc7bfe53bf212090b6675c91fc5db5ffc94605e4f1e5d9bc7f5e6892304fcc5e910405c5f8e0a773954f19df14e71bcd', 'BlsPubKey': '1441595ce7e9a51b5649478c952470b2b42e8f4521e7348ff1bd504e0bc2efb5157ec38f6bdb2336147b0cc371704b0936f192f58145fcf69c49a5a6bbc8d0c6980e60ffd3689a2b0957c227b779a8f34cb6054147c67a529d77d11d0113d482', 'StakingAddress': 'atp1pqa4x33638je9a22u02r4dgfstwft3f8nufpck', 'BenefitAddress': 'atp1pqa4x33638je9a22u02r4dgfstwft3f8nufpck', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3518, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'd72c276c0c4e2dec1b6259090033052da0e04395f2278350f93202c6c9e6263047e944a935ffb6221dcc38ce43f880e8ca533340abacf7e75c981e6acdafc9ed', 'BlsPubKey': 'ea4aa00c52bc364b4e626cb52ed974fafbf63fbf6222ac136ae91b245f680793f886442f41de9579aadcdbfe3324851448bfe069ce5362d7d96f2b2c9318cb80ebe39c7c7f29d660fc075806234e3783b42dc90621e3a65260551ec928494298', 'StakingAddress': 'atp1xjhv7e5tdcp054qsyy580lcp5lja4nqawe8sht', 'BenefitAddress': 'atp1xjhv7e5tdcp054qsyy580lcp5lja4nqawe8sht', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3521, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '6b548df6de75a051a4b4ca3c0921fff8103964c0758b26784bf3f77e0244f0facd01f6b92035a5c652ab4751a3cd5dd2deceb36be7e6458f9db7331b6962201b', 'BlsPubKey': '92a3c04fb7ed2bbdd3199edc37c47176f9369ab9314974ca8eacbbfc1b1e464a684da348c79a46d685f6e7319f2328090dd562e9f84097f15a1b19ffa86aefa598a76ebd7d2cdc5cbf9e78f1db3bf7591556eb1bc8f27d542015cfa1cdb38a83', 'StakingAddress': 'atp10ekvmavx4zvn6ruvljsu8wlpys0dgzyvmw0g6r', 'BenefitAddress': 'atp10ekvmavx4zvn6ruvljsu8wlpys0dgzyvmw0g6r', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3524, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '917bdb55a08870c608f9307e76d7a789c78b3e7fc3fe41121122ab00fb46611c9ec6a01101ea29aed7f0a61751f1587e3081542d6e1bb2040a4d52c442023f22', 'BlsPubKey': '6fc88ce45b492c0437c1b231b6c7cb080d3ba5cab180242250697b1663901608a471b47b38cba93e7e67bca6b1e83206e93e0fd06d6170647f74726f356c31e3216ddb30d6f80c99ef42b15256469b0773fb4fc2bacbf79a28d9ad19f4526a0e', 'StakingAddress': 'atp1dju8fs3gf4cw7s0325ndlgm63f34czz3v85urr', 'BenefitAddress': 'atp1dju8fs3gf4cw7s0325ndlgm63f34czz3v85urr', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3527, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '13b849fcf7036a5f804018df9f4ff3c1b870ecbbdd1169539e5ed35efc5e0b88fcb391f19d7ae7499e3c1be7f51103d9e943bcaceb26f263f4b49f5f2095c02e', 'BlsPubKey': 'd7573cda21ab43a4025236442d623097b0e3d558420b539ab7303a6c6903a969256473e5298d7f5ddaaacea5351a6f097f4927656ec69ba3fb94c278ddc929aa0a663319e30c714bec2c49c35f40aac6b6728d6a27a78443436ad61fc84a7908', 'StakingAddress': 'atp1qzh8s2n97988m42lk9ex06r9sgz58jrg6th7km', 'BenefitAddress': 'atp1qzh8s2n97988m42lk9ex06r9sgz58jrg6th7km', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3531, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'a4cc62229b8d86bda71447f010cc3d28484092fbbddcdcc90327ff0854471f255ba65a4331655be5c72f5e1cd39431a96966512482d8bf2e0b1995ec9d11bb50', 'BlsPubKey': '556497429d98cf61e3d854f7eaaf6fd21e633b475d57277bfb78697b7ab6a8db2ba7c321eedfd6777c9a71c8adba880df3c10a4bd26fefc82f68c32043a79ceff1176e45f2d7783c0aa738aa4cbbcf6072fa3fd695262ac032437999bce71c04', 'StakingAddress': 'atp1l2vydj045n3udaf6lrswpl8qyycx26h0pcyzlk', 'BenefitAddress': 'atp1l2vydj045n3udaf6lrswpl8qyycx26h0pcyzlk', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3535, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '9f04a7e612543f55fd5fcd3e69845dd6bfb5c7b6408110954a1901ff2c23023cd889a1f01058327e9007b1d9e180b45e94f40cf1831083046929dfe4f4c1584e', 'BlsPubKey': '2ef14be7b7be4e791ee1ce3ff0f50ab4c0b41930f9e40754180a65b28e3636890be19476716423ef1fec6620dbd1690d949dda8035e7cbba6703a0ebf9243ebd584d688e47d465a92e6629ad2688a7211ef911830ef70fdc65a01762a01f7003', 'StakingAddress': 'atp1gyw0kz2ujw2w9ayydufv0rs9a22j2sxef00gyp', 'BenefitAddress': 'atp1gyw0kz2ujw2w9ayydufv0rs9a22j2sxef00gyp', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3539, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '9678453e766fb9573017d33d8fd6d7c60b622a56bff7c775c47045be86b886a7ea0aa8eddabd3a7aeaafcb01cee264adcafbba9ea4a78f5aa302fc18ccb60dba', 'BlsPubKey': '5cd5de19b200d20f51c6928ec9768572ff7e518267658a4ac5ef82bb5dc316b8ed680d5763e800a39a7ecd4180765013144fad6c1e04831f9a93bf42b3c6715212c1efd37f5942e2b6a5d2cb027723b7168600f37bb87cb7183bf5754e225795', 'StakingAddress': 'atp103hwzlzlurq4qx4kemy9t8n0s0qtxus9ckx3x6', 'BenefitAddress': 'atp103hwzlzlurq4qx4kemy9t8n0s0qtxus9ckx3x6', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3543, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '0bd7ee8d75ae470303a382ad4c4def91587508389127c3b3038b690c7e57480de78b3f5c0550f3049b17e66fde485e258dd1c372cbeab1a7d584287366fbf4fc', 'BlsPubKey': '490da6e1253a7c3bf08ad99c820669656c5437878bf2ea6965ff23f64ed72e1d86b23bfe1ef65c3c9d2f160e863cef160ab43e1f13ff37d56bffbe7855a1c2307f327b981ab5f1d1c1b2e8b0d662551d90cd376f0e1485f69de4e41714ea7819', 'StakingAddress': 'atp1adtf8ewtqhmq93ep0mlgs30ar4v2s0d3pxgyrc', 'BenefitAddress': 'atp1adtf8ewtqhmq93ep0mlgs30ar4v2s0d3pxgyrc', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3546, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '74770a703d5f514a5935537059f7e854351bcc4b3297d026096649711f238fede7916be2713b3f6c2c91878152efb708f971ebcefc8782556416fb02297a4cd3', 'BlsPubKey': 'fe6cc1927a94ce2a9ad68a06bbf812617f661773f985aa7569f016fa08e2519d3a359d20eafd40d1091493b50f11f109ec20159c7ca1b1127726fd6a2497bcf3b860acbe8af1b503bfeb164d0c40ef2719a3032b6676b5d1cd935734664c7b93', 'StakingAddress': 'atp1ftrxq4s5myg5tqmgjr44nv5h55urhjy6hm4snw', 'BenefitAddress': 'atp1ftrxq4s5myg5tqmgjr44nv5h55urhjy6hm4snw', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3551, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'c102dc7ca9bbdedd154cee9cbe3721eab673025010fa1877b34617c18ce8126254aa5bf3b4d30089f0a7c383ad20784d6134fa69591d65fde92eb4bc712f243f', 'BlsPubKey': '34de258f0b8fbd31c19efadf11be74af6aea9f38847923c809467c340306c27069feff30c77ca096e47ddd73f2ccc2034cd9f381f1f1a1d06aa5ed032b7c1482b9d3356a8311e294dbbf211e3d878f2127196c024b085e6e5aa241552807cd11', 'StakingAddress': 'atp1mfu0cyml75np7csduc2g895akexksuafde0tnp', 'BenefitAddress': 'atp1mfu0cyml75np7csduc2g895akexksuafde0tnp', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3555, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': 'ae67f4cf9dd66472f3d81ca1d3b5f4a4e313a7642151f8a00e400ce1f0c82660bbdc07bc1873048f32e7fc5ec154a342ac0780bd56293a0ea8e39dc6bee1b5c8', 'BlsPubKey': 'e35c5cf1abf7b1e984ef3f58101d91ae7854747e5d9e910e7f4a3e8566cdf44f889e1369d9fab4e96593513ffb0e0b049398716d83466f6b16da35b7f3b37e121da04ea6c5692f77c5b80c116b9d4498cae13c00fad7a0116ea6a8aaf34daf10', 'StakingAddress': 'atp1egs8uzspe4egd9kedprs27gw8dj3300p6x73m0', 'BenefitAddress': 'atp1egs8uzspe4egd9kedprs27gw8dj3300p6x73m0', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3560, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '3d9b3315631962c2b8ea8c999d25b6d25ae29cd0bbcd585e1b2fa04777580d73577c7a39e23e00c1e1699acf8eb2f220d7abc06f716ae65270d550a81f92fcf5', 'BlsPubKey': '32415f2c79f251989b3382dc39047ae83c24eb5a122869baaadb763df4545e69e103018e3e70489eaeb449e30074ef041e31d646482f7d58afa6f10cdaa4ff76790a449413f44c00678906e95e8a4bcc26fc250d56dfe50d30884382ac9f798d', 'StakingAddress': 'atp123y66x9a63yvn0rpa8ums45g2cz2u9v8pn5zqe', 'BenefitAddress': 'atp123y66x9a63yvn0rpa8ums45g2cz2u9v8pn5zqe', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3564, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '90240d0b0fb3ca2bf6cfaec185b5b8cde7ed36512ee0d5c7eae334238821366140f6b3cc5634c89d018699d5ca4447d817833e99c86a838420de267a2a817a77', 'BlsPubKey': 'a4980855c822fe7338cd75a6211c3c16a392d27faf3a6c682bc931d357769ec7f525ba4b66a08b2dc3bc4c21f088b9031c95d527e4ca7564c5e2be4f2938fde404f6e4a6ad5b5e499017e9365fcfa559a9a874de74603667075c3b076b260588', 'StakingAddress': 'atp1c7jz2csunruly3aqljjgm3que83uvasc40zmlv', 'BenefitAddress': 'atp1c7jz2csunruly3aqljjgm3que83uvasc40zmlv', 'RewardPer': 1000, 'NextRewardPer': 1000, 'RewardPerChangeEpoch': 1, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 1, 'StakingBlockNum': 3568, 'Shares': 20000000000000000000000, 'Released': 0, 'ReleasedHes': 20000000000000000000000, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': 'external_id', 'NodeName': 'node_name', 'Website': 'website', 'Details': 'details'}, {'NodeId': '7924c431094e03d494948245b4aa6ba750beddd89bbcff2b9b6a8a429de4e9a7bd6d05369201f71529659f059e73a8573b764c515cffacc8d1aa00570bb837ec', 'BlsPubKey': 'ce8d622d0ee8025e6c636fd3f109783a50cac7919a6c567333786291417cff45df206e1124cfb9b69db38ac69bbff3147acb9be4df75158953f0947399f36ad218711ec7cea86adde5b743a8cf0dbffb064e199e91ece06102abffb9abf65107', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.1', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': '4f71e19d114208c137e2ebe56c249986d3e96475eafc5bf2c0e21fe573b27e7e552ea8371ecec6855571ea70ad70036f0bc131b69fd9205425092c5638155701', 'BlsPubKey': 'b782423b1574d06b33cbfb2f7b59169beae804adb413df74474f60fc986508abd4ab48d2de087b98743585c9b47dce06abfc35cc6b2bd42024bf57a4bcad8175f980ed051b198d3e62c3f653ded1044362a474876eb4b4ed03e2440115212b95', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 1, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.2', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': 'da7ad3634d22e2f0ef410dd41abc229adfadb004e2a6990724a96898551c7e29cc06556624077ea22042efb4c763e9d6f8190f58d178e3c36e25b370f176ea48', 'BlsPubKey': '27c6a37d205a8a3af3fa5750f6fec61e1b8587748ba72aba2872fb63000e6f1d2f0cceb904dfede23c0d44eeca8827149850b2b0bf2f61002776eda7d68bd74a3f740f7d9e681730389b07c47e30526d1349d96eabc8ddeca813f4845cc29018', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 2, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.3', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': 'e4fa996ea8ef426f90e1f0a2be7d5b70736ee5dbace46f9f3ac764728fb229c810fbc64de9f5aa26a0a3ab9c0db1e1222d37575e6ea98acb7866bc2bafd81246', 'BlsPubKey': '4e4185cca11e6c053320e743855ebea313a0239d98ff391ef0c17389c990b68a06678f72ac239da43219a2a95d8c480f65c19455c168c45957d5247f643d6e7c383f9866e87ba1eb6824cd3bf8482177b3bca3246bea9ac90c3576b2187c4090', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 3, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.4', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': '795c53e33221cf83539e2578757fd9c6290163a17db83b8135cc522f32ff1d833306dba54efc7a51265c28b4fb0b0cd92227ed1404c0ee02e5c4417504bee500', 'BlsPubKey': '5e9dca15e1cb6c57427348219da04dce2606b96f44e46d0a61deeaee187f2d0c977cec98851795950f52efe38e09d6008cdd1c42eb1d5319d7b31fffc37478c9df7327207096c78ff6fc8aa788fdc5aa46ca7a658af409a91b50cfcfefc96583', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 4, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.5', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': '22aa706ddb9482b03ddd4f19565ad0d9c0dd48fbcb9ca0ddda108a7cc2cd3e49e23b10aba8f72f7e60346cf474f72e855fab883c2fde25f736fb80cd625af702', 'BlsPubKey': '5134e901cc78ab65b007e2568de29d7c74d5e420ce9e9f0e61d311485dbae7811d2aaa040a3797662784740d8f86e304acdf87b7283c2e4c89d17878adebe73a34bbacdbae6d5072371d9ea92f64ac0116f89c32a0d74eb8a1c70559d1c0e214', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 5, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.6', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}, {'NodeId': '06b10fc918f91dface521a14b83604e5936fdaf6ab806e00a4b6a8b5dfe32f59fc0614ede81a7decfe71970134ffd64b20221d62fb5bf2dbe03c0ec464323f8a', 'BlsPubKey': '6cbab24aa5a67e817a2add203b7e0c4e91994dd70b62e75ba12c9cbf6d23b2c8fcdde3ca9924ad45fe97663312be550b75228c51cba2e24cd3bdba25aa9f4a08656c459c4b84a43c957dfabdfe4fde1f70e3bc8c3a28490fe97751c46d5f6d12', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 6, 'ProgramVersion': 3330, 'Status': 0, 'StakingEpoch': 0, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'Released': 10500000000000000000000, 'ReleasedHes': 0, 'RestrictingPlan': 0, 'RestrictingPlanHes': 0, 'DelegateEpoch': 0, 'DelegateTotal': '0x0', 'DelegateTotalHes': '0x0', 'DelegateRewardTotal': '0x0', 'ExternalId': '', 'NodeName': 'alaya.node.7', 'Website': 'alaya.network', 'Details': 'The Alaya Node'}]}
# verifierlist = tx.ppos.getVerifierList()
# print(f'verifierlist={verifierlist}')  #verifierlist={'Code': 0, 'Ret': [{'NodeId': '7924c431094e03d494948245b4aa6ba750beddd89bbcff2b9b6a8a429de4e9a7bd6d05369201f71529659f059e73a8573b764c515cffacc8d1aa00570bb837ec', 'BlsPubKey': 'ce8d622d0ee8025e6c636fd3f109783a50cac7919a6c567333786291417cff45df206e1124cfb9b69db38ac69bbff3147acb9be4df75158953f0947399f36ad218711ec7cea86adde5b743a8cf0dbffb064e199e91ece06102abffb9abf65107', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 0, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.1', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': '4f71e19d114208c137e2ebe56c249986d3e96475eafc5bf2c0e21fe573b27e7e552ea8371ecec6855571ea70ad70036f0bc131b69fd9205425092c5638155701', 'BlsPubKey': 'b782423b1574d06b33cbfb2f7b59169beae804adb413df74474f60fc986508abd4ab48d2de087b98743585c9b47dce06abfc35cc6b2bd42024bf57a4bcad8175f980ed051b198d3e62c3f653ded1044362a474876eb4b4ed03e2440115212b95', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 1, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.2', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': 'da7ad3634d22e2f0ef410dd41abc229adfadb004e2a6990724a96898551c7e29cc06556624077ea22042efb4c763e9d6f8190f58d178e3c36e25b370f176ea48', 'BlsPubKey': '27c6a37d205a8a3af3fa5750f6fec61e1b8587748ba72aba2872fb63000e6f1d2f0cceb904dfede23c0d44eeca8827149850b2b0bf2f61002776eda7d68bd74a3f740f7d9e681730389b07c47e30526d1349d96eabc8ddeca813f4845cc29018', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 2, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.3', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': 'e4fa996ea8ef426f90e1f0a2be7d5b70736ee5dbace46f9f3ac764728fb229c810fbc64de9f5aa26a0a3ab9c0db1e1222d37575e6ea98acb7866bc2bafd81246', 'BlsPubKey': '4e4185cca11e6c053320e743855ebea313a0239d98ff391ef0c17389c990b68a06678f72ac239da43219a2a95d8c480f65c19455c168c45957d5247f643d6e7c383f9866e87ba1eb6824cd3bf8482177b3bca3246bea9ac90c3576b2187c4090', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 3, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.4', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': '795c53e33221cf83539e2578757fd9c6290163a17db83b8135cc522f32ff1d833306dba54efc7a51265c28b4fb0b0cd92227ed1404c0ee02e5c4417504bee500', 'BlsPubKey': '5e9dca15e1cb6c57427348219da04dce2606b96f44e46d0a61deeaee187f2d0c977cec98851795950f52efe38e09d6008cdd1c42eb1d5319d7b31fffc37478c9df7327207096c78ff6fc8aa788fdc5aa46ca7a658af409a91b50cfcfefc96583', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 4, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.5', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': '22aa706ddb9482b03ddd4f19565ad0d9c0dd48fbcb9ca0ddda108a7cc2cd3e49e23b10aba8f72f7e60346cf474f72e855fab883c2fde25f736fb80cd625af702', 'BlsPubKey': '5134e901cc78ab65b007e2568de29d7c74d5e420ce9e9f0e61d311485dbae7811d2aaa040a3797662784740d8f86e304acdf87b7283c2e4c89d17878adebe73a34bbacdbae6d5072371d9ea92f64ac0116f89c32a0d74eb8a1c70559d1c0e214', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 5, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.6', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}, {'NodeId': '06b10fc918f91dface521a14b83604e5936fdaf6ab806e00a4b6a8b5dfe32f59fc0614ede81a7decfe71970134ffd64b20221d62fb5bf2dbe03c0ec464323f8a', 'BlsPubKey': '6cbab24aa5a67e817a2add203b7e0c4e91994dd70b62e75ba12c9cbf6d23b2c8fcdde3ca9924ad45fe97663312be550b75228c51cba2e24cd3bdba25aa9f4a08656c459c4b84a43c957dfabdfe4fde1f70e3bc8c3a28490fe97751c46d5f6d12', 'StakingAddress': 'atp1ur2hg0u9wt5qenmkcxlp7ysvaw6yupt4vll2fq', 'BenefitAddress': 'atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r', 'RewardPer': 0, 'NextRewardPer': 0, 'RewardPerChangeEpoch': 0, 'StakingTxIndex': 6, 'ProgramVersion': 3330, 'StakingBlockNum': 0, 'Shares': 10500000000000000000000, 'ExternalId': '', 'NodeName': 'alaya.node.7', 'Website': 'alaya.network', 'Details': 'The Alaya Node', 'ValidatorTerm': 0, 'DelegateTotal': '0x0', 'DelegateRewardTotal': '0x0'}]}

print(tx.platon.blockNumber)


# 委托平账：
# delegate1, private_key = tx.create_account()
delegate1, private_key = 'atp1gcnuk9n99rwm3vzv7vnqc00g35kpp0h838spwv', 'f1ed4d9be14711b84e0ea6f3c4e3b4e6eb8db61a1497b9599e621e907d8aad47'
# print('创建账户信息：', delegate1, private_key)  #创建账户信息： atp1gcnuk9n99rwm3vzv7vnqc00g35kpp0h838spwv f1ed4d9be14711b84e0ea6f3c4e3b4e6eb8db61a1497b9599e621e907d8aad47
# balance_befor = tx.platon.getBalance(delegate1)
# print(f'balance_befor={balance_befor}')
# result = tx.transfer(pri_key, delegate1, tx.web3.toWei(3, 'ether'))
# print(f'result={result}')
# balance_befor = tx.platon.getBalance(delegate1)
# print(f'balance_befor={balance_befor}')
#
delegate_list = [{'address': 'atp1a78ls0s4zrw66dwmx0h6vu6lp2wffjn52ftfkk',
                  'prikey': 'bdbcca45b8af0b751bb39657a005c9ed4341ed7bc15ac6eb37a84b7fd12fcc07'},
                 {'address': 'atp1tmdug9sv5kv06wu87yvhuedzat7mqwtk2runc9',
                  'prikey': '234685d90e59950a21293d835b4c07d3b59495439d84d7702cc4cf6cd531787d'},
                 {'address': 'atp1vtesk9c9eqq3aalajlnnvgxw7a86gq8dw423x9',
                  'prikey': '3b94db8adffdf98a83cae664127d071d71b33388101f3e3a70b9560fdf44621c'},
                 {'address': 'atp14hmsk2qne5ps3epf9jx8cyz94mkq00y4jlzvl8',
                  'prikey': '020676edc99aa0b0467f9b21555df072cfb7f506c77fbbd773c29bc8acdaf18d'},
                 {'address': 'atp1m0qy0ylh7evjk2yfrezkmaylwz32c4n3ttqukp',
                  'prikey': '27122d05e6aa853210465c7bea32102d8513ed08bc89b2262105cd42d970ec5c'},
                 {'address': 'atp1nmy3lfpxk0r7rezr5hjdscqsulwjlfprmjundm',
                  'prikey': '00eb834fd1de75897bb97cb9495e3bd401dcfca8d0f74c4b3ece2bfbd8a91046'},
                 {'address': 'atp16a5f649vmwk3842jcwajrfqtjrsu5rlfxx8v2h',
                  'prikey': '5c2f690ce28296ee98bcb6007b16c0c7ce5c5f4276cc7500eaae827e687b7384'},
                 {'address': 'atp1xwew5ywq4lcy3tt4epay5dm8mx46cs5t389y7v',
                  'prikey': '32106c508cd93f91bc1cd5e4e4034257b2c450a213a3dd41c42e1f133b72f1d0'},
                 {'address': 'atp102rkam0m4ayasfe5awklaf3y367zedr6vc236c',
                  'prikey': '4b59af16af4b4109b9ec876053f9fb938f0be9dc143bebca02518d68958b3afd'},
                 {'address': 'atp19nzzh4p3s87jf436hs2wmjjwta7k5yak2p98az',
                  'prikey': 'a5157fe5a53889d13810c5e1ef5ac4e341f4f6b395682df4b9e5ed91512db9c7'}
                 ]
#
# for i in delegate_list:
#     address = i['address']
#     balance_befor = tx.platon.getBalance(address)
#     print(f'balance_befor={balance_befor}')
#     result = tx.transfer(pri_key, address, tx.web3.toWei(3, 'ether'))
#     print(f'result={result}')
#     balance_befor = tx.platon.getBalance(address)
#     print(f'balance_befor={balance_befor}')
#
staking_nodeid1 = '104005f1bb2cefa6059be68d8f7b6dd0ed7b325688c88c6d03be8df471e5979b3d45157835cc2795566855392eb77274b61b3197f3dba129350cd2f61b6f9a0a'
staking_nodeid2 = '50b6d2f6490040ac0813d0aa0042d6020b0e537d5922805b00de7180bbdb29fca4877fdbf2d2dcd570b8ac9a904c02c69a60c9089239bfff04e0252886ef1158'
#
#
# for delegate in delegate_list[:4]:
#     result = tx.delegate(delegate['prikey'], staking_nodeid1, 0, tx.web3.toWei(1, 'ether'))
#     assert_code(result, 0)
#
# for delegate in delegate_list[4:]:
#     result = tx.delegate(delegate['prikey'], staking_nodeid2, 0, tx.web3.toWei(1, 'ether'))
#     assert_code(result, 0)
#
# result = tx.delegate(private_key, staking_nodeid1, 0, tx.web3.toWei(1, 'ether'))
# assert_code(result, 0)
#
# time.sleep(2)
# result = tx.delegate(private_key, staking_nodeid2, 0, tx.web3.toWei(1, 'ether'))
# assert_code(result, 0)
#
# #查看当前结算周期的出块间隔：
# avg_time= tx.ppos.getAvgPackTime()
# print(f'avg_time={avg_time}')   #avg_time={'Code': 0, 'Ret': 2000}

#5747块高


#等两个结算周期后注释上面的，跑下面的,复现bug  块高在21500-32250之间
#
for i in delegate_list:
    result = tx.ppos.getRelatedListByDelAddr(i['address'])['Ret']
    print(i['address'], result[0]['NodeId'])
    result = tx.ppos.getDelegateReward(i['address'])['Ret']
    reward = result[0]['reward']
    print('平账奖励：', reward)

result_de = tx.ppos.getDelegateReward(delegate1)['Ret']
print('操作地址各节点未提取委托奖励：', result_de)

#节点第一个信息：
candidate_info1 = tx.ppos.getCandidateInfo(staking_nodeid1)['Ret']
print("质押信息 {}".format(candidate_info1))
print("节点1在那个周期的生效委托 {}".format(candidate_info1['DelegateTotal']))

for delegate in delegate_list[:4]:
    stakingnum = tx.ppos.getCandidateInfo(staking_nodeid1)['Ret']['StakingBlockNum']
    result = tx.ppos.getDelegateInfo(stakingnum, delegate['address'], staking_nodeid1)['Ret']
    print("用户在那个周期委托的金额 {} {}".format(delegate['address'], result['Released']))


#节点第二个信息：
candidate_info2 = tx.ppos.getCandidateInfo(staking_nodeid2)['Ret']
print('质押信息：', candidate_info2)
print("节点2在那个周期的生效委托 {}".format(candidate_info2['DelegateTotal']))


for delegate in delegate_list[4:]:
    stakingnum = tx.ppos.getCandidateInfo(staking_nodeid2)['Ret']['StakingBlockNum']
    result = tx.ppos.getDelegateInfo(stakingnum, delegate['address'], staking_nodeid2)['Ret']
    print("用户在那个周期委托的金额 {} {}".format(delegate['address'], result['Released']))


#复现bug
for i in range(4):
    result = tx.delegate(private_key, staking_nodeid1, 0, tx.web3.toWei(1, 'ether'))
    assert_code(result, 301111)

for i in range(6):
    result = tx.delegate(private_key, staking_nodeid2, 0, tx.web3.toWei(1, 'ether'))
    assert_code(result, 301111)

result = tx.withdraw_delegate_reward(private_key)
assert_code(result, 0)

balance = tx.platon.getBalance(tx.ppos.delegateRewardAddress)
print(f'领取收益后委托收益池金额balance={balance}')

result = tx.ppos.getCandidateInfo(staking_nodeid1)['Ret']
print("节点1质押信息 {}".format(result))
print("节点在那个周期发放的委托奖励 {}".format(result['DelegateRewardTotal']))

result = tx.ppos.getCandidateInfo(staking_nodeid2)['Ret']
print("节点2质押信息 {}".format(result))
print("节点2在那个周期发放的委托奖励 {}".format(result['DelegateRewardTotal']))

for address in delegate_list:
    result = tx.ppos.getDelegateReward(address['address'])['Ret']
    reward = result[0]['reward']
    print(reward)
    balance = tx.platon.getBalance(address['address'])
    print(f'节点address={address}, 金额balance={balance}')


#升级


#升完级之后：
# for address in delegate_list:
#     result = tx.ppos.getDelegateReward(address['address'])['Ret']
#     reward = result[0]['reward']
#     print(reward)
#     balance = tx.platon.getBalance(address['address'])
#     print(f'节点address={address}, 金额balance={balance}')
