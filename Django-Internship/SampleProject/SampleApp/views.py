from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmployeeData

# Create your views here.

def hello(request):
	return HttpResponse("<h1>Hello guys welcome to django internship</h1>")


def sam(request):
	return HttpResponse("<h2 style=color:green;background-color:yellow;font-size:45px><center>Django Internship</center></h2>")

def dynamic(request,id):
	return HttpResponse("<h2><center>My Rollnumber is:{}</center></h2>".format(id))

def data(request,name):
	return HttpResponse("<h1 style=color:navy;background-color:green;font-style:italic><center>My Name is :{}</center></h1>".format(name))

def task(request,a,b):
	return HttpResponse("<h2><center>my rollnumber is:{} and my name is:{}</center></h2>".format(a,b))


def table(request):
	return render(request,'table.html',{})


def det(request,id,name):
	return render(request,'details.html',{'i':id,'n':name})


def external(request):
	if request.method=="POST":
		na=request.POST['uname']
		mb=request.POST['mbl']
		em=request.POST['eml']
		ps=request.POST['psw']
		cps=request.POST['cpsw']
		# print(na,mb,em,ps,cps)
		return render(request,'data.html',{'n':na,'m':mb,'e':em,'p':ps,'cp':cps})

	return render(request,'external.html')

def boot(request):
	return render(request,'boot.html')

def btp(request):
	return render(request,'bt/home.html')

#def crud(request):
#	return render(request,'bt/crudoperations.html')

def crud(request):
	p = EmployeeData.objects.all()
	if request.method == "POST":
		a = request.POST['ei']
		b = request.POST['en']
		c = request.POST['ed']
		d = request.POST['ea']
		t = EmployeeData(eid=a,ename=b,edesg=c,eage=d)
		t.save()
		return redirect('/')
	return render(request,'bt/crudoperations.html',{'z':p})

def emupdate(request,r):
	m = EmployeeData.objects.get(id=r)
	if request.method == "POST":
		m.eid = request.POST['ei']
		m.ename = request.POST['en']
		m.edesg = request.POST['ed']
		m.eage = request.POST['ea']
		m.save()
		return redirect('/')
	return render(request,'bt/emupdate.html',{'n':m})

def emdel(request,y):
	k = EmployeeData.objects.get(id=y)
	if request.method == "POST":
		k.delete()
		return redirect('/')
	return render(request,'bt/emdel.html',{'s':k})
