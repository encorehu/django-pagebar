from django.template import Library, Node, TemplateSyntaxError, Variable

register = Library()

class DisplayPageRangeNode(Node):
    def __init__(self, paginator, page_number, context_var):
        self.paginator = Variable(paginator)
        self.page_number = Variable(page_number)
        self.context_var = context_var

    def render(self, context):
        paginator   = self.paginator.resolve(context)
        page_number = self.page_number.resolve(context) #-1
        #print paginator.page_range
        #print page_number,paginator.num_pages

        #slicing
        start, stop = 0, paginator.num_pages
        if paginator.num_pages >4:
            start  = max(page_number-4, 0)
            stop   = min(page_number+3, paginator.num_pages)

        #print start,stop
        context[self.context_var] = paginator.page_range[start:stop]
        return ''

def get_display_page_range(parser, token):
    """
    {% get_display_page_range [pagenator] [page_number ] as [context_var] %}
    """
    bits = token.contents.split()
    if len(bits) not in (3, 5):
        raise TemplateSyntaxError('%s tag requires 3 or 5 arguments' % bits[0])
    if bits[3] != 'as':
        raise TemplateSyntaxError("Third argument to %s tag must be 'as'" % bits[0])
    if not bits[2]:
        raise TemplateSyntaxError("Second argument to %s tag must be the page_number varian" % bits[0])
    if not bits[3]:
        bits[4] = 'display_page_range'

    return DisplayPageRangeNode(bits[1], bits[2], bits[4])

register.tag('get_display_page_range', get_display_page_range)
