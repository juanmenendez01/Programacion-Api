import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Usuario } from './entities/usuario.entity';
import { CreateUsuarioDto } from './dto/create-usuario.dto';
import { UpdateUsuarioDto } from './dto/update-usuario.dto';

@Injectable()
export class UsuarioService {
  constructor(
    @InjectRepository(Usuario)
    private usuarioRepository: Repository<Usuario>,
  ) {}

  create(dto: CreateUsuarioDto): Promise<Usuario> {
    const nuevo = this.usuarioRepository.create(dto);
    return this.usuarioRepository.save(nuevo);
  }

  findAll(): Promise<Usuario[]> {
    return this.usuarioRepository.find();
  }

  async findOne(id: number): Promise<Usuario> {
  const usuario = await this.usuarioRepository.findOneBy({ id });
  if (!usuario) {
    throw new Error(`Usuario con ID ${id} no encontrado`);
  }
  return usuario;
}


  async update(id: number, dto: UpdateUsuarioDto): Promise<Usuario> {
  await this.usuarioRepository.update(id, dto);

  const usuario = await this.usuarioRepository.findOneBy({ id });
  if (!usuario) {
    throw new NotFoundException(`Usuario con ID ${id} no encontrado`);
  }

  return usuario;
}

  async remove(id: number): Promise<void> {
    await this.usuarioRepository.delete(id);
  }
}
