from django.shortcuts import render
from .models import Registration

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        Registration.objects.create(name=name, email=email, phone_number=phone_number)

    return render(request, 'registrations/register.html')

