###

"""
ملف تحديث معرف الجلسة (سايد)
"""
###
from helper import *

http_proxy = "187.1.57.206:20183"
https_proxy = "203.8.207.39:80"


proxies = None 
# #{
# "http" : http_proxy,
# "https" : https_proxy,

# }

try:
    with open(json_file,"w") as  Json:
        Ac = Client(
            autoDevice=True,proxies=proxies
        )

        Ac.login(
            e
            ,
            p
        )

        Json.write(
            '[ \n \t'
        )

        dump(
            {
                "sid" : Ac.sid
                }
                ,
                Json
                ,
                indent=6
                )

        Json.write(
            '\n \t ]'
        )
        print('''
        Done ''')

except Exception  as JsonFilError:
    print(
 JsonFilError
    )