// console.log("Corto las verduras");
// console.log("Las  pongo en la sarten");
// console.log("Cocino las verduras");


// Asincronicos
// console.log("Pongo la ropa en la lavadora");
// setTimeout(() => {
//     console.log("saco la ropa de la lavadora");
// }, 3000);
// console.log("Preparo el almuerzo");

// Funcion de la pizza con callback
/*
function pedirPizza(callback){
    console.log("pidiendo pizza...");
    setTimeout(() => {
        console.log("Pizza lista");
        callback();
    }, 2000);
}
function comerPizza(){
    console.log("Ahora puedo comer la pizza");
}

pedirPizza(comerPizza);
*/

// verificar si un candidato cumple con los requisitos
/*

function verificarCandidato(nombre, cumpleRequisitos, noCumpleRequisitos) {

    const cumple = Math.random()> 0.5

    if(cumple)
{
    cumpleRequisitos(nombre);
}else
{
    noCumpleRequisitos(nombre);
}
}

*/
//Definir los callback
/*
function aceptarCandidato(nombre){
    console.log(`${nombre} ha sido aceptado. Se procede con la oferta`)
}

function rechazarCandidato(nombre){
    console.log(`${nombre} no ha sido aceptado. no cumple con los reuisitos`)
}

verificarCandidato("Juan", aceptarCandidato, rechazarCandidato)
*/

// **************Ejemplo de promeza**********************
/*
const Promeza = new Promise((resolve, reject) =>{
    let pizzaLista = false;

    if (pizzaLista)
    {
        resolve("La pizza esta lista");
    }
    else
    {
        reject("No se pudo hacer la pizza");
    }
})

Promeza
.then((mensaje)=> console.log(mensaje))
.catch((mensaje)=> console.log(mensaje))
*/

// Funcion Async para hacer cafe
/*
function hervirAgua(){
    return new Promise((resolve)=> {
        console.log("Ponioendo a hervir el agua");
        setTimeout(()=>{
            resolve("el agua esta lista");
        }, 3000)
    })
}
async function hacerCafe() {
    console.log("Preparando para hacer cafe");
    const agua = await hervirAgua();
    console.log(agua);
    console.log("el cafe esta listo");
}

hacerCafe();
*/

//Mas de una espera (await) Dentro de una funcion Async
/*
function validarPedido(IdPedido){
    return new Promise((resolve)=>{
        console.log(`validando el pedido ${IdPedido}`)
        setTimeout(()=>{
            resolve(`Pedido ${IdPedido} validado`)
        });
    }, 4000);
}

function notificarAlmacen(IdPedido){
    return new Promise((resolve)=>{
        console.log(`Notificando al almacen sobre el pedido ${IdPedido}`)
        setTimeout(()=>{
            resolve(`Almacen notificado para el pedido ${IdPedido}`)
        }, 4000)
    })
    
}

function confirmarFinanza(IdPedido)
{
    return new Promise((resolve)=>{
        console.log(`Confirmando a finanzas el pedido ${IdPedido}`);
        setTimeout(()=>{
            resolve(`Finanzas confirmadas para el pedido ${IdPedido}`);
        }, 4000)
    })
}

async function procesarPedido(IdPedido){
    console.log(`Iniciando el pedido ${IdPedido}`);
    const resultadoValidacion = await validarPedido(IdPedido);
    console.log(resultadoValidacion);

    const resultadoAlmacen = await notificarAlmacen(IdPedido);
    console.log(resultadoAlmacen);

    const resultadoFinanza = await confirmarFinanza(IdPedido);
    console.log(resultadoFinanza);

    console.log(`Pedido ${IdPedido} Procesado exitosamente`)
}

procesarPedido(123444);
*/