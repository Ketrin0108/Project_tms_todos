from django.forms.models import model_to_dict
from django.http import JsonResponse

from todos.forms import ToDoForm, ToDoUpdateForm, ToDoFilterForm
from todos.models import ToDo


def todos(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            data = form.save()
            return JsonResponse(model_to_dict(data))
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})
    return JsonResponse({'todos': [model_to_dict(p) for p in ToDo.objects.all()]})


def todo(request, todo_id: int):
    try:
        todo_obj = ToDo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'ToDo not found.'})

    if request.method == 'POST':
        form = ToDoUpdateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            data = form.save()
            return JsonResponse(model_to_dict(data))
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})

    elif request.method == 'DELETE':
        todo_obj.delete()
        return JsonResponse({'status': 204, 'message': 'ToDo successfully deleted'})

    return JsonResponse({'todos': model_to_dict(todo_obj)})