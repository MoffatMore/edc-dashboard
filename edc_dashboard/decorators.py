from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def allowed_users(allowed_roles=None):
	if allowed_roles is None:
		allowed_roles = []

	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles or request.user.is_superuser:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page.', status=403)

		return wrapper_func

	return decorator
