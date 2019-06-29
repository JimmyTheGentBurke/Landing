from django.shortcuts import render
from .forms import SubscriberForm

def MainPage(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        form = form.save()

    return render(request, 'MainPage/HomePage.html', locals())


