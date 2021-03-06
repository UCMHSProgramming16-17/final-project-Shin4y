# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import requests
    import json
    import time
    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go
    from plotly.graph_objs import *
    import plotly.graph_objs as go
    from plotly.graph_objs import *
##import plotly.offline as offline
##from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    from datetime import datetime

define e = Character("Eileen")

define t = Character("Tender")

image main_face = "menu_face"
image bg sin_curr_bg = "sin_curr_bg.jpg"
image bg menu_start = "city_bg.jpg"
$ curr1 = 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg menu_start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show main_face

    # These display lines of dialogue.

    "Hello, friend."

    e "What do you want to do?."

    menu:
        "Let's check a single currency price.":
            jump sin_curr

        "Let's compare currencies!":
            jump dub_curr

        "Think I'm done for now.":
            return

label sin_curr:
    
    scene bg sin_curr_bg
    with fade

    python:
        plotly.tools.set_credentials_file(username='Shin4y', api_key='sR7volNuu8cIT6HIEGtQ')

        date = (time.strftime("%d/%m/%Y"))
        base = 'GBP'

        compare2 = input("which currency? Please type 3 letter symbol for currency in all caps. EX: USD, AUD, RUB.")
        compare1 = input("other currency? Please type 3 letter symbol for currency in all caps. EX: USD, AUD, RUB.")

        # place holders
        dat = [None]*7
        x_val = [None]*7
        y_val2 = [None]*7
        y_val1 = [None] *7
        url2 = 'http://api.fixer.io/'
        prev2 = [None] * 7 #placeholder

        # getting correct date strings
        day = date[0] + date[1]
        month = date[3]+date[4]
        year = date[6]+date[7]+date[8]+date[9]

        def date_generate(which):
            for i in range(0,7):
                date_holder = day
                month_holder = month
                m = int(month_holder)
                d = int(date_holder)
                if d - i <= 0: # if the previous week is part of a past month
                    change = abs(i-d) #changing day
                    if m == 4 or month == 6 or month == 9:
                        d = 31 - change
                    if m == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        d = 32 - change
                    if m == 2:
                        d = 29 - change
                if m == month_holder: #changing month
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

                x_val[i] = datetime(year = int(year), month = m, day = d) #dates on the actual graph
                prev2[i] = year + '-' + month_holder + "-" + date_holder #dates used to request values from api
            prev3 = prev2
            if which == 1: #using one function to return different values when needed based on which parameter
                return x_val
            
            else:
                return prev3



        def get_data(compare): #get data from api
            y_val = [None] * 7
            prev = date_generate(2)
            print (prev)
            for x in range(0,7):
                url_place = url2
                url_place = url_place + prev[x] + '?base=' + base + '&symbols=' + compare
                #print (url_place)
                dat[x] = json.loads(requests.get(url_place).text)
                y_val[x] = dat[x]['rates'][compare]
                #print (json.dumps(dat[x], indent=2, sort_keys = True))

            return y_val



        y_val1 = get_data(compare1) #get line 1 y value
        y_val2 = get_data(compare2) #get line 2 y value
        x_val = date_generate(1) #same x value for both charts

        scatter0 = go.Scatter(x = x_val, y= y_val1, name = compare1, mode = "lines+markers") #data for the lines
        scatter1 = go.Scatter(x = x_val, y= y_val2, name = compare2, mode = "lines+markers") #data for the lines
        data = Data([scatter0, scatter1])

        py.plot(data, filename = 'basic-line') #plotting









    show main_face
    t "which country?"

    return




   

    # This ends the game.
return
    

