#CHECK EVERYTHING
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Screen size and color
Window.size = (400, 600)

class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.width = Window.size[0]
        self.height = Window.size[1]
        self.add_gradient()



    def add_gradient(self):
        alpha_channel_rate = 0
        increase_rate = 1 / self.width

        for sep in range(self.width):
            self.canvas.add(Color(rgba=(100/225, 0, 190/255, alpha_channel_rate)))
            self.canvas.add(Line(points=[sep, 0, sep, self.height], width=1))
            alpha_channel_rate += increase_rate

        # Landing Page
        self.cols = 1
        self.padding = 100
        self.spacing = 30
        self.title = Label(
            text='Lvcky Guesses',
            color=(0,0,0.5,1),
            font_size= 50
            )
        self.add_widget(self.title)

        # Adding Landing page buttons
        self.start = Button(
            text='START',
            font_size=15,
        )
        self.add_widget(self.start)
        self.start.bind(on_press=self.displayStart)


        self.instructions = Button(
            text='INSTRUCTIONS',
            font_size=15,
        )
        self.add_widget(self.instructions)

        self.end = Button(
            text='END',
            font_size=15,
        )
        self.add_widget(self.end)

    def displayStart(self,instance):
        self.land = Label(
            text="Lvcky Guesses",
            font_size= 50
        )
        self.add_widget(self.land)

        self.quest = Label(
            text='Can you guess the 6 lucky Numbers?',
            font_size= 15
        )
        self.add_widget(self.quest)

Window.size = (400, 600)

class Entry(GridLayout):
    def __init__(self, **kwargs):
        super(Entry, self).__init__(**kwargs)

        self.cols = 1
        self.padding = 100
        self.spacing = 30
        self.title = Label(
            text='Lvcky Guesses',
            color=(0, 0, 0.5, 1),
            font_size=50
        )
        self.add_widget(self.title)

        self.quest = Label(
            text='Can you guess the 6 lucky Numbers?',
            font_size=15
        )
        self.add_widget(self.quest)

        self.range = Label(
            text='Enter your guess (1-99): ',
            font_size=15
        )
        self.add_widget(self.range)

        self.player = TextInput(
            hint_text="Player Guess: ",
            multiline=False,
            font_size=15,
            size=(20,20)
        )

        self.add_widget(self.player)

        self.attempts = GridLayout()
        self.cols = 1
        self.attempbox = Label(text='Your Attempts = 6 ')
        self.add_widget(self.attempbox)

        # Input Button
        self.input = Button(text='ENTER')
        self.add_widget(self.input)

        # Input Message Display
        self.display = Label(text='Result on Entry')
        self.add_widget(self.display)

        # Adding Reveal Box
        self.reveal = Label(text='The Lucky Numbers are: ')
        self.add_widget(self.reveal)




class Lucky(App):
    def build(self):
        return Entry()

if __name__ == '__main__':
    Lucky().run()
