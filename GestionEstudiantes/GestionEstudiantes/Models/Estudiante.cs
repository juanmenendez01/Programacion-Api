using System;
using System.Collections.Generic;

namespace GestionEstudiantes.Models;

public partial class Estudiante
{
    public int IdEstudiante { get; set; }

    public string Nombre { get; set; } = null!;

    public string Email { get; set; } = null!;

    public virtual ICollection<Curso> IdCursos { get; set; } = new List<Curso>();

}
