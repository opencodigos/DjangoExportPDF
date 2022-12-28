# Django Export To PDF
Nesse tutorial vamos exportar os dados de uma tabela para PDF.

***myapp/views.py***

```python
import datetime
from django.http import HttpResponse
import tempfile
from django.template.loader import render_to_string  
import weasyprint

def export_pdf(request): 
    products = Product.objects.all() # lista todos os produtos 
    html_index = render_to_string('export-pdf.html', {'products': products})  
    weasyprint_html = weasyprint.HTML(string=html_index, base_url='http://127.0.0.1:8000/media')
    pdf = weasyprint_html.write_pdf(stylesheets=[weasyprint.CSS(string='body { font-family: serif} img {margin: 10px; width: 50px;}')]) 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Products'+str(datetime.datetime.now())+'.pdf' 
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(pdf)
        output.flush() 
        output.seek(0)
        response.write(output.read()) 
    return response
```

***myapp/urls.py***

```python
from django.urls import path 
from myapp import views

urlpatterns = [
	 ...
   path('export-pdf/', views.export_pdf, name='export-pdf'),  
]
```

***myapp/templates/export-pdf.html***

```html
{% extends 'base.html' %}

{% block content %}
	<h1>Lista de Produtos</h1>  
    
    <table class="table"> 
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nome</th>
                <th scope="col">Preço</th>
                <th scope="col">Descrição</th>
                <th scope="col">Imagens</th>
            </tr>
        </thead> 
        <tbody>
            {% for product in products %}
            <tr>
                <th scope="row">{{ product.id }}</th>
                <th scope="row">{{ product.name|upper }}</th>
                <th scope="row">{{ product.price }}</th>
                <th scope="row">{{ product.description }}</th>

                <th scope="row">
                    {% for el in product.products.all %} 
                    <img src="{{el.image.url}}" alt="{{el.id}}" class="mx-2" width="50">
                    {% endfor %}
                </th>

            </tr>
            {% endfor %}
        </tbody>
    </table>  
{% endblock %}
```

```python
<a class="btn btn-danger" href="{% url 'export-pdf' %}">ExportPDF</a>
```

## Django ExportPDF com Filtro

```python
def export_pdf(request): 
    obj = request.GET.get('obj')
    # products = Product.objects.filter(name__icontains=obj) # lista todos os produtos 
    print(obj) 
    if obj:  
        products = Product.objects.filter(name__icontains=obj)  
    else:
        products = Product.objects.all()   
    
    html_index = render_to_string('export-pdf.html', {'products': products})  
    weasyprint_html = weasyprint.HTML(string=html_index, base_url='http://127.0.0.1:8000/media')
    pdf = weasyprint_html.write_pdf(stylesheets=[weasyprint.CSS(string='body { font-family: serif} img {margin: 10px; width: 50px;}')]) 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Products'+str(datetime.datetime.now())+'.pdf' 
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(pdf)
        output.flush() 
        output.seek(0)
        response.write(output.read()) 
    return response
```

```python
<a class="btn btn-danger" href="{% url 'export-pdf' %}?obj={{request.GET.obj}}">ExportPDF</a>
```