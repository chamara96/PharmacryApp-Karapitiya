from firebase import firebase

firebase = firebase.FirebaseApplication('https://pharmacy-test1.firebaseio.com/', None)

data =  { 'id': '',
          'name': 'Pharm A',
          'owner':'Mr ABC',
          'tele': '0701234567',
          'address': "D100, AA, BB, CC",
          'lat':7.268318,
          'lng':80.597409,
          'password':"pass123"
          }

# result = firebase.post('/pharm_user/',data)
# print("added")
# print(result)
# firebase.put('/pharm_user/'+result["name"],'id',result["name"])

print("updated")