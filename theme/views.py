from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models  import Blog, Category

def contactform(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! We will get back to you soon.")
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contactform.html', {'form': form})

def home(request):
    blogs = Blog.objects.order_by('-published_date')[:3]  # Get the 3 latest blogs
    return render(request, 'home.html', {'blogs': blogs})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-published_date') 
    categories = Category.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, 'categories':categories})

def blog_detail(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    blogs = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog_detail.html', {'blog': blog, 'blogs': blogs})

def services(request):
    return render(request, 'services.html')

def search(request):
    categories = Category.objects.all()
    query = request.GET.get('q', '').strip()  # Handle empty or invalid query
    blogs = []
    
    if query:
        blogs = Blog.objects.filter(title__icontains=query) 

    context = {
        'query': query,
        'blogs': blogs,
        'categories' : categories,
    }
    return render(request, 'search.html', context)


