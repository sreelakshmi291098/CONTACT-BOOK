from django.shortcuts import render,redirect

from app17.models import Contact

# Create your views here.
def index(request):
    Data=Contact.objects.all()
    return render(request,'index.html', {'Data': Data})
def contact(request):
    return render(request,'contact.html')
def addcontact(request):
    return render(request,'addcontact.html')



def saveinfo(request):
    if request.method=="POST":
        Firstname=request.POST['first_name']
        Phonenumber=request.POST['phone']
        add=Contact(Firstname=Firstname,Phonenumber=Phonenumber)
        add.save()
        Data=Contact.objects.all()
    
        return render(request, 'index.html',{'Data': Data})
        
    else:
        return render(request, 'addcontact.html')

def formupdate(request,id):
    if request.method=="POST":
        add=Contact.objects.get(id=id)
        add.Firstname=request.POST["first_name"]
        add.Phonenumber=request.POST["phone"]
        add.save()
        return redirect("index")

def edit(request,id):
    Data=Contact.objects.get(id=id)
    return render(request,'edit.html',{'Data':Data})
    
def delete(request,id):
    add=Contact.objects.get(id=id)
    add.delete()
    return redirect('index')

def search(request):
    query=request.GET["query1"]
    Data=Contact.objects.filter(Phonenumber__icontains=query)
    params={'Data':Data}
    return render(request,'search.html',params)
    

