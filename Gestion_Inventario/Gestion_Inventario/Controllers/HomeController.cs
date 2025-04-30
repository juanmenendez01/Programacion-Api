using System.Diagnostics;
using Gestion_Inventario.Models;
using Gestion_Inventario.ViewModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using static Microsoft.EntityFrameworkCore.DbLoggerCategory;

namespace Gestion_Inventario.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        private readonly InventarioContext _context;
        private readonly ProductViewModels _model;

        public HomeController(ILogger<HomeController> logger, InventarioContext context)
        {
            _logger = logger;
            _context = context;
        }

        public async Task<IActionResult> Index(string filtroNombre = "")
        {
            var consulta = _context.Productos.AsQueryable();

            if (!string.IsNullOrWhiteSpace(filtroNombre))
            {
                consulta = consulta.Where(p => p.Nombre.Contains(filtroNombre));
            }

            var productos = await consulta.ToListAsync();

            var Lista_productos = new ProductViewModels
            {
                ListaProductos = productos,
                FiltroNombre = filtroNombre,

            };
            return View(Lista_productos);
        }
        [HttpPost]
        public async Task<IActionResult> Index(ProductViewModels model)
        {
            if(model.producto.IdProducto == 0)
            {
                _context.Productos.Add(model.producto);
            }
            else
            {
                _context.Productos.Update(model.producto);
            }

                
            await _context.SaveChangesAsync();



            return RedirectToAction("Index");
        }

        [HttpPost]
        public async Task<IActionResult> Delete(int id)
        {
            var eliminar = await _context.Productos.FirstOrDefaultAsync(p => p.IdProducto == id);

            if(eliminar != null)
            {
                _context.Productos.Remove(eliminar);
                await _context.SaveChangesAsync();
            }
            return RedirectToAction("Index");
        }

        public async Task<IActionResult> Update(int id)
        {
            var producto = await _context.Productos.FindAsync(id);

            var productViewModel = new ProductViewModels
            {
                producto = producto,
                ListaProductos = await _context.Productos.ToListAsync()
            };


            if (producto == null)
            {
                return NotFound();
            }

            return View("Index", productViewModel);
        }
        

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
