from django.shortcuts import render
from .formulaires import ContactForm

def contact_view(request):
    if request.method=='post':
        nom = request.POST['nom']
        email = request.POST['email']
        password = request.POST['password']
        message = request.POST['message']
        print(nom, email, password, message)
        if len(nom)<2 or len(email)<3 or len(password)<10 or len(message)<4:
            messages.error(request,"Remplir le message correctement svp")
        else:
            contact = Contact(nom=nom, email=email, password=password, message=message)
            contact.save()
            messages.success(request, "Votre message a été bien envoyé")
    return render(request, 'contact/contact.html')

