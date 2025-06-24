console.log("Inicio")

setTimeout(() => {
    console.log("Timeout 1")
}, 2000)
console.log("Fin")

setTimeout(() => {
    console.log("Esto se ejecuta despues de 0 segundos pero despues del inicio")
}, 0)
console.log("Final")