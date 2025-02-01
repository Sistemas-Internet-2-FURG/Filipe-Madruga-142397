# Avaliações 1° bimestre

## CRUD
  
### Requisitos

- [x] Banco de dados de usuarios;
- [x] Banco de dados de registro (minimo duas tabelas dependentes);
  - Cadastro de aluno (precisa estar em ao menos uma turma, ou seja, precisa ter uma turma cadastrada previamente);
  - Cadastro de Turmas;

### Desenvolvido

#### Rotas

#### Definição das Tabelas

 Tabela de Usuarios
| userid TEXT (PK) | username TEXT | useremail TEX (PK) | userpassw TEXT                |
| ---------------- | ------------- | ------------------ | ----------------------------- |
| 1b80c831-4c...   | Fulano        | email@doiminio.com | scrypt:32768:8:1$w1IxaGwe5... |

Tabela de Turmas  
| classcode TEXT (PK) | classname TEXT            |
| ------------------- | ------------------------- |
| 23039               | Sistemas para Internet II |

Tabela de Alunos
| registration TEXT (PK) | studentname TEXT |
| ---------------------- | ---------------- |
| 000001                 | Fulano           |

Tabela de Turmas e Alunos
| class TEXT (FK)(PK) | registration TEXT (FK)(PK) |
| ------------------- | -------------------------- |
| 23039               | 000001                     |

#### Extras

- [ ] Filtro por aluno
- [ ] Filtro por turma
