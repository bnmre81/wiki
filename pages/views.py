from django.shortcuts import render
from .models import Page
# Create your views here.
def list_page(request):
	context = {
		'page_list': Page.objects.all(),
	}
	
	return render(request, "list.html", context)


def detail_page(request, page_id):
	context = {
		'page_detail': Page.objects.get(id=page_id),
	}
	
	return render(request, "detail.html", context)