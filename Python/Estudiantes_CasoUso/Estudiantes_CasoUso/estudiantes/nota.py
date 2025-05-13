
def CrearNotas( Id,Nota_1, Nota_2, Nota_3):
    notas = [Id, Nota_1, Nota_2, Nota_3]
    return(notas)




def ConsultarNotas(Id, notas):
    for fila in notas:

        # if(fila[0] == Id):
        #     return fila

        if Id in fila:
            return(fila)
        else :
            print("el id no existe")

