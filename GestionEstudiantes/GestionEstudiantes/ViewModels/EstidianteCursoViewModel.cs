using GestionEstudiantes.Models;

namespace GestionEstudiantes.ViewModels
{
    public class EstidianteCursoViewModel
    {
        public Estudiante Estudiante { get; set; } = new();
        public List<int> Cursoseleccionado { get; set; } = new(); // Para los IDs de cursos seleccionados
        public List<Curso> CursosDisponibles { get; set; } = new();
        public List<Estudiante> Estudiantes { get; set; } = new();
        public string Filtro { get; set; }
    }
}
