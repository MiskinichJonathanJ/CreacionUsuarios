import argparse
import sys
from utils.logger import setup_logger
from utils.user_ops import create_user, add_to_group

def  main():
    parser = argparse.ArgumentParser(description='Crecion Usuario - Crear usuarios y asignar grupos')
    parser.add_argument('-c', '--create', action="store_true" ,help='Crear un nuevo  usuario')
    parser.add_argument('-u', '--user', type=str, help="Nombre del usuario")
    parser.add_argument('-p', '--password', type=str, help="Contraseña del usuarioa crear")
    parser.add_argument('-g',  '--group', type=str, help="Grupos al que asignar  al usuario")

    args = parser.parse_args()
    logger = setup_logger()

    if args.create:
        if not args.user or not args.password:
            loggerr.error("Se debe especificar  usuario y password  al  crear un usuario")
            sys.exit(1)
        sucess = create_user(args.user, args.password,  logger)
        if args.group and sucess:
            groups = args.group.split(",")
            add_to_group(args.user, groups, logger)

if __name__ == "__main__":
    main()
