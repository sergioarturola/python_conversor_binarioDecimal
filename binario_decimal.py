from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#funciones con la logica
#decimal a binario
def toBinario(numero):
    lista = []
    while numero > 0:

        resto = numero%2
        numero = int(numero/2)
        lista.append(resto)


    lista.reverse()
    s = [str(i) for i in lista] #tengo que pasarlo a string si no, no funciona el join
    num_bin = ''.join(s)

    return num_bin

#de binario a decimal
def toDecimal(binary):
    sum = 0
    cont = 0

    for i in binary:
    
        sum += pow(int(i)*2, cont)
        cont += 1
    
    return sum


#para saber opcion selelccionada
def obtener():
    seleccion = combo_opciones.get()

    if seleccion == "Binario":
        try:
            numero = int(txtNumero.get())
            print(numero +2)
            conversion = toBinario(numero)
            messagebox.showinfo(message="El numero en decial es: "+conversion, title="Resultado")
        except ValueError:
            messagebox.showinfo(message="Solo numeros enteros", title="Atencion")
    else:
        binario = txtNumero.get()
        convertir = toDecimal(binario)
        messagebox.showinfo(message="El numero en decial es: "+str(convertir), title="Resultado")


#interfaz grafica
ventana = Tk()
ventana.geometry("300x200")
ventana.title("Convertidor binario")

#colocando los componentes
#etiqueta de la caja
etiquetaNumero = Label(ventana, text="Numero")
etiquetaNumero.grid(column=0,row=0)

#texto de entrada
txtNumero = Entry(ventana)
txtNumero.grid(column=1, row= 0)
txtNumero.focus()
#etiqueta del combobox
etiquetaCombo = Label(ventana, text="Convertir a")
etiquetaCombo.grid(column=1, row = 2)
#combobox
combo_opciones = ttk.Combobox(ventana)
combo_opciones['values'] = ('Binario', 'Decimal')
combo_opciones.grid(column=1, row=3)
#boton
btnConvertir = Button(ventana, text="Convertir", command=obtener)
btnConvertir.grid(column=1, row=4)

ventana.mainloop()



