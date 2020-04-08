from firebase import firebase

firebase = firebase.FirebaseApplication("https://pharmacy-test1.firebaseio.com")
result = firebase.get('/client_user', '')
username="0702697490"
data={'-M3qjcYthQ02dfPMdaTl': {'address': 'D100, AA, BB, CC', 'id': '-M3qjcYthQ02dfPMdaTl', 'lat': 7.284246, 'lng': 80.626552, 'name': 'test user A', 'password': 'pass123', 'tele': '0701234567'}, '-M3r6J3X2_Zp7_sDVC6t': {'address': 'Morawaka,Nelundeniya', 'id': '-M3r6J3X2_Zp7_sDVC6t', 'lat': '7.123456', 'lng': '80.987654', 'name': 'chamara', 'password': 'mypass123', 'tele': '0702697490'}}
for i in data:
    if data[i]["tele"]==username:
        output=data[i]
    else:output={"login":"false"}
print(output)