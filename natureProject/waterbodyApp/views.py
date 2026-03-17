from django.shortcuts import render, redirect
from .forms import OceanForm, LakeForm
from .models import Ocean, Lake

def home(request):
    oceans = Ocean.objects.all()
    context = {"oceans":oceans}
    return render(request,'waterbodyApp/oceans.html',context)

# Create your views here.
def createOcean(request):
    form = OceanForm() # get an instance of the Ocean form
    if request.method == 'POST':
        form = OceanForm(request.POST) # get what the user has input
        if form.is_valid():  #validate the form to ascetain the input have been dne well
            form.save()
            return redirect('read-oceans') 
        else:
            print("kejljwejlwjlkwje=====")
    context = {'form':form}
    return render(request, 'waterbodyApp/form.html', context)


def readOceans(request):
    oceans = Ocean.objects.all()
    context = {"oceans": oceans}
    return render(request, 'waterbodyApp/oceans.html', context)

def readOcean(request,pk):
    ocean = Ocean.objects.get(id=pk)
    context = {"ocean": ocean}
    return render(request, 'waterbodyApp/ocean.html', context)

def updateOcean(request,pk):
    ocean = Ocean.objects.get(id=pk)
    form = OceanForm(instance = ocean)
    if request.method == 'POST':
        form = OceanForm(request.POST, instance= ocean)
        if form.is_valid():
            ocean.save()
            return redirect('read-oceans')
    context = { "form":form}
    return render(request,'waterbodyApp/form.html', context)

def deleteOcean(request, pk):
    ocean = Ocean.objects.get(id=pk)
    ocean.delete()  
    return redirect('read-oceans')


def createLake(request):
    form = LakeForm() # get an instance of the Ocean form
    if request.method == 'POST':
        form = LakeForm(request.POST) # get what the user has input
        if form.is_valid():  #validate the form to ascetain the input have been dne well
            form.save()
        return redirect('read-lakes') 
    
    context = {'form':form}
    return render(request, 'waterbodyApp/form.html', context)

def readLakes(request):
    lakes = Lake.objects.all()
    context = {"lakes": lakes}
    return render(request, 'waterbodyApp/lakes.html', context)
     
def readLake(request,pk):
    lake = Lake.objects.get(id=pk)
    context = {"lake": lake}
    return render(request, 'waterbodyApp/lake.html', context)

def updateLake(request, pk):
    lake = Lake.objects.get(id=pk)
    form = LakeForm(instance = lake)
    if request.method  == 'POST':
        form = LakeForm(request.POST, instance= lake)
        if form.is_valid():
            form.save()
            return redirect('read-lakes')

    context = {"form": form}
    return render(request, 'waterbodyApp/form.html', context)

def deleteLake(request, pk):
    lake = Lake.objects.get(id=pk)
    lake.delete()  
    return redirect('read-lakes')

