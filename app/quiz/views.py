from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse  # Ensure HttpResponse is imported
from .models import Category, Question
import random

def home(request):
    # Redirect only if the category parameter is present and the quiz view handles it correctly
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    # Otherwise, render the category selection page
    context = {'categories': Category.objects.all()}
    return render(request, 'qcategory.html', context)


#def home(request):
 #   context = {'categories': Category.objects.all()}
  #  return render(request, 'qcategory.html', context)


def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs = list(question_objs)
        random.shuffle(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer": question_obj.get_answers(),
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)  # Consider using logging instead of print for production code
        return HttpResponse("Something went wrong")
