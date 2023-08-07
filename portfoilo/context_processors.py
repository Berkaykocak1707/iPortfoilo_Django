from .models import Profile

def profile(request):
    profile = Profile.load()
    return {'profile': profile}
