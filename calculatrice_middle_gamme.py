from tkinter import *
import math

# Initialisation de la fenêtre
window = Tk()
window.title("Calculatrice")

# Ajouter un champ de saisie
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


# Fonction pour ajouter un chiffre dans le champ de saisie
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Fonction pour effacer le champ de saisie
def button_clear():
    e.delete(0, END)


# Fonction pour effectuer les opérations mathématiques
def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(0, "Erreur : division par zéro")
    except:
        e.delete(0, END)
        e.insert(0, "Erreur")


# Ajouter les boutons à la calculatrice
button_list = ['C', '(', ')', '%', 'sin', 'cos', 'tan', 'sqrt',
               '7', '8', '9', '/', 'x^2', 'x^y',
               '4', '5', '6', '*', '1/x', 'log10',
               '1', '2', '3', '-', 'x^(1/y)', 'log2',
               '0', '.', '=', '+', 'mean', 'std',
               '', '', '', '', 'var', 'pi']

for i, digit in enumerate(button_list):
    if digit == '':
        continue
    button = Button(window, text=digit, padx=40, pady=20, command=lambda x=digit: button_click(x))
    if digit == 'C':
        button.config(command=button_clear)
    elif digit == '=':
        button.config(command=button_equal)
    elif digit == 'sin':
        button.config(command=lambda: button_click('sin('))
    elif digit == 'cos':
        button.config(command=lambda: button_click('cos('))
    elif digit == 'tan':
        button.config(command=lambda: button_click('tan('))
    elif digit == 'sqrt':
        button.config(command=lambda: button_click('sqrt('))
    elif digit == 'x^2':
        button.config(command=lambda: button_click('**2'))
    elif digit == 'x^y':
        button.config(command=lambda: button_click('**'))
    elif digit == '1/x':
        button.config(command=lambda: button_click('1/'))
    elif digit == 'log10':
        button.config(command=lambda: button_click('math.log10('))
    elif digit == 'log2':
        button.config(command=lambda: button_click('math.log2('))
    elif digit == 'x^(1/y)':
        button.config(command=lambda: button_click('**(1/)'))
    elif digit == 'mean':
        button.config(command=lambda: button_click('statistics.mean('))
    elif digit == 'std':
        button.config(command=lambda: button_click('statistics.stdev('))
    elif digit == 'var':
        button.config(command=lambda: button_click('statistics.variance('))
    elif digit == 'pi':
        button.config(command=lambda: button_click('math.pi'))
    button.grid(row=1 + i//6, column=i%6)

# Boucle principale
window.mainloop()
