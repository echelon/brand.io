#!/usr/bin/env python
"""
Compile my homepage into a static HTML document.
Copyright 2012 Brandon Thomas.
"""

import json
import datetime
from string import Template

TEMPLATE = 'template.html'
OUTPUT = 'public/index.html'
TIME_FMT = '%H:%M %B %d, %Y'

def load_template(fname):
	f = open(fname, 'r')
	tpl = Template(f.read())
	f.close()
	return tpl

def load_json(fname):
	f = open(fname, 'r')
	data = json.loads(f.read())
	f.close()
	return data

def make_videos(items):
	def make_url(id, num):
		return 'http://img.youtube.com/vi/%s/%d.jpg' % (id, num)

	html = ''
	for it in items:
		html += """<a
			href="http://youtube.com/watch?v=%s"><img
				src="%s" id="%s"></a>""" % (it, make_url(it, 1), it)

	return html

def make_items(items):
	html = ''
	for it in items:
		html += """<div class="item">
		<div class="itemimg">
			<a href="%s"><img src="%s"></a>
		</div>
		<div class="itemdesc">
			<div class="itemtitle">
				<a href="%s">%s</a>
				<span class="itemdate">%s</span>
			</div>
			%s
		</div>
		</div>
		""" % (it['url'], it['img'], it['url'],
				it['title'], it['date'], it['descr'])

	return html

class EST(datetime.tzinfo):
	"""From StackOverflow"""
	def utcoffset(self, dt):
		return datetime.timedelta(hours=-5)

	def dst(self, dt):
		return datetime.timedelta(0)

def save_template(fname, tpl):

	def make_projects():
		data = load_json('projects.json')
		html = make_items(data)
		return html

	def make_presentations():
		data = load_json('presentations.json')
		html = make_items(data)
		return html

	def make_videos2():
		data = load_json('videos.json')
		html = make_videos(data)
		return html

	t = {
		'projects': make_projects(),
		'videos': make_videos2(),
		'presentations': make_presentations(),
		'compileTime': datetime.datetime.now(EST()).strftime(TIME_FMT)
	}
	html = tpl.safe_substitute(t)
	f = open(fname, 'w')
	f.write(html)
	f.close()

def main():
	html = load_template(TEMPLATE)
	save_template(OUTPUT, html)

if __name__ == '__main__':
	main()
