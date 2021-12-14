from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage, send_mail

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method == "POST":
         formulario_contacto=FormularioContacto(data=request.POST)
         if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django", "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n".format(nombre, email, contenido), 
                "", ["gsantiesteban@sifizsoft.com"], reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto?valido")
            except:
                return redirect("/contacto?novalido")

    return render(request, 'contacto/contacto.html', {"mi_formulario": formulario_contacto})
