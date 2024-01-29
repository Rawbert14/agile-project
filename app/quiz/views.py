from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Category, Question, QuizScore
import random, json
from django.db.models import Count, Avg, Max, Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required
def home(request):
    categories = Category.objects.all()
    quizzes_with_attempts = Category.objects.annotate(
        num_attempts=Count('quizscore', filter=Q(quizscore__user=request.user)),
        score=Max('quizscore__score', filter=Q(quizscore__user=request.user)),
        last_attempt_date=Max('quizscore__date_taken', filter=Q(quizscore__user=request.user))
    )
    context = {
        'categories': categories,
        'quizzes_with_attempts': quizzes_with_attempts
    }
    return render(request, 'qcategory.html', context)

@login_required
def quiz(request):
    category_name = request.GET.get('category')
    category = Category.objects.filter(category_name=category_name).first()
    quiz_title = category.category_name if category else "Quiz"
    context = {'category': category_name, 'quiz_title': quiz_title}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.filter(
            category__category_name__icontains=request.GET.get('category', '')
        ) if request.GET.get('category') else Question.objects.all()
        random.shuffle(list(question_objs))
        data = [{
            "uid": q.uid, "category": q.category.category_name,
            "question": q.question, "marks": q.marks,
            "answers": q.get_answers(),
            "correct_answer": next(a['answer'] for a in q.get_answers() if a['is_correct'])
        } for q in question_objs]
        return JsonResponse({'status': True, 'data': data})
    except Exception as e:
        return HttpResponse("Something went wrong", status=500)

@csrf_exempt  
@require_POST
@login_required
def submit_score(request):
    try:
        data = json.loads(request.body)
        print("Received data:", data)  

        quiz_id = data.get('quiz_id')
        score = float(data.get('score'))
        
        quiz_name = data.get('quiz_id')
        quiz = Category.objects.get(category_name=quiz_name)

        if quiz_id is None or score is None:
            return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)

       
        QuizScore.objects.create(
            user=request.user,
            quiz=quiz,
            score=score
        )

        return JsonResponse({'status': 'success', 'message': 'Score saved successfully'})

    except Category.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Quiz not found'}, status=404)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

    except Exception as e:
        print(f"Error: {str(e)}")  
        return JsonResponse({'status': 'error', 'message': 'An error occurred'}, status=500)

