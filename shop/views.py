from django.shortcuts import render, get_object_or_404
from .models import Cake, RuleSettings, Filling
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def catalog(request):
    # Отримуємо всі торти з бази даних
    cakes = Cake.objects.all()
    # Передаємо їх у HTML-шаблон
    return render(request, 'shop/catalog.html', {'cakes': cakes})

def cake_detail(request, cake_id):
    # Шукаємо торт за ID. Якщо не знайдено — видасть сторінку 404
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, 'shop/cake_detail.html', {'cake': cake})

@csrf_exempt
def calculate_price(request):
    """
    Ендпоинт для расчета цены торта.
    Принимает POST-запрос с параметрами (вага, начинка тощо) в форматі JSON.
    """
    if request.method == 'POST':
        # Тут в майбутньому будемо читати дані: data = json.loads(request.body)

        # Поки що віддаємо фіктивну (заглушену) ціну
        response_data = {
            'status': 'success',
            'calculated_price': 1500.00,
            'message': 'Ціна успішно розрахована'
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Тільки POST запити'}, status=405)


@csrf_exempt
def update_calculator_settings(request):
    """
    Ендпоинт для зміни коефіцієнтів калькулятора (для адмінки).
    """
    if request.method == 'POST':
        # Тут в майбутньому будемо зберігати нові налаштування
        return JsonResponse({'status': 'success', 'message': 'Налаштування оновлено'})

    return JsonResponse({'error': 'Тільки POST запити'}, status=405)

def rules_view(request):
    # Отримуємо налаштування (якщо їх ще немає в базі, створюємо з дефолтними значеннями)
    rules, created = RuleSettings.objects.get_or_create(id=1)
    return render(request, 'shop/rules.html', {'rules': rules})

def fillings_and_prices_view(request):
    rules, created = RuleSettings.objects.get_or_create(id=1)
    fillings = Filling.objects.all()
    return render(request, 'shop/fillings.html', {'rules': rules, 'fillings': fillings})