from django.test import TestCase
from quiz.models import Category, Question, Answer

class QuizAppModelTest(TestCase):

    def setUp(self):
        # Create a Category instance
        self.category = Category.objects.create(
            category_name="General Knowledge",
            description="Test Category Description",
            is_onboarding=False
        )

        # Create a Question instance linked to the Category
        self.question = Question.objects.create(
            category=self.category,
            question="What is the capital of France?",
            marks=10
        )

        # Create Answer instances linked to the Question
        self.answer1 = Answer.objects.create(
            question=self.question,
            answer="Paris",
            is_correct=True
        )
        self.answer2 = Answer.objects.create(
            question=self.question,
            answer="London",
            is_correct=False
        )

    def test_category_creation(self):
        self.assertEqual(self.category.category_name, "General Knowledge")
        self.assertEqual(self.category.description, "Test Category Description")
        self.assertEqual(self.category.is_onboarding, False)

    def test_question_creation(self):
        self.assertEqual(self.question.category, self.category)
        self.assertEqual(self.question.question, "What is the capital of France?")
        self.assertEqual(self.question.marks, 10)

    def test_answer_creation(self):
        self.assertEqual(self.answer1.question, self.question)
        self.assertEqual(self.answer1.answer, "Paris")
        self.assertEqual(self.answer1.is_correct, True)
        self.assertEqual(self.answer2.answer, "London")
        self.assertEqual(self.answer2.is_correct, False)

    def test_get_answers_method(self):
        answers = self.question.get_answers()
        self.assertIsInstance(answers, list)
        self.assertEqual(len(answers), 2)
        self.assertIn({'answer': 'Paris', 'is_correct': True}, answers)
        self.assertIn({'answer': 'London', 'is_correct': False}, answers)
