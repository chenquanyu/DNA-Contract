**《DNA区块链系统部署手册》**

[TOC]

以下操作都是针对service的服务器，环境为linux，推荐使用Ubuntu或CentOS

# 1. 部署区块链节点

此部分以单主机上部署多区块链节点为例进行说明。
  
## 1.1. 获取

首先从github下载DNA文件到指定的目录:
```shell
$ mkdir /opt/DNA && cd /opt/DNA
$ wget https://github.com/DNAProject/DNA/releases/download/v0.7.3beta/dnaNode-linux-amd64
$ mv dnaNode-linux-amd64 dnaNode
$ chmod +x dnaNode
```

得到可执行程序

* `dnaNode`: 节点程序

## 1.2. 配置修改

成功运行DNA需要至少4个节点：

1. 将相关文件复制到目标主机，包括：
    - 节点程序`dnaNode`
      ```shell
      $ cd /opt/DNA && mkdir node1 node2 node3 node4 
      $ cp /opt/DNA/dnaNode /opt/DNA/node1
      $ cp /opt/DNA/dnaNode /opt/DNA/node2
      $ cp /opt/DNA/dnaNode /opt/DNA/node3
      $ cp /opt/DNA/dnaNode /opt/DNA/node4
      ```

2. 创建钱包文件
    - 通过命令行程序，在每个主机上分别创建节点运行所需的钱包文件wallet.dat 

      ```shell
      ./dnaNode account add -d
      Use default setting '-t ecdsa -b 256 -s SHA256withECDSA'
        signature algorithm: ecdsa
        curve: P-256
        signature scheme: SHA256withECDSA
      Password:
      Re-enter Password:
      Index:1
      Label:
      Address:AQSM9mwdBQLRMmnqjgRNKtjDQPR2VckYwn
      Public key:03cde2494a59569fb6cac64539645bcdad3284b97d56a30c9f48b7f5d9a511c58d
      Signature scheme:SHA256withECDSA
      Create account successfully.

      ```

3. 种子节点配置

    - 默认配置文件`config.json`

      ```shell
      $ cd /opt/DNA/node1
      $ touch config.json
      $ vi config.json
      {
        "SeedList": [
          "10.0.1.100:20338",
          "10.0.1.101:20338",
          "10.0.1.102:20338",
          "10.0.1.103:20338"
        ],
        "ConsensusType":"vbft",
        "VBFT":{
          "n":40,
          "c":1,
          "k":4,
          "l":64,
          "block_msg_delay":10000,
          "hash_msg_delay":10000,
          "peer_handshake_timeout":10,
          "max_block_change_view":3000,
          "admin_ont_id":"did:dna:AMAx993nE6NEqZjwBssUfopxnnvTdob9ij",
          "min_init_stake":10000,
          "vrf_value":"1c9810aa9822e511d5804a9c4db9dd08497c31087b0daafa34d768a3253441fa20515e2f30f81741102af0ca3cefc4818fef16adb825fbaa8cad78647f3afb590e",
          "vrf_proof":"c57741f934042cb8d8b087b44b161db56fc3ffd4ffb675d36cd09f83935be853d8729f3f5298d12d6fd28d45dde515a4b9d7f67682d182ba5118abf451ff1988",
          "peers":[
            {
              "index":1,
              "peerPubkey":"0289ebcf708798cd4c2570385e1371ba10bdc91e4800fa5b98a9b276eab9300f10",
              "address":"ANT97HNwurK2LE2LEiU72MsSD684nPyJMX",
              "initPos":10000
            },
            {
              "index":2,
              "peerPubkey":"039dc5f67a4e1b3e4fc907ed430fd3958d8b6690f4f298b5e041697bd5be77f3e8",
              "address":"AMLU5evr9EeW8G1WaZT1n1HDBxaq5GczeC",
              "initPos":10000
            },
            {
              "index":3,
              "peerPubkey":"0369f4005b006166e988af436860b8a06c15f3eb272ccbabff175e067e6bba88d7",
              "address":"AbSAwqHQmNMoUT8ps8N16HciYtgprbNozF",
              "initPos":10000
            },
            {
              "index":4,
              "peerPubkey":"035998e70d829eea58998ec743113cf778f66932a063efc1a0a0496717c4a0d93d",
              "address":"AemhQtcPTGegSk1UAsiLnePVcut1MLXSPg",
              "initPos":10000
            }
          ]
        }
      }
      ```

    - 将4个主机作为种子节点地址分别填写到每个配置文件的`SeelList`中，格式为`节点IP地址 + 节点NodePort`，默认节点端口20338
      ```shell
      "SeedList": [
        "10.23.227.249:20338",
        "10.23.227.249:20348",
        "10.23.227.249:20358",
        "10.23.227.249:20368"
      ]
      ```

4. 记账人配置
    - 为每个节点创建钱包时会显示钱包的公钥信息，将所有节点的公钥信息分别填写到节点配置文件的`peers`项中
    
      ```shell
      "peers":[
      {
        "index":1,
        "peerPubkey":"03cde2494a59569fb6cac64539645bcdad3284b97d56a30c9f48b7f5d9a511c58d",
        "address":"AQSM9mwdBQLRMmnqjgRNKtjDQPR2VckYwn",
        "initPos":10000
      },...]
      ```
        注：每个节点的钱包公钥信息也可以通过命令行程序查看：
    
        `$ ./dnaNode account list -v` 

5. 复制config.json到每个节点的目录中：

      ```shell
      $ cp /opt/DNA/node1/config.json /opt/DNA/node2
      $ cp /opt/DNA/node1/config.json /opt/DNA/node3
      $ cp /opt/DNA/node1/config.json /opt/DNA/node4
      ```    

    每个节点目录结构如下，

    ```shell
    $ ls
    config.json dnaNode wallet.dat
    ```
## 1.3. 启动

创建启动脚本 `start.sh` （如果在同一台机器则需要为每个节点配置不同端口）

```shell
$ cd /opt/DNA
$ touch start.sh
$ vi start.sh
#!/bin/bash
cd /opt/DNA/node1
nohup ./dnaNode --config=config.json --enable-consensus --rest=true --nodeport=20338 --rpcport=20336 --restport=20334 --wsport=20335 --password=123456 &
cd /opt/DNA/node2
nohup ./dnaNode --config=config.json --enable-consensus --rest=true --nodeport=20348 --rpcport=20346 --restport=20344 --wsport=20345 --password=123456 &
cd /opt/DNA/node3
nohup ./dnaNode --config=config.json --enable-consensus --rest=true --nodeport=20338 --rpcport=20356 --restport=20354 --wsport=20355 --password=123456 &
cd /opt/DNA/node4
nohup ./dnaNode --config=config.json --enable-consensus --rest=true --nodeport=20368 --rpcport=20366 --restport=20364 --wsport=20365 --password=123456 &

$ chmod +x start.sh
$ ./start.sh
```

了解更多请运行 `./dnaNode --help`.