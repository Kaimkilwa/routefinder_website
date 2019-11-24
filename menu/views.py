from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.db.models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def Homebview(request):
	return render(request, 'menu/index.html')
   

# def Ourservice(request):
# 	return render(request, 'navs/service.html')

class Ourservice(ListView):
    # queryset = ServiceModel.objects.filter(Category=1).order_by("-created_on")
    # queryset=Categories.objects.annotate(
    # sub=filter(Subquery(ServiceModel.objects.filter(Category=OuterRef('pk')).only('pk'))).order_by('-created_on')
    # )

    queryset =            Categories.objects.all().order_by('-created_on')
    template_name =       'navs/service.html'
    context_object_name = "my_service"
    paginate_by =         3
   
    
# class ServiceDetail(DetailView):
#     model               =  Categories
#     context_object_name = "my_service"
#     template_name 		= 'navs/service_detail.html' 
def ServiceDetail(request, question_id):
    # try:
    #   question = Questions.objects.get(pk=question_id)
    # except latest_question_list.DoesNotExist:
    #   raise Http404("Question does not exist")
    #   return render(request, 'polls/detail.html', {'question': question})

    categories = get_object_or_404(Categories, pk=question_id)
    return render(request, 'navs/service_detail.html', {'category': categories})



class ServiceCategory(ListView):
	queryset 			=   ServiceModel.objects.filter(status=1).order_by('-created_on')
	context_object_name =  "service_Category"
	template_name 		=  'menu/service.html'


class AboutView(ListView):
    queryset            =   AbooutUsModel.objects.filter(status =1).order_by('-created_on')  
    context_object_name =  'about_us'
    template_name       =   'navs/about.html'

class TeamView(ListView):
    queryset            =  TeamModel.objects.all().order_by('-created_on')
    context_object_name = 'ourteam'
    template_name       = 'navs/team.html'


def ContactView(request):
    form = ContactForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # commit=False
            # post.author = request.user
            
            # post.save()
            
            return redirect('menu:contact')
            success_message = 'Success: Thank for cintact us'
        else:
            form = ContactForm()
    return render(request, 'navs/contact.html', {'form': form})
class visionView(ListView):
    queryset  =            VisiionMission.objects.all()
    context_object_name =  'companyvision'
    template_name =        'navs/vission.html'

class AssociatesView(ListView):
    queryset  = Associates.objects.all().order_by('-created_on')
    context_object_name = 'Ourassociates'
    template_name =       'navs/associates.html'

class ClientsView(ListView):
    queryset  =            ClientModel.objects.all().order_by('-created_on')
    context_object_name = 'clients'
    template_name =        'navs/client.html'
def Client_details(request,client_id):
    client_det = get_object_or_404(ClientModel, pk=client_id)
    return render(request, 'navs/client_detail.html', {'client_det': client_det})


def Apply_service(request,apply_id):
    cate = get_object_or_404(Categories, pk=apply_id)
    try:
        selected_choice = cate.servicemodel_set.get(pk=request.POST['choice'])
    except (KeyError, ServiceModel.DoesNotExist):
# Redisplay the question voting form.
        return render(request, 'navs/service_detail.html', {'cate': cate,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.applied_in += 1
        selected_choice.save()
# Always return an HttpResponseRedirect after successfully dealing
# with POST data. This prevents data from being posted twice if a
# user hits the Back button.
    return HttpResponseRedirect(reverse('menu:service'))
         # args=(question.id,) this args goes in this function  
         # for retreiving information after submitting

