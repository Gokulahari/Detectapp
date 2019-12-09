from django.shortcuts import HttpResponse,render
# from .models import Student
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

dic = {}
def home(request):
    if request.method == 'POST':
        if (request.POST.get('click')):
            p_name = request.POST.get('nam').capitalize()
            # p_name = p_name.capitalize()
            # p_id = request.POST.get('ii')
            p_price = request.POST.get('rs')
            if p_name and p_price:
                dic[p_name] = p_price
                db.child("Product_Details").update(dic)
                # ins = Student(pro_name=p_name, pro_price=p_price)
                # ins.save()
                return render(request, 'web/main.html',{'k':"Added Successfully"})
            else:
                return render(request, 'web/main.html', {'k': "Fill the product name and price"})
            # return HttpResponse(fol)

        elif(request.POST.get('click1')):
            p_name = request.POST.get('nam').capitalize()
            if p_name:
                if db.child("Product_Details").child(p_name).get().val():
                    db.child("Product_Details").child(p_name).remove()
                    return render(request, 'web/main.html', {'k': "Deleted Successfully"})
                else:
                    res = "No Product named as "+p_name
                    return render(request, 'web/main.html', {'k':res})
            else:
                return render(request, 'web/main.html', {'k': "Enter the Product to delete"})
        elif (request.POST.get('click2')):
            # data = {}
            # p = Student.objects.all()
            # data["prod"] = p
            # data["prod"] = p



            p = db.child("Product_Details").get().val()
            return render(request, 'web/product.html',{'data':p})

        elif (request.POST.get('click4')):
            # ref = db.reference('Orders')
            # ans = ref.get()

            return render(request, 'web/orders.html')

    p = db.child("Product_Details").get().val()
    return render(request, "web/main.html", {"w": p})


    # data = Student.objects.all()
    # return HttpResponse(data)
    # # for i in data:
    # #     l.append(i.name)


