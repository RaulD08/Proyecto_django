from django.shortcuts import render, redirect
from web.models import *
from web.forms import MainForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import connection
from django.db.models import QuerySet

from django.core.paginator import Paginator

# Create your views here.

def index(request):

    redir = request.session.get('redir')
    if redir:
         list = request.session.get('list')
    else:
        list = []
    if list != []:
        request.session['id_orden_buscado'] = ''
        request.session['envio_inicio_buscada'] = ''
        request.session['envio_final_buscada'] = ''
        request.session['ciudad_buscada'] = ''
        id_orden_buscado = list[0]
        envio_inicio_buscada = list[1]
        envio_final_buscada = list[2]
        ciudad_buscada = list[3]
        if id_orden_buscado != '':
            datos = Salesorderheader.objects.filter(salesorderid__startswith=id_orden_buscado).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            print('en primer paso')
            request.session['id_orden_buscado'] = id_orden_buscado
            return redirect('/filtro')

        elif envio_inicio_buscada != '' and envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__range=(envio_inicio_buscada, envio_final_buscada)).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            request.session['envio_inicio_buscada'] = envio_inicio_buscada
            request.session['envio_final_buscada'] = envio_final_buscada
            return redirect('/filtro')

        elif envio_inicio_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__gte=envio_inicio_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            request.session['envio_inicio_buscada'] = envio_inicio_buscada
            return redirect('/filtro')

        elif envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__lte=envio_final_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            request.session['envio_final_buscada'] = envio_final_buscada
            return redirect('/filtro')

        elif ciudad_buscada != '':
            datos = Salesorderheader.objects.filter(shiptoaddressid__city__icontains=ciudad_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            request.session['ciudad_buscada'] = ciudad_buscada
            return redirect('/filtro')
    
    if request.method == 'POST':
        id_orden_buscado = request.POST.get('id_orden_selector')
        envio_inicio_buscada = request.POST.get('envio_inicio_selector')
        envio_final_buscada = request.POST.get('envio_final_selector')
        ciudad_buscada = request.POST.get('ciudad_selector')
        #print(id_orden_buscado, envio_inicio_buscada, envio_final_buscada, ciudad_buscada)
        request.session['id_orden_buscado'] = id_orden_buscado
        request.session['envio_inicio_buscada'] = envio_inicio_buscada
        request.session['envio_final_buscada'] = envio_final_buscada
        request.session['ciudad_buscada'] = ciudad_buscada
    
        if id_orden_buscado != '':
            datos = Salesorderheader.objects.filter(salesorderid__startswith=id_orden_buscado).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            return redirect('/filtro')

        elif envio_inicio_buscada != '' and envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__range=(envio_inicio_buscada, envio_final_buscada)).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            return redirect('/filtro')

        elif envio_inicio_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__gte=envio_inicio_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            return redirect('/filtro')

        elif envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__lte=envio_final_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            return redirect('/filtro')

        elif ciudad_buscada != '':
            datos = Salesorderheader.objects.filter(shiptoaddressid__city__icontains=ciudad_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            return redirect('/filtro')

        else:
            datos = Salesorderheader.objects.all().values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            request.session['list'] = []
            return redirect('/')
        
    else:
        datos = Salesorderheader.objects.all().values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
    
    pag = Paginator(datos, 10)
    pagina = request.GET.get('pagina')
    dato = pag.get_page(pagina)

    context = {
        'orden': datos,
        'form': MainForm(),
        'dato': dato,
        }
    return render(request, 'tabla.html', context)



def filtro(request):
    
    if request.user.is_authenticated:

        request.session['redir'] = False
        id_orden_buscado = request.session.get('id_orden_buscado')
        envio_inicio_buscada = request.session.get('envio_inicio_buscada')
        envio_final_buscada = request.session.get('envio_final_buscada')
        ciudad_buscada = request.session.get('ciudad_buscada')

        if id_orden_buscado != '':
            datos = Salesorderheader.objects.filter(salesorderid__startswith=id_orden_buscado).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')

        elif envio_inicio_buscada != '' and envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__range=(envio_inicio_buscada, envio_final_buscada)).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
        
        elif envio_inicio_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__gte=envio_inicio_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
        
        elif envio_final_buscada != '':
            datos = Salesorderheader.objects.filter(shipdate__lte=envio_final_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
        
        elif ciudad_buscada != '':
            datos = Salesorderheader.objects.filter(shiptoaddressid__city__icontains=ciudad_buscada).values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')

        else:
            datos = Salesorderheader.objects.all().values('salesorderid', 'orderdate', 'shipdate', 'shiptoaddressid__addressline1', 'shiptoaddressid__addressline2', 'shiptoaddressid__city')
            

        if request.method == 'POST':

            id_orden_buscado = request.POST.get('id_orden_selector')
            envio_inicio_buscada = request.POST.get('envio_inicio_selector')
            envio_final_buscada = request.POST.get('envio_final_selector')
            ciudad_buscada = request.POST.get('ciudad_selector')
            list = [id_orden_buscado, envio_inicio_buscada, envio_final_buscada, ciudad_buscada]
            request.session['list'] = list
            request.session['redir'] = True
            return redirect('/')
        
        pag = Paginator(datos, 7)
        pagina = request.GET.get('pagina')
        dato = pag.get_page(pagina)
        resultados = datos.count()

        context = {
            'form': MainForm(),
            'dato': dato,
            'resultados': resultados,
            }

        return render(request, 'filtro.html', context)
    
    else:
        return redirect('/')


def login_view(request):

    if request.user.is_authenticated == False:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info (request, f"Iniciaste sesión como: {username}")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Usuario o contraseña inválido.")
            else:
                messages.error(request, "Usuario o contraseña inválido.")
        
        form = AuthenticationForm()
        context = {
            'login_form' : form,
        }
        return render(request, "login.html", context)
    else:
        messages.info(request, "Ya ha iniciado sesión.")
        return HttpResponseRedirect('/')
    
    
def logout_view(request):
    logout(request)
    messages.success(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')