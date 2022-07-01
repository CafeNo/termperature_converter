#Thanakorn Posiri 6310742306

from tkinter import * # just import the tkinter libraly module

if __name__ == '__main__': # This is the main function of the program to set up the Window
    root = Tk() # set root
    root.title('Converter celcius and fahrenheit') # title of the window
    root.geometry('490x170') # geometry of the window
    root.resizable(False, False) # resizable is stable
    root['background'] = '#24292e' # background color


'''
        Fahrenheit Class of UI and Calculated

'''


def UI_fahrenheit(): # This function is for the fahrenheit class
    txt = farTxt.get() # get the value of the textbox
    farInput = float(txt) # input value of the textbox

    celBox.delete(0, END) # delete the value of the textbox
    celBox.insert(0, '%.1f' % (celCal(farInput))) # insert the value of the textbox


def fahCal(celcius): # This function is for the calculate celcius class
    celcius = celcius * 9 / 5 + 32 # calculation formula of celcius
    return celcius # return the value

fahLabel = Label(root, text = 'Fahrenheit', font = ('Aerial', 12, 'bold'), bg = '#24292e', fg = '#ffab70') # set bg color and text for the label
fahLabel.grid(row = 0, column = 0, padx = 10, pady = 10) # set grid for title bar
farTxt = StringVar() # set stringvar for textbox
farTxt.set('') # set textbox for celcius
farBox = Entry(root, textvariable = farTxt, font = ('Calibri', 16, 'bold'), bg = '#FFFFFF', fg = '#000000') # set bg color and text for textbox
farBox.grid(row = 0, column = 1, padx = 20, pady = 3) # set grid for textbox
farButton = Button(root, text = 'Convert', command = UI_fahrenheit, font = ('Calibri', 10, 'bold'), bg = '#ffab70', fg = '#000000') # set farhrenheit button
farButton.grid(row = 0, column = 2, padx = 3, pady = 3, ipadx = 10, ipady = 5) # set grid for button
farlabel2 = Label(root, text='Fahrenheit   =   celcius * 9 / 5 + 32', font = ('Aerial', 9), bg = '#24292e', fg = '#ffab70') # set bg color and text for the calculation formula of fahrenheit label
farlabel2.grid(row = 4, column = 1) # set grid for textbox


'''
        Celcius Class of UI and Calculated

'''


def UI_celcius(): # This function is for the celcius class
    txt = celTxt.get() # get the value of the textbox
    celInput = float(txt) # input value of the textbox

    farBox.delete(0, END) # delete the value of the textbox
    farBox.insert(0, '%.1f' % (fahCal(celInput))) # insert the value of the textbox

def celCal(fahrenheit): # This function is for the calculate fahrenheit class
    fahrenheit = (fahrenheit - 32) * 5 / 9 # calculation formula of fahrenheit
    return fahrenheit # return the value

celLabel = Label(root, text = 'Celcius', font = ('Aerial', 12, 'bold'), bg = '#24292e', fg = '#9ecbff') # set bg color and text for the label
celLabel.grid(row = 1, column = 0, padx = 10, pady = 10) # set grid for title bar
celTxt = StringVar() # set stringvar for textbox
celTxt.set('') # set textbox for celcius
celBox = Entry(root, textvariable = celTxt, font = ('Calibri', 16, 'bold'), bg = '#FFFFFF', fg = '#000000') # set bg color and text for textbox
celBox.grid(row = 1, column = 1, padx = 20, pady = 3) # set grid for textbox
celButton = Button(root, text = 'Convert', command = UI_celcius, font = ('Calibri', 10, 'bold'), bg = '#9ecbff', fg = '#000000') # set celcius button
celButton.grid(row = 1, column = 2, padx = 3, pady = 3, ipadx = 10, ipady = 5) # set grid for button
cellabel2 = Label(root, text='Celcuis   =   (fahrenheit - 32) * 5 / 9', font = ('Aerial', 9), bg = '#24292e', fg = '#9ecbff') # set bg color and text for the calculation formula of celcius label
cellabel2.grid(row = 5, column = 1) # set grid for textbox

root.mainloop()