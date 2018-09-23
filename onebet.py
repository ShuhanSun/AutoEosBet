#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
import time
import random

#是否开启赌
Enable_Bet=True
#钱包密码
Wallet_Passwd="1234"
#eos账户
MyAccount="aaaeeeiiiooo"

args = None
API_URL = "https://api.eosnewyork.io:443"

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



wallet_unlock()

account=MyAccount
roll = sys.argv[1]
# before = getbalance(account)
bet(account, "0.1000 EOS", str(roll))

time.sleep(3)
after = getbalance(account)
print("EOS余额 balance :", before," ---> ", after)
ab=round(after-before, 4)
if ab >= 0:
	print("WIN 赢啦 😄 ======>", ab)
else :
	print("LOST 输了 😂 ======>", ab)




