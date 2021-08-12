from django.shortcuts import redirect

def restrict_logged(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request, *args, **kwargs)
    return wrapper_func

def restrict_unlogged(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func

def admin_only(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func