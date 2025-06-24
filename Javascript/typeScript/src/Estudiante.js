"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Nota = exports.Estudiante = void 0;
class Estudiante {
    constructor(id, nombre, apellido) { }
    getEstudiante(id) {
        console.log("estudiante id: " + id);
    }
    addEstudiante(id) {
        console.log("Estudiante añadido: " + id);
    }
    deleteEstudiante(id) {
        console.log("Estudiante eliminado" + id);
    }
}
exports.Estudiante = Estudiante;
class Nota {
    constructor(idNota, id, Matematicas, Ingles, Español) {
    }
    getNota(idNota) {
        console.log("Notas listada: " + idNota);
    }
    addNota(idNota) {
        console.log("Nota actualizada: " + idNota);
    }
    deleteNota(idNota) {
        console.log("Nota eliminada: " + idNota);
    }
}
exports.Nota = Nota;
