from django.shortcuts import render, redirect
from .forms import IpForm
from .models import Ip
from django.contrib import messages
import ipaddress


def home(request):

    form = IpForm
    data = {
        'form': form
    }

    if request.method == 'POST':
        fio = request.POST.get('fio')
        cabinet = request.POST.get('cabinet')
        department = request.POST.get('department')
        user_name = request.POST.get('user_name')
        pc_name = request.POST.get('pc_name')
        ip = request.POST.get('ip')
        if not fio:
            messages.success(request, "Не введено ФИО")
            return redirect('home')
        if not cabinet:
            messages.success(request, "Не введен кабинет")
            return redirect('home')
        if not department:
            messages.success(request, "Не введен отдел")
            return redirect('home')
        if not user_name:
            messages.success(request, "Не введено имя пользователя пк")
            return redirect('home')
        if not pc_name:
            messages.success(request, "Не введено имя пк")
            return redirect('home')
        if not ip:
            messages.success(request, "Не введено IP")
            return redirect('home')

        try:
            ipaddress.ip_address(ip)  # Проверка на валидность IP-адреса
        except ValueError:
            messages.success(request, "Некорректный IP-адрес")
            return redirect('home')

        try:
            cabinet = int(cabinet)
        except ValueError:
            messages.error(request, "Не корректно введен кабинет")
            return redirect('home')

        try:
            department = int(department)
        except ValueError:
            messages.error(request, "Не корректно введен  отдел")
            return redirect('home')

        request.session['fio'] = fio
        request.session['cabinet'] = cabinet
        request.session['department'] = department
        request.session['user_name'] = user_name
        request.session['pc_name'] = pc_name
        request.session['ip'] = ip

        return redirect('ip_submit')

    return render(request, 'main/home.html', data)


def ip_submit(request):

    fio = request.session.get('fio')
    cabinet = request.session.get('cabinet')
    department = request.session.get('department')
    user_name = request.session.get('user_name')
    pc_name = request.session.get('pc_name')
    ip = request.session.get('ip')

    Ip.objects.get_or_create(
        fio=fio,
        cabinet=cabinet,
        department=department,
        user_name=user_name,
        pc_name=pc_name,
        ip=ip
    )

    messages.success(request, "Запись сохранена!")
    return redirect('home')
