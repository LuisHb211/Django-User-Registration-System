from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
# from django.http import Http404

def index(request):
  contacts = Contact.objects.filter(show=True).order_by('-id')
  
  paginator = Paginator(contacts, 20)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  
  context = {
    'page_obj': page_obj,
    'site_title': 'Contatos - '
  }
  
  return render(
    request,
    'contact/index.html',
    context,
  )
  
def search(request):
  search_value= request.GET.get('q', '').strip()
  
  if search_value == '':
    return redirect('contact:index')
  
  # Faz com que a querry busque tanto no first name, quanto no last..., pelo texto passado na busca 
  contacts = Contact.objects\
  .filter(show=True)\
  .filter(
    Q(first_name__icontains=search_value) |
    Q(last_name__icontains=search_value) |
    Q(phone__icontains=search_value)  |
    Q(email__icontains=search_value)
    )\
  .order_by('-id')
  
  paginator = Paginator(contacts, 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  
  
  context = {
    'page_obj': page_obj,
    'site_title': 'Search - ',
    'search_value': search_value,
  }
  
  return render(
    request,
    'contact/index.html',
    context,
  )
  
def contact(request, contact_id):
  # single_contact = Contact.objects.filter(pk=contact_id).first()
  # if single_contact is None:
  #   raise Http404()
  
  single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
  site_title = f'{single_contact.first_name} {single_contact.last_name} - '
  context = {
    'contact':single_contact,
    'site_title':site_title,
  }  

  return render(request, 'contact/contact.html', context)