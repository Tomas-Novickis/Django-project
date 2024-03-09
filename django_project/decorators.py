from django.http import HttpResponseForbidden


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.username == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden({
                "You are not authorized to access this page."}, status=401)
    return wrapper
