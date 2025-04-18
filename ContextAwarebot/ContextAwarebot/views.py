from django.shortcuts import render
from aiengine.ml.main import Result, Model

def home(request):
    if request.method == 'POST':
        prompt=request.POST.get('prompt')
        Domain= Result(prompt)
        response = Model(prompt, Domain)
        return render(request, 'index.html', {'response': 'response'})
    else:
        return render(request, 'index.html')