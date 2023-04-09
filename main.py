#simple gui using tkinter by flixzit

#creating a function that changes the text of the label (you can make this function do anything you want)
def changeText():
    label.config(text="the text has changed")


#importing libraries
#tkinter is a python library for creating GUI and we are importing it as tk to make it easier to use
import tkinter as tk

#creating the main window
root = tk.Tk()

#setting the title of the window
#title of the window
root.title("My first GUI")
#setting the size of the window
root.geometry("500x500")

#creating a label
#label is a text that is displayed on the window and we are creating a label and storing it in a variable called label
label = tk.Label(root, text="click the button to change the text", font=("Arial", 20))
#placing the label on the window
label.pack()

#creating a button
root.button = tk.Button(root, text="change text", command=changeText)
#placing the button on the window
root.button.pack()

#making a input box
#input box is a box where you can type text and we are creating an input box and storing it in a variable called inputBox
inputBox = tk.Entry(root, width=50)
#placing the input box on the window
inputBox.pack()

#creating a function that gets the text from the input box
def getText():
    #getting the text from the input box
    text = inputBox.get()
    #removing the text from the input box
    inputBox.delete(0, "end")

    #printing the text
    print(text)

#creating a button to get the text from the input box
root.button = tk.Button(root, text="get text", command=getText)
#placing the button on the window
root.button.pack()


#looping the main window this runs the main window if you have a new or diffrent window you need to loop that window
#just change the name of the window to the name of the window you want to loop
root.mainloop()

#made by flixzit add me on discord at flixzit#0513 for help