using System;
using System.Collections.Generic;

namespace GestionEstudiantes.Models;

public partial class Curso
{
    public int Id { get; set; }

    public string Nombre { get; set; } = null!;

    public int Creditos { get; set; }

    public virtual ICollection<Estudiante> IdEstudiantes { get; set; } = new List<Estudiante>();
}
