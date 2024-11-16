from django import template
register = template.Library()

@register.filter
def change_null_value(var):
    if var =="None":
        return "-"
    else:
        return var