import requests
import json
import time
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
##import plotly.offline as offline
##from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from datetime import datetime


plotly.tools.set_credentials_file(username='Shin4y', api_key='sR7volNuu8cIT6HIEGtQ')
##offline.init_notebook_mode()
##init_notebook_mode(connected=True)


date = (time.strftime("%d/%m/%Y"))
base = 'GBP'
compare2 = 'AUD'
compare1 = 'RUB'
prev = [None]*7
dat = [None]*7
x_val = [None]*7
y_val = [None]*7
y_val2 = [None]*7
url = 'http://api.fixer.io/latest?base='+base+'&symbols='+compare
url2 = 'http://api.fixer.io/'
info = json.loads(requests.get(url).text)
##print (json.dumps(info, indent=2, sort_keys = True))
##print (date)

day = date[0] + date[1]
month = date[3]+date[4]
year = date[6]+date[7]+date[8]+date[9]
##print (day + "-" + month + "-" + year)

def date_generate(which):

	for i in range(0,7):
		date_holder = day
		month_holder = month
		m = int(month_holder)
		d = int(date_holder)
		if d - i <= 0:
			change = abs(i-d)
			if m == 4 or month == 6 or month == 9:
				d = 31 - change
			if m == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
				d = 32 - change
			if m == 2:
				d = 29 - change
			if m == month_holder:
				m = m - 1
		else:
			d = d - i
		if d < 10:
			date_holder = '0'+ str(d)
		else:
			date_holder = str(d)
		
		if m < 10:
			month_holder = '0' + str(m)
		else:
			month_holder = str(m)

	x_val[i] = datetime(year = int(year), month = m, day = d)
	prev[i] = year + '-' + month_holder + "-" + date_holder
	if which == 1:
		return x_val
	else:
		return y_val


def get_data(compare):
	for x in range(0,7):
		url_place = url2
		url_place = url_place + prev[x] + '?base=' + base + '&symbols=' + compare
		print (url_place)
		dat[x] = json.loads(requests.get(url_place).text)
		y_val[x] = dat[x]['rates']['USD']
		print (json.dumps(dat[x], indent=2, sort_keys = True))
	return y_val



for i in range(0,7):
	date_holder = day
	month_holder = month
	m = int(month_holder)
	d = int(date_holder)
	if d - i <= 0:
		change = abs(i-d)
		if m == 4 or month == 6 or month == 9:
			d = 31 - change
		if m == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			d = 32 - change
		if m == 2:
			d = 29 - change
		if m == month_holder:
			m = m - 1
	else:
		d = d - i
	if d < 10:
		date_holder = '0'+ str(d)
	else:
		date_holder = str(d)

	if m < 10:
		month_holder = '0' + str(m)
	else:
		month_holder = str(m)
	
	x_val[i] = datetime(year = int(year), month = m, day = d)
	prev[i] = year + '-' + month_holder + "-" + date_holder
##print (prev)

for x in range(0,7):
	url_place = url2
	url_place = url_place + prev[x] + '?base=' + base + '&symbols=' + compare
	print (url_place)
	dat[x] = json.loads(requests.get(url_place).text)
	y_val[x] = dat[x]['rates'][compare]
	print (json.dumps(dat[x], indent=2, sort_keys = True))

for x in range(0,7):
	url_place = url2
	url_place = url_place + prev[x] + '?base=' + base + '&symbols=' + compare2
	print (url_place)
	dat[x] = json.loads(requests.get(url_place).text)
	y_val2[x] = dat[x]['rates'][compare2]
	print (json.dumps(dat[x], indent=2, sort_keys = True))

##date_generate()

##get_data()
##x_val = date_generate(1)
##y_val = get_data()
print (x_val, y_val)
scatter0 = go.Scatter(x = x_val, y= y_val, name = compare, mode = "lines+markers")
scatter1 = go.Scatter(x = x_val, y= y_val2, name = compare2, mode = "lines+markers")
data = Data([scatter0, scatter1])

py.plot(data, filename = 'basic-line')






