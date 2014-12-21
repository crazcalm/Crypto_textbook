from tkinter import *
from tkinter import ttk

class Shift_cipher_gui(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Assigning varibales
        self.master = master
        self.feet = StringVar()
        self.meters = StringVar()

        # Building the GUI
        self.__mainframe()
        self.__mainframe_content(self.mainframe)

        # Create title of GUI
        master.title("Does this work?")


        # packing everything together
        self.pack()

    def __mainframe(self):
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.rowconfigure(0, weight=1)


    def __mainframe_content(self, frame):
        self.feet_entry = ttk.Entry(frame, width=7,
                textvariable=self.feet)
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(frame, textvariable=self.meters).grid(column=2,
                row=2, sticky=(W, E))
        ttk.Button(frame, text="Calculate",
                command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(frame, text='feet').grid(column=3, row=1,
                sticky=W)
        ttk.Label(frame, text='is equivalent to').grid(column=1,
                row=2, sticky=E)
        ttk.Label(frame, text='meters').grid(column=3, row=2,
                sticky=W)
    
    def calculate(self, *args):
        try:
            print(args)
            value = float(self.feet.get())
            self.meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
if __name__ == "__main__":
    root = Tk()
    test = Shift_cipher_gui(root)
    test.mainloop()
