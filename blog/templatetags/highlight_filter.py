import re
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='highlight')
def highlight(text, word):
    #return mark_safe(text.replace(word, "<span class='highlight'>%s</span>" % word))
    pattern = r'(?i)(' + word + ')'
    regex = re.compile(pattern)
    text = regex.sub(r"<span class='highlight'>\1</span>", text)

    return mark_safe(text)