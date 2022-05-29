from dataclasses import dataclass
from environs import Env


@dataclass
class Bot:
    token: str


@dataclass
class DB:
    host: str
    db_name: str
    user: str
    password: str


@dataclass
class Redis:
    host: str
    password: str


@dataclass
class Config:
    bot: Bot
    redis: Redis


def load_config():
    env = Env()
    env.read_env()
    return Config(
        bot=Bot(
            token=env.str("BOT_TOKEN")
        ),
        redis=Redis(
            host=env.str("REDIS_HOST"),
            password=env.str("REDIS_PASSWORD")
        )
    )
