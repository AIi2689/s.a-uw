import os
def ar():
 if os.path.exists('font.ttf'):
    os.system('curl https://raw.githubusercontent.com/br5kly/XC/main/font.sh >font.sh')
    os.system('chmod +x font.sh')
    os.system('bash font.sh')
    ar()
 if not os.path.exists('font.ttf'):
    print("تريمكس عربي بالفعل")   
ar()
