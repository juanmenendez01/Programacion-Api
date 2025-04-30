using System.ComponentModel.DataAnnotations;
using Gestion_Inventario.Models;

namespace Gestion_Inventario.ViewModels
{
    public class ProductViewModels
    {
        
        public Producto producto {  get; set; } = new Producto();

        public List<Producto> ListaProductos { get; set;} = new List<Producto>();

        public string FiltroNombre {  get; set; }

    }
}
