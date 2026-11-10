from django.http import JsonResponse
from django.shortcuts import render


VERIFICATION_FLAG = False
VERIFICATION_TEXT = "Version Buena"


def verification(request):
	return render(
		request,
		"core/verification.html",
		{
			"verification_flag": VERIFICATION_FLAG,
			"verification_text": VERIFICATION_TEXT,
		},
	)


def health(request):
	"""Endpoint de salud: confirma que la aplicación web está viva."""
	return JsonResponse({"status": "ok"})
