import os
import pathlib

from dotenv import load_dotenv
from loguru import logger

is_env_file = os.getenv("CONFIG_SOURCE", "env_file") == "env_file"


class SystemConfig:
    __loaded: bool = False
    ROOT_DIR: str = None

    @staticmethod
    def load():
        logger.info("Loading from env file: {}", is_env_file)
        if is_env_file:
            logger.info("Loading from env file: trait-seeker.conf")
            from dotenv import find_dotenv
            load_dotenv(find_dotenv(filename='trait-seeker.conf', raise_error_if_not_found=True))
        SystemConfig._set_root_dir()
        Constants.load()
        SystemConfig.__loaded = True

    @staticmethod
    def get(key: str, default=None):
        if not SystemConfig.__loaded and is_env_file:
            SystemConfig.load()
        return os.getenv(key, default)

    @staticmethod
    def get_vital(key: str):
        if not SystemConfig.__loaded:
            SystemConfig.load()
        env_val = os.getenv(key)
        if env_val:
            return env_val
        raise Exception(f"Mandatory parameter: {key} not available in env | Env file read: {is_env_file} ")

    @staticmethod
    def _set_root_dir():
        SystemConfig.ROOT_DIR = str(pathlib.Path("./files").absolute())
        os.makedirs(SystemConfig.ROOT_DIR, exist_ok=True)


class Constants:
    MODEL_PATH: str
    DATA_PATH: str

    @staticmethod
    def load():
        Constants.MODEL_PATH = os.path.join(SystemConfig.ROOT_DIR, "models")
        Constants.DATA_PATH = os.path.join(SystemConfig.ROOT_DIR, "data")
