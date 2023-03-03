###
"""
الملف الرئيسي
"""
###





from functiones import *


http_proxy = "187.1.57.206:20183"
https_proxy = "203.8.207.39:80"


proxies =None
# # {
# "http" : http_proxy,
# "https" : https_proxy,

# } 



Ac = Client(autoDevice=True,proxies=proxies)

try:
      file = open(
        json_file
        )
      data = load(
        file
    )

      Ac.login_sid(data[0]["sid"])

      file.close() 
except Exception as Login_Error:
    print(
        Login_Error
    )


Object = Ac.get_from_code(
    UrlChat
)

ChatId = Object.objectId


ComId = Object.comId

Sc = SubClient(
    comId=ComId,profile=Ac.profile,proxies=proxies
    )

Ac.join_community(
    comId=ComId
    ) if ComId!=0 else None

print(ComId)
Sc.join_chat(ChatId)

Sc.edit_profile(content=Help_menu)

vip1 = return_ObjId('https://aminoapps.com/c/mary-miraculous/page/user/coder/r4a1_xQSBfrkoBB5Vlg1mpmb3zvzk5n2YY')
vip2 = return_ObjId('https://aminoapps.com/c/mary-miraculous/page/user/imposter/eaMJ_2QFmfJVdxQJK1x3lDp8Lg8Qnb1k2sQ')
vip3 = return_ObjId()
vip4 = return_ObjId()

vips = [
        vip1,
        vip2,
        vip3,
        vip4
        
]

@Ac.event("on_text_message")
def on_text_message(data):

        
        if data.comId in coms:
              nickname = data.message.author.nickname
              cId = data.message.chatId
              text = data.message.content
              uId = data.message.author.userId
              msgId  =data.message.messageId

              Sc = Ac if data.comId==0 else SubClient(
    comId=data.comId,profile=Ac.profile)
 


              if uId in vips:
                            if text.startswith('Join?') and text.replace('Join?','') :
                                    
                                    Url = text.replace('Join?','').strip()
                                
                                    try:                                     
                                      
                                           Ac.join_chat(chatId=return_ObjId(Url)) if not return_ComId(Url)   else SubClient(
    comId=return_ComId(Url),profile=Ac.profile).join_chat(  chatId=return_ObjId(Url))
                                    except Exception as Error:
                                            print(Error)
                            if text.startswith('lev?') and text.replace('lev?','') :
                                    
                                    Url = text.replace('lev?','').strip()
                                
                                    try:                                     
                                      
                                           Ac.leave_chat(chatId=return_ObjId(Url)) if not return_ComId(Url)   else SubClient(
    comId=return_ComId(Url),profile=Ac.profile).leave_chat(  chatId=return_ObjId(Url))
                                    except Exception as Error:
                                            print(Error)
                                    
                            if text.startswith('EditT?') and text.replace('EditT?',''):
                                            
                                    try:                                     
                                        Sc.edit_chat(
                                                    title=text.replace('EditT?',''),chatId=cId
                                                    )
                                    except Exception as Error:
                                            print(Error)
                            if text =='Random?':
                                
                                    users =[]
                                    for num in range(0,400,100):users.extend(Sc.get_online_users(start=num).profile.userId)
                                    for num in range(3):
                                            user = choice(users) 
                                            users.remove(user)
                            
                                            try:
                                                
                                                Sc.invite_to_chat(userId=user,chatId=cId)
                                                Sc.send_message(message='Done!',chatId=cId,replyTo=msgId)
                                            except Exception as Error :
                                                print(str(Error))
                                    del users
 
                            if text.startswith('RandomBg?'):
     

                                    Subject = random_image(text.replace('RandomBg?','')) if text.replace('RandomBg?','') else random_image()
                                    if Subject:

                                            try:
                                                url = Sc.upload_media(
                                                            file=BytesIO(get(url=Subject).content)
                                                            ,fileType='image') 
                                                print(url)                                     
                                                Sc.edit_chat(
                                                            backgroundImage=url,chatId=cId
                                                            )
                                            except Exception as Error:
                                                    print(Error)
                                    else:
                                            Sc.send_message(message='لم يتم العثور على صورة',chatId=cId,replyTo=msgId)
                                            
    
              if text =='YourName?':
                    


                    try:
                                
                                Sc.send_message(message='Doxy',chatId=cId)
                    except Exception as Error :
                                print(str(Error))

                                
              if text.startswith('Doxy?'):
                    
                    text = text.replace('Doxy?','')  if text.replace('Doxy?','') else 'hi'
                    
                    try:
                                
                                Sc.send_message(
                                            message=str(
                                           randomReply(text)),
                                           chatId=cId,replyTo=msgId
                                           )
                    except Exception as Error :pass



              if text.startswith('DevAcc?'):
                    
                    
                    try:
                                
                                Sc.send_message(
                                            message=
                                            '''
                                            - - - - - - - - - - - \nDeveloper account : www.instagram.com/w7x7s \n- - - - - - - - - - - 
                                            '''
                                        ,
                                           chatId=cId,replyTo=msgId
                                           )
                    except Exception as Error :
                                print(str(Error))
@Ac.event("on_group_member_join")
def on_member_join(data):
    cId = data.message.chatId
    nickname = data.message.author.nickname
    uId = data.message.author.userId
    if data.comId in coms:
        if cId == ChatId:
               Sc.send_message(message=f"[c]Hello, <${nickname}$>!", chatId=cId, mentionUserIds=[uId])