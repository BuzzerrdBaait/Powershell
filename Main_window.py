import tkinter as tk


class PopupWindow(tk.Toplevel):
    def __init__(self, title, label_texts, bg_color="gray10", width=220, height=200):
        super().__init__()
        self.entries = []
        self.labels = []
        
        self.configure(bg=bg_color)  # Set background color
        
        for i, text in enumerate(label_texts):
            label = tk.Label(self, text=text, fg="green", bg=bg_color)
            label.pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries.append(entry)
            self.labels.append(label)
        
        button = tk.Button(self, text="Submit", command=self.get_values, bg=bg_color, fg="green")
        button.pack()
        
        self.title(title)
        self.geometry(f"{width}x{height}")  # Set window size

    def get_values(self):
        values = [entry.get() for entry in self.entries]
        print(*values)
        self.destroy()

def create_buttons(window, button_callbacks):
    frame = tk.Frame(window, bg="green")
    
    buttons = []
    for i in range(len(button_callbacks)):
        literal_string = repr(button_callbacks[i])
        buttons_name_whole = literal_string.split(" ")

        button = tk.Button(frame, text=buttons_name_whole[1], width=20, height=5, command=button_callbacks[i], bg="gray10", fg="green")
        buttons.append(button)

    for i, button in enumerate(buttons):
        row = i // 4
        col = i % 4
        button.grid(row=row, column=col)

    frame.pack()

    
def function1():
    PopupWindow("Function 1", ["Enter Value 1"])

def function2():
    PopupWindow("Function 2", ["Enter Value 1", "Enter Value 2"])

def function3():
    PopupWindow("Function 3", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function4():
    PopupWindow("Function 4", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def killcomputer():
    PopupWindow("Kill Computer", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function6():
    PopupWindow("Function 6", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function7():
    PopupWindow("Function 7", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function8():
    PopupWindow("Function 8", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function9():
    PopupWindow("Function 9", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function10():
    PopupWindow("Function 10", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function11():
    PopupWindow("Function 11", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

def function12():
    PopupWindow("Function 12", ["Enter Value 1", "Enter Value 2", "Enter Value 3"])

# Create the main window
window = tk.Tk()
window.configure(bg="green")

# Define the button callbacks
button_callbacks = [function1, function2, function3, function4, killcomputer, function6, function7, function8,
                    function9, function10, function11, function12]

# Create the buttons
create_buttons(window, button_callbacks)

# Start the main event loop
window.mainloop()