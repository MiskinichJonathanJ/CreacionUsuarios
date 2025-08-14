import  logging
import os

def setup_logger():
    # crear directorio si no existe
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/actions_of_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
     )

    return logging.getLogger()

