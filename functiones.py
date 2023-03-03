###

'''
ملف المودل
'''


##



from helper import *


def upload(FileName:str='',Url:str=''):

    if FileName or Url:
        try:

                image_read = get(
                    url=Url
                    ).content if Url else open(
                        FileName
                        ,
                        "rb"
                        ).read()
                image_64_encode = encodebytes(
                    image_read
                    )
                data = {'key':"a82a4185e66f0e0c171fab6abb10786e",
                    'image':image_64_encode,
                    'name':'support supra',
                    'expiration': 60  }
                headers = {
                    'Accept': 'application/json'
                    }
                response = post(
                    url='https://api.imgbb.com/1/upload'
                    ,
                    data=data
                    ,
                    headers=headers)
                return response.json()['data']['url']

        except Exception as WrongResponse:
            print("WrongResponse",WrongResponse)
 




def random_image(subject:str='anime'):

            Url     = f"https://api.pinterest.com/v3/search/pins/?query={subject}&page_size=250"

            headers ={
                'authorization':
                'Bearer MTQzMTYwMjoxMDk2Njk3MDg0MTY3MzkyODI4OjkyMjMzNzIwMzY4NTQ3NzU4MDc6MXwxNjQxNzU4OTk5OjAtLTE4MjQxYmM3NTI4ZTEzYWE5YTAxODFkY2M0NTI4OWYx'
                , 
                'content-type':'application/x-www-form-urlencoded'}
            
            response = get(
                url=Url
                ,
                headers=headers)
            try:
                  return loads(response.text)["data"][0]['image_large_url']
            except:
                  try:
                        return choice(loads(response.text)["data"])['image_large_url']
                  except:
                        return False



def removeBackground(Url:str):
    response1 = get(
		url=Url
		).content

    response2 = post(
		url= 'https://api.remove.bg/v1.0/removebg',
		files ={'image_file': response1},
		data ={'size': 'auto'}
		,
		headers=
		{'X-Api-Key': "x9MCRGHgv3hPDthtNN2CWueC"})

    if response2:
        with open(  f"{images}no-bg.png", 'wb') as image:
            image.write(
                response2.content
                )
        return image.name

	 
			
def randomReply(text: str, lang: str="en"):
        params = {
            "msg":text
            }

        response = get(
            url = f"http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1" 
            ,
            params=params
            )
            
        if response.status_code==200:
            return str(response.json().get("cnt"))
        else:
            return response.text



def translate(text: str, From: str, to: str) -> str:

	text = text.strip().replace(' ', '%20')

	headers = {
		'User-Agent': 'curl/7.35.0'
		, 
		'Host': 'translate.googleapis.com'
		, 'Accept': '*/*'
		}
	Url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={From}&tl={to}&dt=t&dj=1&q={text}'

	response = get(
		url=Url
		,
		headers=headers).json()

	return response['sentences'][0]['trans']

def return_ObjId(Url:str=''):
      if Url:
           return Client.get_from_code(Client(),code=Url).objectId

      
def return_ComId(Url:str=''):
      if Url:
           return Client.get_from_code(Client(),code=Url).comId


