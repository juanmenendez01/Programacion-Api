"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Estudiante_1 = require("./Estudiante");
// setTimeout(function (): void {
//     console.log("Hola desde funcion anonima TS");
// }, 2000)
// const sumar = (a: number, b: number) : number => a+b
// console.log(sumar(4, 8))
// function saludar(nombre: string, callback: ()=>void): void{
//     console.log("Hola " + nombre)
//     callback();
// }
// saludar("wilson", ()=>{
//     console.log("Callback ejecutado")
// })
// async function obtenerDatos() {
//     const data = await fetch("https://dog.ceo/api/breeds/image/random");
//     const json = await data.json();
//     console.log(json) 
// }
// obtenerDatos()
//Ejemplo de promesa en TS
// const promesa: Promise<string> = new Promise((resolve, reject)=>{
//     setTimeout(()=>{
//         resolve("Hecho!!")
//     }, 2000)
// })
// promesa.then(console.log)
// const suma = (...numeros: number[]): number => numeros.reduce((a,b)=> a + b)
// console.log(suma(1,2,3,5))
// interface Persona{
//     nombre: string;
//     edad: number;
// }
// const persona: Persona = {nombre: "Juan", edad: 99}
// console.log("Hola " + persona.nombre + " Tienes "+ persona.edad + " años de edad")
// console.log("El numero pi es " + Pi)
// class Animal{
//     constructor(public nombre: string){
//     }
//     sonido(): void{
//             console.log(this.nombre + " Hace un ruido")
//         }
// }
const estudiante = new Estudiante_1.Estudiante(1, "Juan andres", "Villarraga");
console.log("Estudiante: " + estudiante.addEstudiante(1));
