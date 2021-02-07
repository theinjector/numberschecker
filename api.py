import requests
import pyfiglet
import time
from termcolor import colored
#if proxy is dead change it type:http
#website for http proxies http://www.freeproxylists.net/fr/?c=&pt=&pr=HTTP&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0
#use fast proxy
proxies = {'http': 'http://110.78.147.62.8080','http': 'http://49.204.79.81:80'}

ascii_banner = pyfiglet.figlet_format("Num Validation")
exit = "Donation Paypal: https://www.paypal.me/abderrafielamhali"

print(colored(ascii_banner,'red'))
print(colored(">>>>Please Don't Forget to add your prefix country in your list<<<<",'yellow'))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36OPR/63.0.3368.71'}

print("\033[36;1m-list of proxies to send the request randomly" ,proxies)
s = requests.session()
live = open('live.txt','w')
die = open('dead.txt','w')
list = input("\033[32;1m Please input your Phone numbers List : \033[0m")
list = open(list, 'r')
print(colored("Loading proxies...",'red'))
time.sleep(3)

while True:
	code = list.readline().replace('\n','')
	if not code:
		break
    # if you want to change api_key please create an account in abstractapi.com ang get your api_key
	link="http://phonevalidation.abstractapi.com/v1/?api_key=3f302e5b72704232a9ec72b5b91badbe&phone={}".format(code)
	r = requests.post(url = link)
	content = requests.get(link,proxies=proxies,headers=headers).text
	if "false" in content:
		print("\033[31m-"*50)
		print("\033[31m[-]INVALID> \033[0m : \033[31m"+code+"|\033[37m[INVALID PHONE]")
		print("\033[31m-"*50)
		die.write(code + "\n")
	else:
		print("\033[32;1m-"*50)
		print("\033[32;1m[+]VALID> \033[0m : \033[32m"+code+"|\033[37m[VALID PHONE]")
		print("\033[32;1m-"*50)
		live.write(code +"\n")
print(colored(exit,'yellow'))
