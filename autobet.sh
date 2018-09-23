
#本地需要有：cleos, keosd,并创建钱包导入账户私钥。依赖 geteos.sh
#改为自己的游戏账户
MyAccount='aaaeeeiiiooo'
#收益账户
EarnAccount='aaapppaaappp'
#钱包密码
Wallet_Passwd='1234'

function rand(){
        min=$1
        max=$(($2-$min+1))
        num=$(($RANDOM+1000000000))
        echo $(($num%$max+$min))
    }

for i in {1..3000}  
do  
cleos wallet unlock --password $Wallet_Passwd

t=$(rand 400 500)
echo '------' $i;
ROLL_UNDER=$(rand 1 5)
cleos -u https://api.eosnewyork.io:443 transfer $MyAccount eosbetdice11 '0.1000 EOS' $ROLL_UNDER'5-aaapppaaappp-'

echo 'sleep:' $t
sleep $t

MYEOS=$(./geteos.sh $MyAccount)
myeos=${MYEOS:0:6}
echo '-- my eos is: ' $myeos
if [[ `expr $myeos \> 3.5` -eq 1 ]];then
    echo "go,go,go"
    cleos -u https://api.eosnewyork.io:443 transfer $MyAccount $EarnAccount '0.5000 EOS' iam-$myeos
fi

done
