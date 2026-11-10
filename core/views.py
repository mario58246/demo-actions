from django.http import JsonResponse


def health(request):
	"""Endpoint de salud: confirma que la aplicación web está viva."""
	return JsonResponse({"status": "ok"})
