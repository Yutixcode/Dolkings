# Code by : Njank
# Datetime: May, 09, 2020 - 01:03:23 WIB
# Facebook: njnk.xnxx
from googlesearch import search
from enum import Enum
x = '\033[0m'
u = '\033[4m'
R = '\033[1;91m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;33m'
w = '\033[0;37m'
print(f"""{R}
  (      
  )\ )   
 (()/(  
  /(_))                          ( 
 (_))_      _ _    _              )\ 
  |   \ ___| | |_ (_)_ __  __ _ _(_))
  | {w}|){R} / {w}_{R} \ | / /| | '  \/ {w}_{R}` / __| 
  |___/\___/_|_\_\|_|_||_|\__, \__ \ 
   {w}>> {u}Codename:{x} {u}Yutixcode{x} {R}|___/\___/ 
""")
try:
	ny1 = input(f" {r}{u}Dork{w}:{x} {y}")
	ny2 = int(input(f" {r}{u}Page{w}:{x} {y}"))
	ny3 = int(input(f" {r}{u}Time{w}:{x} {y}"));print('')
	nyx = 0
	for i in search(ny1, tld="com", lang="en", num=int(ny2), start=0, stop=None, pause=int(ny3)):
		with open('results.txt', 'a') as f:
			f.write(f'{i}\n')
		nyx += 1
		print(f'{w}{nyx}) {g}{i}')
		if nyx >= int(ny2):
			break;
	print(f'\n{w}Saved: {g}results.txt')
except ValueError:
	exit(f' {r}{u}Exit{w}! {y}input error')
except KeyboardInterrupt:
	exit(f'\n {r}{u}Exit{w}! {y}thanks for using;)')
