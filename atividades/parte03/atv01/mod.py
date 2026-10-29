
'''
• Mercúrio: 3,7
• Vênus: 8,8
• Terra: 9,8
• Marte: 3,7
• Júpiter: 24,7
• Saturno: 10,4
• Urano: 8,6
• Netuno: 11,1
• Lua: 1,6
'''
import os

def li():
    os.system('cls' if os.name == 'nt' else 'clear')
    
mer = lambda m: m*3.7
ven = lambda m: m*8.8
ter = lambda m: m*9.8
lua = lambda m: m*1.6
mar = lambda m: m*3.7
jup = lambda m: m*24.7
sat = lambda m: m*10.4
ura = lambda m: m*8.6
net = lambda m: m*11.1