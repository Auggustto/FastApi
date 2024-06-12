from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.models.base import Base
from app.models.connection import engine  # Importe o objeto de engine do SQLAlchemy

# Este é o objeto de configuração do Alembic, que fornece acesso aos valores dentro do arquivo .ini em uso.
config = context.config

# Interpretar o arquivo de configuração para Python logging.
# Esta linha configura basicamente os loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importar o objeto MetaData dos modelos
target_metadata = Base.metadata

# Recuperar a URL do banco de dados a partir da variável de ambiente
database_url = os.getenv('DB_URL')

if database_url is None:
    raise EnvironmentError("DATABASE_URL environment variable not set")

# Configurar a URL do SQLAlchemy no objeto de configuração do Alembic
config.set_main_option('sqlalchemy.url', database_url)

def run_migrations_offline() -> None:
    """Executar migrações no modo 'offline'.

    Isso configura o contexto apenas com uma URL e não um Engine, embora um Engine também seja aceitável aqui. 
    Ao pular a criação do Engine, nem precisamos de um DBAPI disponível.

    As chamadas para context.execute() aqui emitem a string dada para a saída do script.
    """
    context.configure(
        url=database_url,  # Use a URL do banco de dados
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executar migrações no modo 'online'.

    Nesse cenário, precisamos criar um Engine e associar uma conexão com o contexto.
    """
    connectable = engine  # Use o objeto de engine do SQLAlchemy

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
