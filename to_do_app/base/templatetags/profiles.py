from django import template

from to_do_app.base.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0
