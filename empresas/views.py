from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from empresas.models import *
from empresas.forms import *
from django.contrib import messages


# Create your views here.
def administracion(request):

    return render(request, 'admin/index.html')


def historia(request):
    form_historia = HistoriaForm()
    if request.method == 'POST':
        form_historia = HistoriaForm(request.POST, request.FILES)
        if form_historia.is_valid():
            form_historia.save()
            messages.info(request, "La historia fue creada con éxito")
            return redirect('empresas:historia')
        else:
            messages.error(request, historia.errors )
            context = {
                'form_historia':form_historia,
            }
    context = {
        'form_historia':form_historia,
    }
    return render(request, 'admin/empresas/historia_form.html', context)

def historia_list(request):
    historias = Historia.objects.all()
    context = {
        'historias':historias
    }
    return render(request, 'admin/empresas/historias_list.html', context)

def historia_edit(request, pk):
    historia = Historia.objects.get(pk=pk)
    form_historia = HistoriaForm(instance = historia)
    if request.method == 'POST':
        form_historia = HistoriaForm(request.POST, request.FILES, instance = historia)
        if form_historia.is_valid():
            form_historia.save()
            messages.info(request, "La historia se editó con éxito")
            return redirect('empresas:historia_list')
        else:
            messages.error(request, historia.errors)
            context = {
                'form_historia': form_historia,
            }
            return render(request, 'admin/empresas/historia_form.html', context)

    context = {
        'form_historia': form_historia,
    }
    return render(request, 'admin/empresas/historia_form.html', context)


class HistoriaDetail(DetailView):
    model = Historia
    template_name = 'admin/empresas/historia_detail.html'

class HistoriaDelete(DeleteView):
    model = Historia
    template_name = 'admin/empresas/historia_confirm_delete.html'
    success_url = reverse_lazy('empresas:historia_list')

def team(request):
    form_team = TeamForm()
    if request.method == 'POST':
        form_team = TeamForm(request.POST, request.FILES)
        if form_team.is_valid():
            form_team.save()
            messages.info(request, "El miembro del equipo fue creado con éxito")
            return redirect('empresas:team_list')
        else:
            messages.error(request, team.errrors)
            context = {
                'form_team':form_team,
            }
    context = {
        'form_team':form_team,
    }
    return render(request, 'admin/empresas/team_form.html', context)

def team_list(request):
    teams = Team.objects.all()
    context = {
        'teams':teams
    }
    return render(request, 'admin/empresas/team_list.html', context)

def team_edit(request, pk):
    team = Team.objects.get(pk=pk)
    form_team = TeamForm(instance = team)
    if request.method == 'POST':
        form_team = TeamForm(request.POST, request.FILES, instance = team)
        if form_team.is_valid():
            form_team.save()
            messages.info(request, "El miembro del team se editó con éxito")
            return redirect('empresas:team_list')
        else:
            messages.error(request, team.errors)
            context = {
                'form_team': form_team,
            }
            return render(request, 'admin/empresas/team_form.html', context)

    context = {
        'form_team': form_team,
    }
    return render(request, 'admin/empresas/team_form.html', context)


class TeamDetail(DetailView):
    model = Team
    template_name = 'admin/empresas/team_detail.html'

class TeamDelete(DeleteView):
    model = Team
    template_name = 'admin/empresas/team_confirm_delete.html'
    success_url = reverse_lazy('empresas:team_list')


def plan(request):
    form_plan = PlanForm()
    if request.method == 'POST':
        form_plan = PlanForm(request.POST, request.FILES)
        if form_plan.is_valid():
            form_plan.save()
            messages.info(request, "El item del plan corporativo fue creado con éxito")
            return redirect('empresas:plan_list')
        else:
            messages.error(request, plan.errrors)
            context = {
                'form_plan':form_plan,
            }
    context = {
        'form_plan':form_plan,
    }
    return render(request, 'admin/empresas/plan_form.html', context)

def plan_list(request):
    planes = Plan.objects.all()
    context = {
        'planes':planes
    }
    return render(request, 'admin/empresas/plan_list.html', context)

def plan_edit(request, pk):
    plan = Plan.objects.get(pk=pk)
    form_plan = PlanForm(instance = plan)
    if request.method == 'POST':
        form_plan = PlanForm(request.POST, request.FILES, instance = plan)
        if form_plan.is_valid():
            form_plan.save()
            messages.info(request, "El item del plan corporativo se editó con éxito")
            return redirect('empresas:plan_list')
        else:
            messages.error(request, plan.errors)
            context = {
                'form_plan': form_plan,
            }
            return render(request, 'admin/empresas/plan_form.html', context)

    context = {
        'form_plan': form_plan,
    }
    return render(request, 'admin/empresas/plan_form.html', context)


class PlanDetail(DetailView):
    model = Plan
    template_name = 'admin/empresas/plan_detail.html'

class PlanDelete(DeleteView):
    model = Plan
    template_name = 'admin/empresas/plan_confirm_delete.html'
    success_url = reverse_lazy('empresas:plan_list')
