function mostrarMensaje()
{
    var estatura = parseFloat(document.getElementById("Estatura").value)
    var peso = parseFloat(document.getElementById("Peso").value)
    var estadoCivil = document.getElementById("estadoCivil").value
    var resultado

    const parametroEstatura = 1.30
    const parametroPeso = 100
    const parametroEstadoCivil = "soltero"
    

    if (estatura >= parametroEstatura){
        if(peso <= parametroPeso){
            if(estadoCivil == parametroEstadoCivil){
                resultado = "saludable"
            } else{
                resultado = "no saludables, no es soltero"
            }
        } else{
            resultado = "no saludable, esta gordo"
        }
    }else{
        resultado = "no saluda, es enano"
    }
}