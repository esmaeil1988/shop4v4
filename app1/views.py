from django.shortcuts import render,redirect
from.models import category,product,client,cart,picture,contact,faktor,faktor_details
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from.forms import *


# Create your views here.
def home(request):
    l=category.objects.all()
    return render(request,'app1/index.html',context={"cats":l})


def contactus(request):
    er=[]
    if request.method=="POST":
        f=fcontact(request.POST)
        if f.is_valid()==False:
            er.append("فرم معتبر نیست")
        else:
            n=f.cleaned_data["fname"]
            fa=f.cleaned_data["lname"]
            e=f.cleaned_data["email"]
            a=f.cleaned_data["address"]
            ph=f.cleaned_data["phonenumber"]
            c=f.cleaned_data["content"]
            contact.objects.create(fname=n,lname=fa,email=e,address=a,phonenumber=ph,content=c)
            f=fcontact()
    else:
        f=fcontact()  
    return render(request,'app1/contact.html',{"f":f,"er":er})


def allprod(request):
    d={"k":product.objects.all()}
    tt=request.GET.get("tt")
    if(tt):
        d={"k":product.objects.filter(title__contains=tt)}
    return render(request,'app1/allprod.html',context=d)
    



def showprod(request,adad):
    l=product.objects.get(id=adad)
    aks=picture.objects.filter(product_id=adad)
    return render(request,'app1/product.html',context={"prd":l,"aks":aks})


def showcategory(request,adad):
    l1=category.objects.get(id=adad)
    l2=product.objects.filter(category=l1)
    return render(request,'app1/category.html',context={"cy":l1,"cp":l2})






def error(request):
    return render(request,"app1/404.html")


def sc(request):
    return render(request,"app1/sc.html")


def reg(request):
    if (request.method=="POST"):
        status=False
        context={"errors":[]}
        f=request.POST.get("fname")
        l=request.POST.get("lname")
        e=request.POST.get("email")
        u=request.POST.get("username")
        p=request.POST.get("password")
        rp=request.POST.get("rpassword")
        if len(p)<6:
            status=True
            context["errors"].append("کلمه عبور باید بیشتر از 6 کاراکتر باشد!")
        if p!=rp:
            status=True
            context["errors"].append("کلمه عبور و تکرار کلمه عبور یکسان نیستند!")
        if(status==False):
            client.objects.create(firstname=f,lastname=l,username=u, password=p)
            return redirect("/success/")
        else:
            return render(request,"app1/register.html",context=context)

    return render(request,"app1/register.html")



def login(request):
    if (request.session.get("login")):
        return redirect("/")
    
    if (request.method=="POST"):
        u=request.POST.get("username")
        p=request.POST.get("password")
        usr=client.objects.filter(username=u,password=p)
        if (usr):
            request.session["login"]=u
            return redirect("/")
        else:
            return redirect("/error/")
    return render(request,"app1/login.html")


def lout(request):
    del request.session["login"]
    return redirect ("/")


def addtocart(request,adad):
    if (request.session.get("login")):
        cl=client.objects.get(username=request.session.get('login'))
        pr=product.objects.get(id=adad)
        sb=cart.objects.filter(client=cl,product=pr).first()
        if sb==None:
            cart.objects.create(client=cl,product=pr,qnt=1)
        else:
            sb.qnt=sb.qnt+1
            sb.save()
        return redirect('/cart/')
    else:
        return redirect('/login/')
    

def delcart(request,adad):
    if (request.session.get("login")):
        cl=client.objects.get(username=request.session.get('login'))
        pr=product.objects.get(id=adad)
        sb=cart.objects.filter(client=cl,product=pr)
        sb.delete()
        return redirect('/cart/')
    else:
        return redirect('/login/')



def editqnt(request,adad):
    if (request.session.get("login")):
        cl=client.objects.get(username=request.session.get('login'))
        pr=product.objects.get(id=adad)
        qnt=request.POST.get('qnt')
        sb=cart.objects.filter(client=cl,product=pr).first()
        sb.qnt=qnt
        sb.save()
        return redirect('/cart/')
    else:
        return redirect('/login/')



def showcart(request):
    if (request.session.get("login")):
       cl=client.objects.get(username=request.session.get('login'))
       p=cart.objects.filter(client=cl,)
       t=0
       for item in p:
           t=t+item.product.price*item.qnt

       return render(request,'app1/cart.html',{'p':p,"t":t})
    else:
        return redirect('/')
    

