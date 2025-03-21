from django.shortcuts import render, redirect
from .forms import Teacher, StudentQueryForm
from .models import Feedback



# Home page view
def home(request):
    teacher_form = Teacher()
    student_form = StudentQueryForm()

    if request.method == "POST":
        if 'teacher_submit' in request.POST:  # Teacher Registration Form
            teacher_form = Teacher(request.POST)
            if teacher_form.is_valid():
                teacher_form.save()
                return redirect('teacher_success')

        elif 'student_submit' in request.POST:  # Student Query Form
            student_form = StudentQueryForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('submit_success')

    return render(request, "homepage.html", {
        "teacher_form": teacher_form,
        "student_form": student_form
    })


# Teacher Registration Success page
def teacher_success(request):
    return render(request, "teacher_success.html")


# Student Query Success page
def submit_success(request):
    return render(request, "submit_success.html")


# views.py


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")



def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        
        if name and email and comment:
            Feedback.objects.create(name=name, email=email, comment=comment)

    feedbacks = Feedback.objects.all()  # Fetch all feedback entries
    return render(request, "feedback.html", {"feedbacks": feedbacks})
