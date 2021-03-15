import logging
import random
import time
import traceback
from threading import Thread
from action import Action
from setting import load_accounts, load_duration, load_threads, web3
from utils import funcs_list


def load_threader():
    action = Action(load_accounts)
    actions.append(action)
    current_time = time.time()
    end_time = current_time + load_duration
    while current_time < end_time:
        # 随机选择方法
        func_name = random.choice(funcs_list)
        load_func = action.__getattribute__(func_name)
        action.logger.info(f'## Chose function is: {func_name}')
        # 随机选择账户
        address = random.choice(action.address_list)
        account = action.accounts[address]
        # 执行压测方法
        res_hash = ''
        try:
            res_hash = load_func(account)
        except Exception as e:
            # print(f'Transaction error! address: {account.address}, nonce: {account.nonce}, res_hash: {res_hash}')
            action.logger.error(f'Transaction error: {traceback.format_exc()}')
        action.logger.info(f'address: {account.address}, nonce: {account.nonce}, res_hash: {res_hash}')
        if res_hash is not False:
            account.nonce = account.nonce + 1
            # 对异常交易进行恢复
            if account.nonce % 20 == 0:
                try:
                    action.platon.waitForTransactionReceipt(res_hash, 20)
                except Exception as e:
                    action.logger.info('wait transaction receipt time out!')
                    nonce = action.platon.getTransactionCount(account.address)
                    if nonce:
                        account.nonce = nonce
                    action.logger.info(f'get transaction count: {account.nonce}')
        current_time = time.time()


def get_count():
    while True:
        time.sleep(10)
        counter = 0
        for action in actions:
            thread_counter = action.delegate_counter + action.undelegate_counter + action.withdraw_reward_counter
            counter = counter + thread_counter
        logging.info(f'counter: {counter}')


if __name__ == "__main__":
    # 主线程日志配置
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    # 生成线程池
    logging.info('######## Simple load tool ########')
    actions, threads = [], []
    for i in range(load_threads):
        t = Thread(target=load_threader, name=f'T{i}')
        threads.append(t)
    # 启动压测线程
    for thread in threads:
        time.sleep(1)
        thread.start()
        logging.info(f'thread [{thread.name}] Started!')
    logging.info(f'loader is running at {web3.eth.blockNumber}, please waiting...')
    logging.info(f'(ps: you can see more from the threads log)')
    # 启动查询线程
    t = Thread(target=get_count, name=f'Tc')
    t.setDaemon(True)
    t.start()
    # 等待多线程运行完成
    for thread in threads:
        thread.join()
    logging.info('load test is done!')
