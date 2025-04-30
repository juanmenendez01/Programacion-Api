using System;
using System.Collections.Generic;

namespace Gestion_Inventario.Models;

public partial class Producto
{
    public int IdProducto { get; set; }

    public string Nombre { get; set; } = null!;

    public string? Descripcion { get; set; }

    public decimal Precio { get; set; }

    public int CantidadDisponible { get; set; }
}
