from django.urls import reverse
from django.http import HttpResponseRedirect

class AccessMiddleware:

	def __init__(self, get_response):
		self._get_response = get_response

	def __call__(self, request):
		if request.user.is_authenticated or request.path == reverse('login'):
			response = self._get_response(request)
			return response
		return HttpResponseRedirect(reverse('login'))