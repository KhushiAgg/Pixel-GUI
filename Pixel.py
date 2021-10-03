from tkinter import *
#import PIL
from PIL import Image, ImageTk
from tkinter.colorchooser import askcolor
#from tkinter.filedialog import askopenfilename, asksaveasfilename as saveAs

class Pixel(object):

    WIDTH, HEIGHT = 600, 400
    PEN_SIZE = 5.0
    COLOR = 'black'

    def __init__(self):
            self.window = Tk()

            self.window.title("Pixel")
            ico = Image.open("icon.jpg")
            photo = ImageTk.PhotoImage(ico)
            self.window.wm_iconphoto(False, photo)
            self.window.geometry("600x400")

            # Creating a photoimage object to use image
            photo1 = PhotoImage(file = "pen.png")
            photo2 = PhotoImage(file = "brush.png")
            photo3 = PhotoImage(file = "color.jpg")
            photo4 = PhotoImage(file = "eraser.png")
            # Resizing image to fit on button
            pen = photo1.subsample(20, 20)
            brush = photo2.subsample(20,20)
            color = photo3.subsample(10,10)
            eraser = photo4.subsample(10,10)

            #items to draw with
            self.pen_button = Button(self.window, image=pen, command=self.use_pen)
            self.pen_button.grid(row=0, column=0)

            self.brush_button = Button(self.window, image = brush, command=self.use_brush)
            self.brush_button.grid(row=0, column=1)

            self.color_button = Button(self.window, image=color, command=self.choose_color)
            self.color_button.grid(row=0, column=2)

            self.eraser_button = Button(self.window, image=eraser, command=self.use_eraser)
            self.eraser_button.grid(row=0, column=3)

            self.choose_size_button = Scale(self.window, from_=1, to=10, orient=HORIZONTAL)
            self.choose_size_button.grid(row=0, column=4)

            #canvas to draw on:
            self.canvas = Canvas(self.window, bg = "white" , height = self.HEIGHT, width = self.WIDTH)
            self.canvas.grid(row=1, columnspan=5)

            #creating menubar
            menubar = Menu(self.window)

            #file menu
            file = Menu(menubar, tearoff=0)
            menubar.add_cascade(label='File', menu= file)
            file.add_command(label = 'New', command= self.NewFile)
            file.add_command(label ='Open', command = None)
            file.add_command(label ='Save As', command = self.Savefile)
            file.add_command(label ='Clear', command = None)
            #file.add_command(label ='Print', command = None)
            file.add_separator()
            file.add_command(label ='Exit', command = self.window.destroy)
            
            #Image Menu
            image = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label ='Image', menu = image)
            image.add_command(label ='Select', command = None)
            image.add_command(label ='Resize', command = None)
            image.add_command(label ='Crop', command = None)
            image.add_command(label ='Rotate', command = None)

            # display Menu
            self.window.config(menu = menubar)
            self.setup()
            self.window.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.pixel)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
    
    def use_pen(self):
        self.activate_button(self.pen_button)
    
    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def pixel(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def NewFile(self):
        print("New File!")

    def Savefile(self):
        print("File Saved!")

    # def OpenFile(self):
    #     self.myfile = askopenfilename(mode ='r', filetypes =[('All Files', '*.*'), ('PNG Files', '*.png'), ('JPEG Files', '*.jpeg')])
    #     if self.myfile is not None:
    #         content = self.myfile.read()
    #         print(content)

    # def save(self):
    #     filename=saveAs(title="Save image as...",filetype=(("PNG images","*.png"),("JPEG images","*.jpg"),("GIF images","*.gif")))
    #     self.image1.save(filename)    

if __name__ == '__main__':
    Pixel()