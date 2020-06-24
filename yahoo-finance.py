from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

welcome = """
         #     # ######## #         #####   #######  #     # ########
         #     # #        #        #     # #       # ##   ## #
         #     # #        #        #       #       # # # # # #
         #  #  # ######   #        #       #       # #  #  # ######
         # # # # #        #        #       #       # #     # #
         ##   ## #        #        #     # #       # #     # #
         #     # ######## ########  #####   #######  #     # ########

        #     # #######     #      #    ##    ####### #     #    ##
        ##   ## #      #    #      #   #  #      #    ##   ##   #  #
        # # # # #      #    #      #  #    #     #    # # # #  #    #
        #  #  # #######     ######## #      #    #    #  #  # #      #
        #     # #   #       #      # ########    #    #     # ########
        #     # #    #  ### #      # #      #    #    #     # #      #
        #     # #     # ### #      # #      #    #    #     # #      #
"""
print('<--'+75*'#'+'-->')
print(welcome)
print('<--'+75*'#'+'-->')

print('requesting . . .')
xiaomi_a3 = 'https://finance.yahoo.com/quote/BBCA.JK?p=BBCA.JK&.tsrc=fin-srch'

uClient = uReq(xiaomi_a3)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
'''
price = page_soup.findAll('div', {
    'class':'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'
    })
table = page_soup.findAll('td', {
    'class':'Ta(end) Fw(600) Lh(14px)'
    })
'''
nums = page_soup.findAll('span', {
    'class':'Trsdu(0.3s)'
    })

#print(price[0])
#print(table)
print('<--'+70*'#'+'-->')
#print(page_soup.prettify())

ket = ['Previous Close', 'Open', 'Bid', 'Ask']
for i, num in enumerate(nums[2:6]):
    print(str(ket[i]) + (15-len(ket[i]))*" " + "= " + str(num))

for i in range(len(nums)):
    print(nums[i].prettify())

print('<--'+70*'#'+'-->')
print('request done.')
