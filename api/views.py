import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Categoria


@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):
  
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data={}
            data['id']= qs.id 
            data['tipo'] = qs.tipo 
            return JsonResponse(data)
        else:
            data  = list (Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type='application/json')


