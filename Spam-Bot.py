import requests
import pyfiglet
ZX = '\033[1;31m' #احمر
kX = '\033[1;33m' #اصفر
mZ1 = '\033[2;31m' #احمر ثاني
mF = '\033[2;32m' #اخضر
nA = '\033[2;34m'#ازرق
jC = '\033[2;35m' #وردي
jB = '\033[2;36m'#سمائي
kY = '\033[1;34m' #ازرق فاتح
Z =  '\033[1;31m' #احمر
Mala = '-'
print(ZX+Mala*50)           

logo = pyfiglet.figlet_format('Spam-BoT')
print(Z+logo)
Mala = '-'
print(ZX+Mala*50)           
tok = input(kY+'  Token Bot  : ')
ID = input(kY+' - ID Telegram : ')
M = input(kY+' - Chataka Che Bet??  : ')
print(jB+' -  Wait Spam bot .........')
while True:  
   tlg = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= > {M}''')
