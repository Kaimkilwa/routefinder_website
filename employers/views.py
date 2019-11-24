from django.shortcuts import render

# Create your views here.
def EmployerView(request):
	return render(request, 'employers/employer.html')
