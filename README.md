# Creacion de Usuarios y Asignacion de Permisos

Script en Python para crear usuarios, asignar permisos (grupos) y registrar logs de auditoría de cada acción en sistemas Linux. 

## Funcionalidades

- Crear usuarios del sistema (useradd + chpasswd).
- Asignar permisos mediante grupos (usermod -aG).
- Logging de auditoría a archivo (logs/actions.log) con nivel y timestamp.

## Arquitectura del Proyecto

UserManagerPlus/
│── user_manager.py        # Script principal (CLI)
│── utils/
│   ├── __init__.py
│   ├── logger.py          # Configuración de logging
│   └── user_ops.py        # Operaciones sobre usuarios/grupos
│── README.md              # Este documento

## Requisitos

- SO: Linux (probado en Ubuntu/Debian; funciona en sistemas con useradd/usermod).
- Python: 3.12 o superior.
- Permisos: Ejecutar con privilegios (ej. sudo) para crear/gestionar cuentas reales.
- Herramientas del sistema: useradd, usermod, chpasswd disponibles en $PATH.

## Instalación

```bash
# 1) Clonar el repo
https://github.com/MiskinichJonathanJ/CreacionUsuarios.git
cd CreacionUsuarios

# 2) (Opcional) Crear venv
python3 -m venv .venv && source .venv/bin/activate

# 3) No hay dependencias externas; listo para ejecutarse
```

## Uso basico (CLI)

```bash
sudo python3 user_manager.py --create --user <nombre_usuario> --password <contraseña>
```

### Ejemplo:

```bash
sudo python3 user_manager.py --create --user juan --password ClaveSegura123
```

## Crear Usuario y añadirlo a grupos
Puedes especificar varios grupos separados por comas:

```bash
sudo python3 user_manager.py --create --user juan --password ClaveSegura123 --group sudo,developers
```

## Parámetros disponibles

- -c, --create	  Indica que se va a crear un nuevo usuario.
- -u, --user	    Nombre del usuario a crear.
- -p, --password	Contraseña que se asignará al usuario.
- -g, --group	    Lista de grupos separados por comas a los que se añadirá el usuario.
