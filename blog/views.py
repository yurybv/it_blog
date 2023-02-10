from django.shortcuts import render


posts = [
    {
        'author': 'Yury',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'January 1, 2023'
    },
    {
        'author': 'Almaz',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'January 2, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
