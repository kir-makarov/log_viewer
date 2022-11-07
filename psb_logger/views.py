from django.shortcuts import render
from .models import MainTable


def catalog(request):
    build_list = MainTable.objects.values('build').distinct()
    context = {"result_build": build_list}
    if request.method == 'POST':
        selected_base = request.POST.get('database', None)
        selected_build = request.POST.get('selectbuild', None)

        if selected_base and selected_build:
            result = MainTable.objects.filter(database=selected_base, build=selected_build)[:1000]
            context["result"] = result
            context["selected_build"] = selected_build
            return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html', context)


def index(request):
    return render(request, 'main/index.html')
