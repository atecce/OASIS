from django.http import HttpResponse

def index(request):

	return HttpResponse('And perhaps, the horizons are limited\n \
				for those who think the center of the universe,\n \
				is man.')
