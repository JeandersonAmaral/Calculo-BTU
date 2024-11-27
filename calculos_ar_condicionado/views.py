from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import AmbienteForm, CamadaForm
from .models import Ambiente, Camada
from django.urls import reverse


def lista(request):
    if request.method == "GET":
        ambientes = Ambiente.objects.all()
        context = {
            'lista': ambientes,
        }
        return render(request, "resultado.html", context)


def criar_ambiente(request):
    if request.method == 'GET':
        ambiente_form = AmbienteForm()
        camada_formset = inlineformset_factory(Ambiente, Camada, form=CamadaForm, extra=1)
        form_camada = camada_formset()
        context = {
            'ambiente_form': ambiente_form,
            'form_camada': form_camada,
        }
        return render(request, "criar_ambiente.html", context)

    elif request.method == "POST":
        ambiente_form = AmbienteForm(request.POST)
        camada_formset = inlineformset_factory(Ambiente, Camada, form=CamadaForm)
        form_camada = camada_formset(request.POST)  

        if ambiente_form.is_valid() and form_camada.is_valid():
            ambiente = ambiente_form.save()
            form_camada.instance = ambiente
            form_camada.save()

            resistencia_total = sum(camada.calcular_resistencia() for camada in ambiente.camadas.all())
            context = {
                'ambiente_form': ambiente_form,  
                'form_camada': form_camada, 
                'resistencia_total': resistencia_total,
            }
            return redirect(reverse('listar')) 

        else:
            context = {
                'ambiente_form': ambiente_form,
                'form_camada': form_camada, 
            }
            return render(request, "criar_ambiente.html", context)  


def editar(request, ambiente_id):
    if request.method == "GET":
        objeto = Ambiente.objects.filter(id=ambiente_id).first()
        if objeto is None:
            return redirect(reverse('listar'))
        ambiente_form = AmbienteForm(instance=objeto)
        camada_formset = inlineformset_factory(Ambiente, Camada, form=CamadaForm, extra=1)
        form_camada = camada_formset(instance=objeto)
        context = {
            'ambiente_form': ambiente_form,
            'form_camada': form_camada,
        }
        return render(request, "criar_ambiente.html", context)
    elif request.method == "POST":
        objeto = Ambiente.objects.filter(id=ambiente_id).first()
        if objeto is None:
            return redirect(reverse('listar'))
        ambiente_form = AmbienteForm(request.POST, instance=objeto)
        camada_formset = inlineformset_factory(Ambiente, Camada, form=CamadaForm)
        form_camada = camada_formset(request.POST, instance=objeto)
        if ambiente_form.is_valid() and form_camada.is_valid():
            ambiente = ambiente_form.save()
            form_camada.instance = ambiente
            form_camada.save()
            return redirect(reverse('listar'))
        else:
            context = {
                'ambiente_form': ambiente_form,
                'form_camada': form_camada,
            }
            return render(request, "criar_ambiente.html", context)
