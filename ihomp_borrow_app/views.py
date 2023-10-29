from django.shortcuts import render
from django.views import generic
from .models import Peripheral, Category, STATUS, Department
from .forms import BorrowerForm
from django.contrib import messages
from .models import Borrow
from django.http import JsonResponse


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


from django.http import JsonResponse
from django.shortcuts import render

def borrow_form(request):
    department_list = Department.objects.all()
    category_list = Category.objects.all()
    peripheral_list = []

    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            borrower_name = form.cleaned_data['borrower_name']
            department = form.cleaned_data['department']
            category = form.cleaned_data['category']
            peripheral = form.cleaned_data['peripheral']
            unique_number = form.cleaned_data['unique_number']

            Borrow.objects.create(
                borrower_name=borrower_name,
                department=department,
                category=category,
                peripheral=peripheral,
                unique_number=unique_number
            )

            messages.success(request, 'Form submitted successfully!')

        # You should include the code to update peripheral_list based on the selected category here.
        if category:
            peripheral_list = Peripheral.objects.filter(category=category)

    return render(request, "borrower-form.html", {
        'department_list': department_list,
        'category_list': category_list,
        'peripheral_list': peripheral_list,
    })


def get_peripherals(request, category_id):
    # Retrieve peripherals for the selected category
    try:
        category = Category.objects.get(category_id=category_id)
        peripherals = Peripheral.objects.filter(category=category)
        peripherals_data = [{'peripheral_id': p.peripheral_id, 'peripheral_description': p.peripheral_description} for p in peripherals]
        return JsonResponse({'peripherals': peripherals_data})
    except Category.DoesNotExist:
        return JsonResponse({'peripherals': []})


def get_unique_numbers(request, peripheral_id):
    try:
        peripheral = Peripheral.objects.get(peripheral_id=peripheral_id)
        if peripheral:
            unique_numbers = peripheral.unique_number.split(',') if peripheral.unique_number else []
        else:
            unique_numbers = []

        return JsonResponse({'unique_numbers': unique_numbers})
    except Peripheral.DoesNotExist:
        return JsonResponse({'unique_numbers': []})


