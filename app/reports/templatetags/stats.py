from django import template

register = template.Library()

@register.filter
def stats(value, value2):
    try:
        if (value-value2<=0):
            return "Doing OK"
        else:
            return "Need guidance"
    except:
        pass
