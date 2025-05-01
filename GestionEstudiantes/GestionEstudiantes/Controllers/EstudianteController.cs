using System.Threading.Tasks;
using GestionEstudiantes.Models;
using GestionEstudiantes.ViewModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace GestionEstudiantes.Controllers
{
    public class EstudianteController : Controller
    {
        private readonly GestionEstudiantesContext _context;

        public EstudianteController(GestionEstudiantesContext context)
        {
            _context = context;
        }
        public async Task<IActionResult> Index(string filter = "")
        {
            var filtro = _context.Estudiantes.AsQueryable();

            if (!string.IsNullOrWhiteSpace(filter))
            {
                filtro = filtro.Where(e => e.Nombre.Contains(filter));
            }
            var viewmodel = new EstidianteCursoViewModel
            {
                Estudiantes = await filtro
                   .Include(e => e.IdCursos)
                   .ToListAsync(),

                CursosDisponibles = await _context.Cursos.ToListAsync(),

                Filtro = filter
            };

            return View(viewmodel);
        }
        
        [HttpPost]
        public async Task<IActionResult> Registro(Estudiante estudiante, List<int> Cursoseleccionado)
        {
            if (ModelState.IsValid)
            {
                // Obtener los cursos seleccionados desde la base de datos
                var cursos = await _context.Cursos
                    .Where(c => Cursoseleccionado.Contains(c.Id))
                    .ToListAsync();

                if (estudiante.IdEstudiante == 0)
                {
                    // NUEVO estudiante
                    foreach (var curso in cursos)
                    {
                        estudiante.IdCursos.Add(curso);
                    }

                    _context.Estudiantes.Add(estudiante);
                }
                else
                {
                    // ACTUALIZACIÓN de estudiante
                    var estudianteExistente = await _context.Estudiantes
                        .Include(e => e.IdCursos)
                        .FirstOrDefaultAsync(e => e.IdEstudiante == estudiante.IdEstudiante);

                    if (estudianteExistente != null)
                    {
                        // Actualizar campos básicos
                        estudianteExistente.Nombre = estudiante.Nombre;
                        estudianteExistente.Email = estudiante.Email;

                        // Limpiar y reasignar cursos
                        estudianteExistente.IdCursos.Clear();

                        foreach (var curso in cursos)
                        {
                            estudianteExistente.IdCursos.Add(curso);
                        }
                    }
                }

                await _context.SaveChangesAsync();
            }

            ModelState.Clear();

            // Recargar el ViewModel
            var viewmodel = new EstidianteCursoViewModel
            {
                Estudiante = new Estudiante(),
                Estudiantes = await _context.Estudiantes
                    .Include(e => e.IdCursos)
                    .ToListAsync(),

                CursosDisponibles = await _context.Cursos.ToListAsync()
            };

            return View("Index", viewmodel);
        }


        public async Task<IActionResult> Delete(int idEstudiante, int IdCurso)
        {
            var estudiante = await _context.Estudiantes
                .Include(e => e.IdCursos)  
                .FirstOrDefaultAsync(e => e.IdEstudiante == idEstudiante);

            if (estudiante == null)
            {
                return NotFound();
            }

            // Buscar el curso a eliminar de la colección de cursos del estudiante
            var curso = estudiante.IdCursos.FirstOrDefault(c => c.Id == IdCurso);

            if(curso != null)
            {
                estudiante.IdCursos.Remove(curso);
            }

            await _context.SaveChangesAsync();

            
            return RedirectToAction("Index");
        }

        public async Task<IActionResult> Update(int idEstudiante)
        {
            var estudiante = await _context.Estudiantes
            .Include(e => e.IdCursos)
            .FirstOrDefaultAsync(e => e.IdEstudiante == idEstudiante);

            if (estudiante == null)
            {
                return NotFound();
            }

            var viewmodel = new EstidianteCursoViewModel
            {
                Estudiante = estudiante,
                Estudiantes = await _context.Estudiantes
                    .Include(e => e.IdCursos)
                    .ToListAsync(),
                CursosDisponibles = await _context.Cursos.ToListAsync()
            };

            return View("Index", viewmodel);
        }

    }
}
