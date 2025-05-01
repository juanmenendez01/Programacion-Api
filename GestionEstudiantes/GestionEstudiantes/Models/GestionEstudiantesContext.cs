using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace GestionEstudiantes.Models;

public partial class GestionEstudiantesContext : DbContext
{
    public GestionEstudiantesContext()
    {
    }

    public GestionEstudiantesContext(DbContextOptions<GestionEstudiantesContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Curso> Cursos { get; set; }

    public virtual DbSet<Estudiante> Estudiantes { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see https://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Server=localhost; Database=GestionEstudiantes; Trusted_Connection=True; TrustServerCertificate=True;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Curso>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PK__Curso__3214EC072C6CF728");

            entity.ToTable("Curso");

            entity.Property(e => e.Nombre)
                .HasMaxLength(255)
                .IsUnicode(false);
        });

        modelBuilder.Entity<Estudiante>(entity =>
        {
            entity.HasKey(e => e.IdEstudiante).HasName("PK__Estudian__B5007C247954740C");

            entity.ToTable("Estudiante");

            entity.Property(e => e.Email)
                .HasMaxLength(255)
                .IsUnicode(false);
            entity.Property(e => e.Nombre)
                .HasMaxLength(255)
                .IsUnicode(false);

            entity.HasMany(d => d.IdCursos).WithMany(p => p.IdEstudiantes)
                .UsingEntity<Dictionary<string, object>>(
                    "EstudianteCurso",
                    r => r.HasOne<Curso>().WithMany()
                        .HasForeignKey("IdCurso")
                        .OnDelete(DeleteBehavior.ClientSetNull)
                        .HasConstraintName("FK__Estudiant__IdCur__619B8048"),
                    l => l.HasOne<Estudiante>().WithMany()
                        .HasForeignKey("IdEstudiante")
                        .OnDelete(DeleteBehavior.ClientSetNull)
                        .HasConstraintName("FK__Estudiant__IdEst__60A75C0F"),
                    j =>
                    {
                        j.HasKey("IdEstudiante", "IdCurso").HasName("PK__Estudian__C5858E59A51E341C");
                        j.ToTable("EstudianteCurso");
                    });
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
