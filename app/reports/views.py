from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def delete_view(request, *args, **kwargs):
    r_id = kwargs.get("pk")
    obj = Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER')) #redirect to current path/view

@login_required
def report_view(request, production_line):
    form = ReportForm(request.POST or None, production_line=production_line)
    pform = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name = production_line)
    #print(queryset)
    line = get_object_or_404(ProductionLine, name = production_line)
    
    

        
       
    if 'submitbtn1'in request.POST:
        
        r_id = request.POST.get("report_id")
        print(r_id)
    
    
        if pform.is_valid():
            report = Report.objects.get(id=r_id)
            print("data here")
            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()
            #form = ReportForm()
            #pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER'))
            
    elif 'submitbtn2'in request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()
            #form = ReportForm()
            #pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER'))
       
    
       
    context = {
        'form': form,
        'pform': pform,
        'object_list': queryset,
    }
    
    return render(request, 'reports/report.html', context)
    