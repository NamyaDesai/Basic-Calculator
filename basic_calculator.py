import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title and size of the main window
        self.title("Calculator")
        self.geometry("400x500")
        
        # Initialize the expression variable to hold the calculator input
        self.expression = ""
        
        # Entry widget for the display (where numbers and results are shown)
        self.display = tk.Entry(self, font=('Arial', 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
        # relief="solid" gives a solid border to the Entry widget
        
        # Buttons layout (list of button labels)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place buttons in the grid
        for i, button in enumerate(buttons):
            tk.Button(self, text=button, font=('Arial', 18), 
                      command=lambda b=button: self.on_button_click(b)).grid(row=i//4+1, column=i%4, sticky="nsew")
            # sticky="nsew" makes the button expand to fill the grid cell in all directions (north, south, east, west)

        # Configure rows and columns to expand with window resizing
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
    
    # Function to handle button clicks
    def on_button_click(self, char):
        if char == "=":  # If equal button is clicked, evaluate the expression
            try:
                self.expression = str(eval(self.expression))  # Evaluate and convert result to string
            except Exception as e:
                self.expression = "Error"  # Display error if evaluation fails
        else:
            self.expression += str(char)  # Append clicked button's character to the expression
        self.update_display()  # Update the display with the current expression
    
    # Function to update the display
    def update_display(self):
        self.display.delete(0, tk.END)  # Clear the current display
        self.display.insert(0, self.expression)  # Insert the current expression into the display

if __name__ == "__main__":
    app = Calculator()  # Create an instance of the Calculator class
    app.mainloop()  # Run the application's main loop