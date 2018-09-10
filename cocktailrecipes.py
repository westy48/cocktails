from guizero import App, Text, PushButton, Box, Picture, yesno
import os

def show_menu():
    delicious.hide()
    menu.show()

def switchoff():
    confirm = yesno("Shutdown", "Do you really want to shutdown?")
    if confirm == True:
# CAUTION: This line shuts your computer down.
        os.system('sudo shutdown -h now')
# If you want to replace the shutdown button with "Quit app" use the following line instead of line 12
#       app.destroy()
    else:
        delicious.show

# Each of these functions hides 'menu', passes an image file to
# the 'recipe' PushButton and shows the 'delicious' box
def coffee():
    menu.hide()
    recipe.image = "espmar.jpg"
    delicious.show()

def drymartini():
    menu.hide()
    recipe.image = "martini.jpg"
    delicious.show()

def elysee():
    menu.hide()
    recipe.image = "champs.jpg"
    delicious.show()

def french75():
    menu.hide()
    recipe.image = "frenchie.jpg"
    delicious.show()

def inamorata():
    menu.hide()
    recipe.image = "inamorata.jpg"
    delicious.show()

def jack():
    menu.hide()
    recipe.image = "bubbly.jpg"
    delicious.show()

def jamesbond():
    menu.hide()
    recipe.image = "vesper.jpg"
    delicious.show()

def last_word():
    menu.hide()
    recipe.image = "lastword.jpg"
    delicious.show()

def margarita():
    menu.hide()
    recipe.image = "marg.jpg"
    delicious.show()

def negroninegroni():
    menu.hide()
    recipe.image = "negroni.jpg"
    delicious.show()

def queen():
    menu.hide()
    recipe.image = "qm.jpg"
    delicious.show()

def revive():
    menu.hide()
    recipe.image = "corpse.jpg"
    delicious.show()

def tc():
    menu.hide()
    recipe.image = "tomcollins.jpg"
    delicious.show()

def valencia():
    menu.hide()
    recipe.image = "agua.jpg"
    delicious.show()


app = App(title="James' Cocktail Cabinet", width = 800, height = 480)
# The main menu page
menu = Box(app, layout = "grid")
message = Text(menu, text = "What drink would you like to make?", grid = [0, 0, 5, 1,], align = "left", size = "36")
agua = PushButton(menu, command = valencia, text = "Agua da Valencia", grid = [0, 1])
agua.width = 15
bubbly = PushButton(menu, command = jack, text = "Bubbly Jack Rose", grid = [1, 1])
bubbly.width = 15
champs = PushButton(menu, command = elysee, text = "Champs Elysee", grid = [2, 1])
champs.width = 15
corpse = PushButton(menu, command = revive, text = "Corpse Reviver No 2", grid = [3, 1])
corpse.width = 15
martini = PushButton(menu, command = drymartini, text = "Dry Martini", grid = [4, 1])
martini.width = 15
espresso = PushButton(menu, command = coffee, text = "Espresso Martini", grid = [0, 2])
espresso.width = 15
frenchy = PushButton(menu, command = french75, text = "French 75", grid = [1, 2])
frenchy.width = 15
inam = PushButton(menu, command = inamorata, text = "Inamorata", grid = [2, 2])
inam.width = 15
last = PushButton(menu, command = last_word, text = "Last Word", grid = [3, 2])
last.width = 15
marg = PushButton(menu, command = margarita, text = "Margarita", grid = [4, 2])
marg.width = 15
back = Picture(menu, image = "menu.jpg", grid = [0, 3, 5, 1])
negroni = PushButton(menu, command = negroninegroni, text = "Negroni", grid = [0, 4])
negroni.width = 15
queenie = PushButton(menu, command = queen, text = "Queen Mother", grid = [1, 4])
queenie.width = 15
tommy = PushButton(menu, command = tc, text = "Tom Collins", grid = [2, 4])
tommy.width = 15
vesper = PushButton(menu, command = jamesbond, text = "Vesper", grid = [3, 4])
vesper.width = 15
off = PushButton(menu, command = switchoff, text = "Power off", grid = [4, 4])
off.width = 15
# The recipe page section - is hidden when the app launches
delicious = Box(app, visible = False)
recipe = PushButton(delicious, command = show_menu, text = '')
# This line makes the app run full screen, without a title bar
# Remove it if you want to run this in a window rather than as a kiosk
app.tk.attributes("-fullscreen",True)
app.display()
