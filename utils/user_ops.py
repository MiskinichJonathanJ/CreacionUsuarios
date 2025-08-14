import subprocess

def create_user(username, pass_user, logger):
    try:
        subprocess.run(["sudo", "useradd", username], check=True)
        subprocess.run(["sudo", "chpasswd"], input=f"{username}:{pass_user}".encode(), check=True)
        logger.info(f"Usuario {username} creado con exito.")
        return  True
    except subprocess.CalledProcessError as  e:
        logger.error(f"Error al crear  al  usuario {username}: {e}")
        return False


def add_to_group(username, groups, logger):
    try:
        subprocess.run(["sudo", "usermod", "-aG", ','.join(groups), username], check=True)
        logger.info(f"El usuario {username} fue añadido a los grupos:  {','.join(groups)}")
        return True
    except Exception as e:
        logger.error(f"Error al añadir  al  usuario a  los grupos {','.join(groups)}: {e}")
        return False

