from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Peripheral, Category, STATUS, Department
from .forms import BorrowerForm
from django.contrib import messages
from .models import Borrow


class CombinedListView(generic.ListView):
    model = Category
    # queryset = Category.objects.order_by("-date_created")
    template_name = "index.html"
    # context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        context['category_list'] = Category.objects.all()
        context['peripheral_list'] = Peripheral.objects.all()
        return context


def borrow_form(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            borrower_name = form.cleaned_data['borrower_name']
            department = form.cleaned_data['department']
            category = form.cleaned_data['category']
            peripheral = form.cleaned_data['peripheral']
            unique_number = form.cleaned_data['unique_number']

            Borrow.objects.create(borrower_name=borrower_name, department=department,
                                  category=category, peripheral=peripheral, unique_number=unique_number)

            messages.success(request, 'Form submitted successfully!')
    # Include the same context data logic here to pass context data to the template
    department_list = Department.objects.all()
    category_list = Category.objects.all()
    peripheral_list = Peripheral.objects.all()

    return render(request, "borrower-form.html", {'department_list': department_list,
                                          'category_list': category_list,
                                          'peripheral_list': peripheral_list})