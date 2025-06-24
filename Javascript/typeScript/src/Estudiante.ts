export class Estudiante{

    constructor(id: number, nombre: string, apellido: string){}

    getEstudiante(id: number): void{
        console.log("estudiante id: " + id)
    }

    addEstudiante(id: number): void{
        console.log("Estudiante añadido: " + id)
    }

    deleteEstudiante(id: number){
        console.log("Estudiante eliminado" + id)
    }
}

export class Nota{
    constructor(idNota: number, id: number, Matematicas: number, Ingles: number, Español: number){

    }

    getNota(idNota: number){
        console.log("Notas listada: " + idNota)
    }
    addNota(idNota: number){
        console.log("Nota actualizada: " + idNota)
    }
    deleteNota(idNota: number){
        console.log("Nota eliminada: " + idNota)
    }
}

interface Estudiantes{
    id: number;
    Nombre: string;
    Apellido: string;
}

interface Notas{
    idNota: number;
    id: string;
    Matematicas: string;
    Español: string;
    Ingles: string;
}