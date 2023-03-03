###### 


# ملف اضافي 

######

print('helper file opened')


# معلومات ومتغيرا البوت
  

json_file = r"sid.json"

images  = r'Bot\images'

coms = [144339917,0]



Help_menu = '\n'.join(
    (
        '''
        Yourname? : اسم البوت
        ''',
        '''
        Random? : دعوة اعضاء عشوائين 
        '''
        ,
        '''
        DevAcc? : حساب المطور
        '''
        ,
        '''
        else? : 
        ''',
        '''
        RandomBg? : لتغيير خلفية الشات
        ''',
        '''
        EditT? : لتعديل عنوان الدردشة
        ''',
        '''
        Join? : ادخال البوت الى دردشة
        ''',
        '''
        lev? : لمغادرة دردشة
        '''
        
        )
)

UrlChat = 'http://aminoapps.com/p/jc2uau2'
e = "ukqubnrkxg85@vddaz.com"

p = "hamza#$1234"


### 
# استدعاء المودل
###




# from keep_alive import keep_alive

# keep_alive()
from requests import get ,post


from aminofix import Client , SubClient

from os import remove

from  json import loads , load,dump,dumps

from  base64 import encodebytes

from random import choice,sample

from io import BytesIO