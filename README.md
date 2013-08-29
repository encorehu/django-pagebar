django-pagebar
==============

display a pretty pagebar by using templatetag, and supply  an optional customize Paginator based on official paginator.

Origin
======

django official display all pages by paginator and page_obj, like this:

[1] [2] [3] [4] [5] [6] [7] ... [198] [199] [200] # total 200 pages for example.

use this code:

    {% for page_number in paginator.page_range %}
        <a href='?page={{page_number}}>{{page_number}}</a>
    {% endfor %}
    
ugly display all the pages of 200, even if you have 2000 pages, it will display 2000 links on one page.

so, the problem is the paginator.page_range, if we can modify the paginator.page_range, the problem will fix.

so, my solution is modify the page_range, to display a part of origin page_range, just called slicing and some if 
else control.

for example, 200 pages, cur_page is var, it will display as follows:

*[] and {} is for styling. {} is cur_page, [] is pages.*

cur_page = 1

    {1} [2] [3] [4] [...200] [Next]

cur_page = 2

    [Previous] [1] {2} [3] [4] [5] [...200] [Next]

cur_page = 3

    [Previous] [1] [2] {3} [4] [5] [6] [...200] [Next]

cur_page = 4

    [Previous] [1] [2] [3] {4} [5] [6] [7] [...200] [Next]

cur_page = 5

    [Previous] [1...] [2] [3] [4] {5} [6] [7] [8] [...200] [Next]

cur_page = 6

    [Previous] [1...] [3] [4] [5] {6} [7] [8] [9] [...200] [Next]

cur_page = x > 4, x < 200-4

    [Previous] [1...] [x-3] [x-2] [x-1] {x} [x+1] [x+2] [x+3] [...200] [Next]

cur_page = 196

    [Previous] [1...] [193] [194] [195] {196} [197] [198] [199] [...200] [Next]

cur_page = 197

    [Previous] [1...] [194] [195] [196] {197} [198] [199] [200] [Next]

cur_page = 198

    [Previous] [1...] [195] [196] [197] {198} [199] [200][Next]

cur_page = 199

    [Previous] [1...] [196] [197] [198] {199} [200] [Next]

cur_page = 200

    [Previous] [1...] [197] [198] [199] [200]

that is much more pretty than the origin pagebar display.
