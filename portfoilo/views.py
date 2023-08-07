from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Profile, Resume, Category, Portfolio
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, JsonResponse
from .forms import ContactForm

def index(request):
    profile = Profile.load()
    resumes = Resume.objects.all()
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()

    context = {
        'profile': profile,
        'resumes': resumes,
        'categories': categories,
        'portfolios': portfolios,
    }
    return render(request, 'index.html', context)

def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"


            try:
                send_mail(
                    subject,
                    message,
                    'YOUR_MAIL_ADRESS', 
                    ['TO_MAIL_ADRESS'],
                    fail_silently=False,
                )
                messages.success(request, 'Email has been sent successfully.')
                return redirect('/index/#contact') 
            except BadHeaderError:
                messages.error(request, 'An error occurred. Invalid header found.')
                return redirect('/index/#contact')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})