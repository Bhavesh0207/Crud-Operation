from django.shortcuts import render, redirect
from .models import product, login, registration, carttable, ordertable
from django.contrib import messages
from django.db.models import Sum
# Create your views here.
def showproductpage(request):
    fetchprodata = product.objects.all()
    print(fetchprodata)
    context = {
        "data": fetchprodata
    }
    return render(request, "showproduct.html", context)

def addproductpage(request):
    return render(request, "addproduct.html")

def insertproductdata(request):
    proname = request.POST.get("pname")
    proprice = request.POST.get("pprice")
    prodesc = request.POST.get("pdesc")
    proimage = request.FILES["pimage"]
    insertdata = product(productname=proname, productprice=proprice, productdesc=prodesc, productimage=proimage)
    insertdata.save()
    return redirect("/")

def showmanageproduct(request):
    fetchproduct = product.objects.all()
    print(fetchproduct)
    context = {
        'data':fetchproduct
    }
    return render(request, "manageproduct.html", context)


def singleproductpage(request, pid):
    getsingledata = product.objects.get(id=pid)
    context = {
        "data": getsingledata
    }
    return render(request, "singleproduct.html", context)


def showloginpage(request):
    return render(request, "login.html")

def showregistrationpage(request):
    return render(request, "registration.html")

def insertlogindata(request):
    useremail = request.POST.get("uemail")
    userpassword = request.POST.get("upassword")
    insertdata = login(email=useremail, password=userpassword)
    insertdata.save()
    return redirect("/")

def insertregistrationdata(request):
    username = request.POST.get("name")
    useremail = request.POST.get("email")
    userpassword = request.POST.get("password")
    usergender = request.POST.get("gender")
    userphone_number = request.POST.get("phone")
    useraddress = request.POST.get("address")
    _role = request.POST.get("role")
    userprofile_picture = request.FILES["dp"]
    insertdata = registration(name=username, email=useremail, password=userpassword, gender=usergender, phone_number=userphone_number, address=useraddress, role=_role, profile_picture=userprofile_picture)
    insertdata.save()
    return redirect("/login")

def checklogindata(request):
    useremail = request.POST.get("uemail")
    userpassword = request.POST.get("upassword")
    try:
        checkuser = registration.objects.get(email=useremail, password=userpassword)
        request.session["logid"] = checkuser.id
        request.session["logname"] = checkuser.name
        request.session.save()
    except:
        checkuser = None

    if checkuser is not None:
        return redirect("/showproduct")
    else:
        print("Invalid Details")
        messages.error(request, "Invalid Email or Password. Please try again.")
    return render(request, "login.html")

def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
    except:
        pass
    return render(request, "login.html")


def addtocart(request):
    uid = request.session["logid"]  # we will get person id who is logged in right now
    quantity = request.POST.get("quantity")  # user selects the quantity
    proid = request.POST.get("pid")  # hidden field data
    proprice = request.POST.get("price")  # hidden field data
    quantity = float(quantity)
    proprice = float(proprice)
    totalamount = proprice * quantity

    # we have check if item is already added in cart or not
    try:
        checkitemincart = carttable.objects.get(userid=uid, productid=proid, cartstatus=1)
    except:
        checkitemincart = None

    if checkitemincart is None:
        storedata = carttable(userid=registration(id=uid), quantity=quantity, productid=product(id=proid), totalamount=totalamount)
        storedata.save()
    else:
        # we have to update cart
        checkitemincart.quantity += quantity
        checkitemincart.totalamount += totalamount
        checkitemincart.save()
    return redirect("/showproduct")

def showcart(request):
    uid = request.session["logid"]
    fetchcartdata = carttable.objects.filter(userid=uid, cartstatus=1)
    total_amount = fetchcartdata.aggregate(total=Sum('totalamount'))['total']
    print(total_amount)
    print(fetchcartdata)
    context = {
        "cartdata": fetchcartdata,
        "finaltotal": total_amount
    }
    return render(request, "showcart.html", context)

def increaseitem(request, id):
    getitemdetail =carttable.objects.get(id=id)
    getitemdetail.quantity += 1
    getitemdetail.totalamount += getitemdetail.productid.productprice
    getitemdetail.save()
    return redirect("/showcart")

def decreaseitem(request, id):
    getitemdetail =carttable.objects.get(id=id)
    quantity = getitemdetail.quantity
    # if quantity is 1 -- then delete item from cart
    if quantity == 1 :
        getitemdetail.delete()
    else:
        getitemdetail.quantity -= 1
        getitemdetail.totalamount -= getitemdetail.productid.productprice
        getitemdetail.save()
    return redirect("/showcart")

def removeitem(request, id):
    fetchitemfromcart = carttable.objects.get(id=id)
    # fetchitemfromcart.delete() -- if you want to delete data from carttable
    fetchitemfromcart.cartstatus = 0
    fetchitemfromcart.save()
    return redirect("/showcart")


def fetchorderdetails(request):
    uid = request.session["logid"]
    name = request.POST.get("uname")
    address = request.POST.get("address")
    finaltotal = request.POST.get("finaltotal")
    payment = request.POST.get("payment")

    storedata = ordertable(userid=registration(id=uid), finaltotal=finaltotal, paymode=payment, name=name, address=address)
    storedata.save()
    messages.success(request, "Order Placed Successfully")
    return  redirect("/showproduct")


def showprofile(request):
    uid = request.session["logid"]
    fetchuserdata = registration.objects.get(id=uid)
    context = {
        "userdata":fetchuserdata
    }
    return render(request, "showprofile.html", context)


def editproduct(request, id):
    getdata = product.objects.get(id=id)
    context = {
        "data" : getdata
    }
    return render(request, "showproduct.html", context)


def updateproduct(request):
    pid = request.POST.get("pid")
    pname = request.POST.get("pname")
    pprice = request.POST.get("pprice")
    pdesc = request.POST.get("pdesc")
    pimage = request.FILES["pimage"]

    getdata = product.objects.get(id=pid)
    getdata.name = pname
    getdata.price = pprice
    getdata.description = pdesc
    getdata.proimage = pimage
    getdata.save()
    return redirect("/manageproduct")


def forgotpassword(request):
    return render(request, "login.html")


def forgotpage(request):
    return render(request, "forgotpassword.html")


