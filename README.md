# autoeosbet

自动玩eosbet 游戏，eosbet游戏外挂。

可设置多个账户，随机出数，随机周期。


说明：
  1. 本地安装：cleos, keosd 工具(eosio命令行与钱包管理器)
  2. 创建钱包导入账户私钥。
  3. 修改脚本中的默认配置。
  4. sh或python3, 执行脚本。等待获取收益。。。。。。

配置：

#开启下注
Enable_Bet=True

#每局休息时间 秒
Sleep_Time=15

#每个账户随机休息时间幅度
Sleep_Time_Randome=1

#每次下注额度
Bet_Limit='0.1000 EOS'

#下注数字： 1~96
#随机下注最低值
Roll_Random_Low=35

#随机下注最高值
Roll_Random_Up=65

API_URL = "https://api.eosnewyork.io:443"

#钱包密码
Wallet_Passwd='1234'

#账户名, 默认3个账号同时玩
My_Account='aaaeeeiiioo'
My_Account2='aaaeeeiiioo'
My_Account3='aaaeeeiiioo'

#及时收取收益阈值：账户余额多余此数时，自动将收益转至收益账户
Balance_Threshold=3.5

#收取收益额度
Bet_Profit="0.5000 EOS"

#收益账户
Earn_account='aaapppaaappp'
