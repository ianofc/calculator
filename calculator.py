import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Científica")
        self.master.geometry("400x600")
        
        self.expression = ""
        
        self.display = tk.Entry(master, font=('Arial', 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()
        self.create_grid_weights()

    def create_buttons(self):
        buttons = [
            ('AC', 1, 0), ('DEL', 1, 1), ('(', 1, 2), (')', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, font=('Arial', 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

    def create_grid_weights(self):
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == '=':
            self.calculate_result()
        elif char in ['sin', 'cos', 'tan', 'sqrt']:
            self.apply_function(char)
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        try:
            # Avalia a expressão e atualiza a exibição
            self.expression = str(eval(self.expression))
            self.update_display()
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")
            self.expression = ""

    def apply_function(self, func):
        try:
            if func == 'sin':
                self.expression = str(math.sin(math.radians(float(self.expression))))
            elif func == 'cos':
                self.expression = str(math.cos(math.radians(float(self.expression))))
            elif func == 'tan':
                self.expression = str(math.tan(math.radians(float(self.expression))))
            elif func == 'sqrt':
                self.expression = str(math.sqrt(float(self.expression)))
            self.update_display()
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()