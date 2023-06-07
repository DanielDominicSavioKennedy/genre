from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .metadata import getdata
from .predict import predict_genre

def home(request):
    return render(request,"home.html")

def classify(request):
    if request.method == 'POST':
        uploadfile = request.FILES['document']
        #print(uploadfile.name)
        print(uploadfile.size)
        
        if not uploadfile.name.endswith('.wav'):
            messages.error(request,'Only .wav file type is allowed')
            return redirect(classify)

        meta = getdata(uploadfile)
        pred=predict_genre(meta)
        return render(request,'classify.html',{"result":pred[0]})
    else:
        return render(request,'classify.html')

