import tkinter
import calculate
from simpleeval import simple_eval
def concat_to_expression(symbol,equation):
    equation.set(equation.get() + str(symbol))

def evaluate(equation):
    try:
        equation.set(str(simple_eval(equation.get())))
    except:
        equation.set("Please enter a valid expression")

def clear_equation(equation):
    equation.set("")

# Create the global variable to represent the equation
expression = ""
def input_number(number, equation):
    global expression

    # Concatenate the string to create the expression
    expression = expression + str(number)
    equation.set(expression)


# Reset the calculator
def clear_input_field(equation):
    global expression 
    expression = ""
    equation.set("Enter the expression")

def main():
    window = tkinter.Tk()
    # Create the GUI window with specified parameters
    window.title("Calculator")
    window.geometry("360x250")
    equation = tkinter.StringVar()

    # Create an input field for the equation
    input_field = tkinter.Entry(window, textvariable=equation)
    input_field.place(height=100)

    # Create the grid for all the buttons
    input_field.grid(columnspan=4, ipadx=100, ipady=5)

    # Put a placeholder message for users
    equation.set("")

    # Creating buttons in appropriate positions
    _1 = tkinter.Button(window, text='1', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(1, equation), height=2, width=7)
    _1.grid(row=2, column=0)
    _2 = tkinter.Button(window, text='2', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(2, equation), height=2, width=7)
    _2.grid(row=2, column=1)
    _3 = tkinter.Button(window, text='3', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(3, equation), height=2, width=7)
    _3.grid(row=2, column=2)
    _4 = tkinter.Button(window, text='4', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(4, equation), height=2, width=7)
    _4.grid(row=3, column=0)
    _5 = tkinter.Button(window, text='5', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(5, equation), height=2, width=7)
    _5.grid(row=3, column=1)
    _6 = tkinter.Button(window, text='6', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(6, equation), height=2, width=7)
    _6.grid(row=3, column=2)
    _7 = tkinter.Button(window, text='7', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(7, equation), height=2, width=7)
    _7.grid(row=4, column=0)
    _8 = tkinter.Button(window, text='8', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(8, equation), height=2, width=7)
    _8.grid(row=4, column=1)
    _9 = tkinter.Button(window, text='9', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(9, equation), height=2, width=7)
    _9.grid(row=4, column=2)
    _0 = tkinter.Button(window, text='0', fg='white', bg='black', bd=0, command=lambda: concat_to_expression(0, equation), height=2, width=7)
    _0.grid(row=5, column=0)
    plus = tkinter.Button(window, text='+', fg='white', bg='black', bd=0, command=lambda: concat_to_expression('+', equation), height=2, width=7)
    plus.grid(row=2, column=3)
    minus = tkinter.Button(window, text='-', fg='white', bg='black', bd=0, command=lambda: concat_to_expression('-', equation), height=2, width=7)
    minus.grid(row=3, column=3)
    multiply = tkinter.Button(window, text='*', fg='white', bg='black', bd=0, command=lambda:  concat_to_expression('*', equation), height=2, width=7)
    multiply.grid(row=4, column=3)
    divide = tkinter.Button(window, text='/', fg='white', bg='black', bd=0, command=lambda: concat_to_expression('/', equation), height=2, width=7)
    divide.grid(row=5, column=3)
    equal = tkinter.Button(window, text='=', fg='white', bg='black', bd=0, command=lambda: evaluate(equation), height=2, width=7)
    equal.grid(row=5, column=2)
    clear = tkinter.Button(window, text='Clear', fg='white', bg='black', bd=0, command=lambda: clear_equation(equation), height=2, width=7)
    clear.grid(row=5, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()