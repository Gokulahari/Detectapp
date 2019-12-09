import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyD1F03SqagQY1Fj9ghix5rhAX0H3EOrVRk",
    "authDomain": "grocery-7a56e.firebaseapp.com",
    "databaseURL": "https://grocery-7a56e.firebaseio.com",
    "projectId": "grocery-7a56e",
    "storageBucket": "grocery-7a56e.appspot.com",
    "messagingSenderId": "61264205453",
    "appId": "1:61264205453:web:af51ade5f61bb79e1034c4"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
dat = {}
if db.child("Product_Details").child("tomato").get().val():
    db.child("Product_Details").child("tomato").remove()
else:
    print("not exist")

# for i in p:
#     print(p[i])

# data = {"Brinjal":14}
#
# db.child("Product_Details").update(data)





