from django.shortcuts import HttpResponse,render
from .models import Student
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
        './firebase-admin-sdk.json')
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://grocery-7a56e.firebaseio.com'
    })
def home(request):
    if request.method == 'POST':
        if (request.POST.get('click')):
            p_name = request.POST.get('nam')
            # p_id = request.POST.get('ii')
            p_price = request.POST.get('rs')
            if p_name and p_price:
                ins = Student(pro_name=p_name, pro_price=p_price)
                ins.save()
                return render(request, 'web/main.html',{'k':"Added Successfully"})
            else:
                return render(request, 'web/main.html', {'k': "Fill the product name and price"})
            # return HttpResponse(fol)

        elif(request.POST.get('click1')):
            p_name = request.POST.get('nam')
            if p_name:
                Student.objects.filter(pro_name=p_name).delete()
                return render(request, 'web/main.html', {'k': "Deleted Successfully"})
            else:
                return render(request, 'web/main.html', {'k': "Enter the product Name to delete"})

        elif (request.POST.get('click2')):
            data = {}
            p = Student.objects.all()
            data["prod"] = p
            return render(request, 'web/product.html',data)

        elif (request.POST.get('click4')):
            ref = db.reference('Orders')
            ans = ref.get()

            return render(request, 'web/orders.html',{'k':ans})














    data = Student.objects.all()
    # return HttpResponse(data)
    # # for i in data:
    # #     l.append(i.name)
    return render(request,"web/main.html",{"w":data})

