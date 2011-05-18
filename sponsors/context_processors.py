from django.core.cache import cache
from sponsors.models import Sponsor

sponsors_large = [
    Sponsor.LEVEL.kryptonite,
    Sponsor.LEVEL.diamond,
]

sponsors_small = [
    Sponsor.LEVEL.platinum,
    Sponsor.LEVEL.gold,
    Sponsor.LEVEL.producer
]

def get_sponsors(key, levels):
    sponsors = cache.get(key)
    if not sponsors:
        sponsors = Sponsor.objects.filter(level__in=levels).order_by('level')
        cache.set(key, list(sponsors), 600)
    return sponsors

def sponsors_by_levels(request):
    ctx = {}
    ctx['sponsors_large'] = get_sponsors('sponsors_large', sponsors_large)
    ctx['sponsors_small'] = get_sponsors('sponsors_small', sponsors_small)    
    # ctx['sponsors_kryptonite'] = Sponsor.objects.filter(level=Sponsor.LEVEL.kryptonite)
    # ctx['sponsors_diamond'] = Sponsor.objects.filter(level=Sponsor.LEVEL.diamond)
    # ctx['sponsors_platinum'] = Sponsor.objects.filter(level=Sponsor.LEVEL.platinum)
    # ctx['sponsors_gold'] = Sponsor.objects.filter(level=Sponsor.LEVEL.gold)
    # ctx['sponsors_producer'] = Sponsor.objects.filter(level=Sponsor.LEVEL.producer)
    return ctx