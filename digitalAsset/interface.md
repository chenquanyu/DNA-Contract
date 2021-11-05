<h1>数字资产合约接口功能设计</h1>

# 1. 基本规范

* 使用工具: DNA java sdk
* 使用示例: json

# 2. 数字资产模块功能清单

## 2.1. 资产信息

### 2.1.1. issueAsset

- 功能说明：发行数字资产
- 方法声明: def issueAsset(assetId, assetInfo)
- 行为：新建数字资产记录
- 校验：资产发行方私钥签名

### 2.1.2. changeStatus

- 功能说明：修改数字资产状态等基本信息
- 方法声明: def changeStatus(assetId, assetInfo)
- 行为：修改数字资产记录，增加修改历史记录
- 校验：资产发行方私钥签名

### 2.1.3. pledgeAsset

- 功能说明：质押数字资产
- 方法声明: def pledgeAsset(assetId, assetInfo, financeInfo)
- 行为：质押数字资产
- 校验：金融机构方私钥签名

### 2.1.4. releaseAsset

- 功能说明：解除数字资产质押
- 方法声明: def releaseAsset(assetId, assetInfo, financeInfo)
- 行为：解除数字资产质押
- 校验：金融机构方私钥签名

### 2.1.5. getAsset

- 功能说明：获取数字资产的基本信息和质押状态
- 方法声明: def getAsset(assetId)
- 行为：获取数字资产的基本信息和质押状态（json字符串）
- 校验：无

### 2.1.6. getAssetHistory

- 功能说明：获取数字资产的基本信息和质押状态
- 方法声明: def getAssetHistory(assetId)
- 行为：获取数字资产的基本信息和质押状态（json字符串）
- 校验：无

## 2.2. 权限管理

### 2.2.1. initOwner

- 功能说明：初始化合约管理账户
- 方法声明: def initOwner(address)
- 行为：初始化合约管理账户
- 校验：只有管理员为空时可以调用

### 2.2.2. changeOwner

- 功能说明：修改合约管理账户
- 方法声明: def changeOwner(address)
- 行为：修改合约管理账户，修改后原管理员账户失效
- 校验：管理员账户私钥签名

### 2.2.3. addIssuer

- 功能说明：增加资产发行方账号
- 方法声明: def addIssuer(address)
- 行为：增加资产发行方账号
- 校验：管理员账户私钥签名

### 2.2.4. removeIssuer

- 功能说明：删除资产发行方账号
- 方法声明: def removeIssuer(address)
- 行为：删除资产发行方账号
- 校验：管理员账户私钥签名

### 2.2.5. addFinance

- 功能说明：增加金融机构账号
- 方法声明: def addFinance(address)
- 行为：增加金融机构账号
- 校验：管理员账户私钥签名

### 2.2.6. removeFinance

- 功能说明：删除金融机构账号
- 方法声明: def removeFinance(address)
- 行为：删除金融机构账号
- 校验：管理员账户私钥签名

## 2.3. 生成账户钱包

```shell
$ cd /path/to/DNAhome
# 生成管理员账户
$ ./dnaNode account add -d -w adminWallet.dat
# 生成资产发行者账户
$ ./dnaNode account add -d -w issuerWallet.dat
# 生成金融机构账户（预留非必须）
$ ./dnaNode account add -d -w financeWallet.dat
```

## 2.4. 部署合约

合约编译后需要部署上链，首先拷贝编译后的文件到节点目录：
```shell
$ cp /path/to/contract/AssetStorage.avm.str /path/to/DNAhome
$ cp /path/to/contract/DigitalAsset.avm.str /path/to/DNAhome
```

然后执行合约部署
```shell
$ cd /path/to/DNAhome
$ ./dnaNode contract deploy --wallet adminWallet.dat --code AssetStorage.avm.str --name AssetStorage --version 1.0 --gaslimit 200000000
$ ./dnaNode contract deploy --wallet adminWallet.dat --code DigitalAsset.avm.str --name DigitalAsset --version 1.0 --gaslimit 200000000
```

这里需要输入钱包密码，然后会返回交易hash，查看执行结果，可通过`./dnaNode info status <TxHash> `来查询交易执行情况
```shell
Password:
Deploy contract:
  Contract Address:f84d079e3e6eedccd0be29a01c902e03c8d325d2
  TxHash:244d7506d0e653533bb7e8ab5d30f088141a0b6a63989126ad78d23efbefcbc2

Tip:
  Using './dnaNode info status 244d7506d0e653533bb7e8ab5d30f088141a0b6a63989126ad78d23efbefcbc2' to query transaction status.
```
**注意：保存好合约地址，用于合约调用**

## 2.5. 部署结果验证

测试AssetStorage、DigitalAsset合约中的name方法，以AssetStorage为例
```shell
$ ./dnaNode contract invoke --address f84d079e3e6eedccd0be29a01c902e03c8d325d2 --params string:name,[string:] --gaslimit 200000 -p -return string

#返回结果
Invoke:d225d3c8032e901ca029bed0cced6e3e9e074df8 Params:["name",[""]]
Contract invoke successfully
  Gas limit:20000
  Return:AssetStorage
```
DigitalAsset合约测试只需替换合约地址即可

## 2.6. 合约初始化

只有DigitalAsset合约需要初始化。

### 2.6.1. 设置合约管理员

合约管理员具备管理资产发行者和金融机构的权限

```shell
# 参数填写owner的钱包账户地址
$ ./dnaNode contract invoke --wallet adminWallet.dat --address 417e68329fd7c5b677ce216c65fa7fc53ed7ee2e --params string:initOwner,[string:'AFmseVrdL9f9oyCzZefL9tG6UbvhPbdYzM'] --gaslimit 200000
```

### 2.6.2. 设置资产发行者（sdk账户）

该设置必须使用合约管理员的钱包账户进行调用

```shell
# 参数填写issuer的钱包账户地址
$ ./dnaNode contract invoke --wallet adminWallet.dat --address 417e68329fd7c5b677ce216c65fa7fc53ed7ee2e --params string:addIssuer,[string:'AMeXW8YQ26a4kRDyxheJU6kcxajHgSCk2h'] --gaslimit 200000
```

### 2.6.3. 设置金融机构（预留功能）

该设置必须使用合约管理员的钱包账户进行调用

```shell
# 参数填写finance的钱包账户地址
$ ./dnaNode contract invoke --wallet adminWallet.dat --address 417e68329fd7c5b677ce216c65fa7fc53ed7ee2e --params string:addFinance,[string:'AMeXW8YQ26a4kRDyxheJU6kcxajHgSCk2h'] --gaslimit 200000
```

## 2.7. 命令行形式调用合约业务功能（供调试使用）

以发行资产为例，钱包需使用资产发行者账户

```shell
# 发行资产
$ ./dnaNode contract invoke --wallet issuerWallet.dat --address 417e68329fd7c5b677ce216c65fa7fc53ed7ee2e --params string:issueAsset,[string:'mykey',string:'myvalue'] --gaslimit 200000

# 查询资产
$ ./dnaNode contract invoke --wallet issuerWallet.dat --address 417e68329fd7c5b677ce216c65fa7fc53ed7ee2e --params string:getAsset,[string:'mykey'] --gaslimit 200000 -p -return string

Invoke:2eeed73ec57ffa656c21ce77b6c5d79f32687e41 Params:["getAsset",["mykey"]]
Contract invoke successfully
  Gas limit:20000
  Return:{"AssetInfo":"myvalue","FinanceInfo":""}
```


