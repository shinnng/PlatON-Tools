## Usage
- 创建账户，并保存到文件

```shell
	python generator.py makeaccount --number 10 --tofile "./accounts.yml"
```

- 从账户文件进行批量转账
```shell
	python generator.py transfer --account "accounts.yml" --privatekey "a689f0879f53710e9e0c1025af410a530d6381eebb5916773195326e123b822b"
```

- 从账户文件进行批量锁仓
```shell
	python generator.py restricting --account "accounts.yml" --privatekey "a689f0879f53710e9e0c1025af410a530d6381eebb5916773195326e123b822b" --epoch 10
```

- 从质押配置文件进行批量质押
```shell
	python generator.py staking --config "./staking_info.yml"
```

- 从质押配置文件进行批量解质押
```shell
	python generator.py withdrew_staking --config "./staking_info.yml"
```

- 使用账户文件中的所有账户，每个账户对随机N个节点进行委托
```shell
	python generator.py delegate --account "./accounts.yml" --amount 20000000000000000000
```

- 使用账户文件中的所有账户，对每个账户委托的N个节点进行解委托
```shell
	python generator.py withdrew_delegate --account "./accounts.yml" --amount 10000000000000000000
```

- 使用账户文件中的所有账户，进行领取委托分红
```shell
	python generator.py withdrew_delegate_reward --account "./accounts.yml"
```












