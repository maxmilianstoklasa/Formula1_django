from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from formula1.forms import DriverModelForm
from formula1.models import *


def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Uložení celkového počtu filmů v databázi do proměnné num_films
    num_drivers = Driver.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    drivers = Driver.objects.order_by('teams')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_drivers': num_drivers,
        'drivers': drivers
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


class DriverList(ListView):
    model = Driver

    context_object_name = 'driver_list'
    template_name = 'racer/list.html'
    paginate_by = 3

    def get_queryset(self):
        if 'constructor_name' in self.kwargs:
            return Driver.objects.filter(
                teams__name=self.kwargs['constructor_name']).all()
        else:
            return Driver.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_drivers'] = len(self.get_queryset())
        if 'constructor_name' in self.kwargs:
            context['view_title'] = f"Team: {self.kwargs['constructor_name']}"
            context['view_head'] = f"Driver's team: {self.kwargs['constructor_name']}"
        else:
            context['view_title'] = 'Drivers'
            context['view_head'] = 'Drivers overview'
        return context


class DriverDetail(DetailView):
    model = Driver

    context_object_name = 'driver_detail'
    template_name = 'racer/detail.html'


""" class CircuitList(ListView):
    model = Circuit

    context_object_name = 'circuit_list'
    template_name = 'circuit/list.html'
    paginate_by = 3

    def get_queryset(self):
        if 'driver_name' in self.kwargs:
            return Circuit.objects.filter(
                winner__name=self.kwargs['driver_name']).all()
        else:
            return Circuit.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if 'driver_name' in self.kwargs:
            context['view_title'] = f"Team: {self.kwargs['driver_name']}"
            context['view_head'] = f"Driver's team: {self.kwargs['driver_name']}"
        else:
            context['view_title'] = 'Circuits'
            context['view_head'] = 'Circuits overview'
        return context """


class DriverCreateView(CreateView):
    model = Driver
    fields = ['name', 'poster', 'nationality', 'birth', 'teams', 'driver_wins', 'wdc', 'biography']


class DriverUpdateView(UpdateView):
    model = Driver
    #fields = '__all__'
    form_class = DriverModelForm
    template_name = 'formula1/driver_form_bootstrap.html'


class DriverDeleteView(DeleteView):
    model = Driver
    success_url = reverse_lazy('driver_list')