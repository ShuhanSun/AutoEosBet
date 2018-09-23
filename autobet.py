#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
import time
import random

# 本地需要有：cleos, keosd,并创建钱包导入账户私钥

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

args = None
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

def run(args):
    # print('autobet.py:', args)
    return subprocess.call(args, shell=True)

def runre(args):
    pi = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
    r = pi.stdout.read()
    return r

def bet(account, amount, roll):
	shell = "cleos -u "+API_URL+" transfer "+account+" eosbetdice11 '"+amount+"' "+roll+"-aaapppaaappp-"
	print("🎲 ", account, amount, roll)
	if Enable_Bet :
		run(shell)

def transfer(account_from, account_to, amount, memo):
	shell = "cleos -u "+API_URL+" transfer "+account_from+" "+account_to+" '"+Bet_Profit+"' "+memo
	if Enable_Bet :
		run(shell)

def wallet_unlock():
	args="cleos wallet unlock --password "+Wallet_Passwd
	run(args)
	

def sleep(s):
	print("sleep:", s, "s: ", end='', flush=True)
	while s > 0:
		s = s - 1
		print(".", end='', flush=True)
		time.sleep(1)
		
	print()

def getbalance(account):
	r = runre("cleos -u "+API_URL+" get currency balance eosio.token "+account)
	#b'1.8677 EOS\n'
	return float(r[0:6])

def autobet(account, amount):
	roll = random.randint(Roll_Random_Low, Roll_Random_Up)
	
	before = getbalance(account)
	bet(account, amount, str(roll))
	time.sleep(3)
	after = getbalance(account)
	print("EOS余额 balance :", before," ---> ", after)
	
	ab=round(after-before, 4)
	if ab >= 0:
		print("WIN 赢啦 😄 ======>", ab)
	else :
		print("LOST 输了 😂 ======>", ab)

	if after >= Balance_Threshold:
		transfer(account, Earn_account, Bet_Profit, "iam")


count=0
while True:
	wallet_unlock()
	count=count+1
	print("🎲🎲🎲 ---------------- eosbet 第:"+str(count)+"局  ------------------------🎲🎲🎲")

	t=Sleep_Time/3
	autobet(My_Account, Bet_Limit)
	sleep(random.randint(t-Sleep_Time_Randome, t+Sleep_Time_Randome))

	autobet(My_Account2, Bet_Limit)
	sleep(random.randint(t-Sleep_Time_Randome, t+Sleep_Time_Randome))

	autobet(My_Account3, Bet_Limit)
	sleep(random.randint(t-Sleep_Time_Randome, t+Sleep_Time_Randome))
	pass



