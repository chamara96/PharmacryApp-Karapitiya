from firebase import firebase

firebase = firebase.FirebaseApplication('https://pharmacy-test1.firebaseio.com/', None)

data =  { 'id': '',
          'name': 'test user A',
          'tele': '0701234567',
          'address': "D100, AA, BB, CC",
          'lat':7.284246,
          'lng':80.626552,
          'password':"pass123"
          }

# result = firebase.post('/client_user/',data)
# print("added")
# print(result)
# firebase.put('/client_user/'+result["name"],'id',result["name"])
# print("updated")

result = firebase.get('/client_user/', '')
print(result)
