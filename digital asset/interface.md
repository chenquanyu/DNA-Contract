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
- 方法声明: def pledgeAsset(assetId)
- 行为：质押数字资产
- 校验：金融机构方私钥签名

### 2.1.4. releaseAsset

- 功能说明：解除数字资产质押
- 方法声明: def releaseAsset(assetId)
- 行为：解除数字资产质押
- 校验：金融机构方私钥签名

### 2.1.5. getAsset

- 功能说明：获取数字资产的基本信息和质押状态
- 方法声明: def getAsset(assetId)
- 行为：获取数字资产的基本信息和质押状态
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

# 6. 字典代码

## 6.1. 网页入口端代号

字段名称： entry_type

|代码|说明|
|--|--|
|S|Supplier|
|C|Center Company|
|F|Finance|
|P|Platform|

## 6.2. 用户角色

字段名称： role

|代码|说明|
|--|--|
|SM|供应商管理员|
|SO|供应商操作员|
|SA|供应商审核员|
|CM|核心企业管理员|
|CO|核心企业操作员|
|CA|核心企业审核员|
|FM|金融机构管理员|
|FO|金融机构操作员|
|FA|金融机构审核员|
|PM|平台管理员|

## 6.3. 用户（供应商，核心企业，金融机构）状态

字段名称： status

|代码|说明|
|--|--|
|1|已启用|
|0|已删除|
|2|已停用|

## 6.4. 文件类型

字段名称： file_type

|代码|说明|
|--|--|
|IDA|身份证正面|
|IDB|身份证反面|
|CA|企业征信授权书|
|FS|财务报表列表|
|BL|营业执照正本|
|BLC|营业执照副本|
|OP|基本开户许可证|
|CPV|公司章程及验资报告|
|BT|银行流水|
|SXA|授信附件|
|CONTRACT|合同|
|DEBT|债权凭证|
|PC|付款承诺函|

## 6.5. 供应商认证状态

字段名称： approve_status

|代码|说明|
|--|--|
|Saved|已保存|
|Pending|待认证|
|Approved|认证通过|
|Returned|已退回修改|
|Rejected|已拒绝|

## 6.6. 债权凭证状态

字段名称： token_status

|代码|说明|
|--|--|
|Saved|待提交|
|Pending|待签收|
|Accepted|已签收|
|Rejected|已拒绝|
|Transferring|已流转|
|Transferred|已流转|

## 6.7. 债权凭证转让方式

字段名称： transfer_type

|代码|说明|
|--|--|
|All|全额转让|
|Part|拆分转让|

## 6.8. 授信业务类型

字段名称： business_type

|代码|说明|
|--|--|
|Create|额度创建|
|Update|额度修改|

## 6.9. 授信状态

字段名称： credit_status

|代码|说明|
|--|--|
|Pending|待授信|
|Waiting|已授信|
|Active|已启用|
|Expired|已过期|
