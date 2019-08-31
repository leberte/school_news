#!/user/bin/python3
# _*_ coding: utf-8 _*_
from mako.template import Template
def rederHtml(templateFile,postlist):
    t = Template(filename=templateFile)
    page = t.render(postlist = postlist )
    return page