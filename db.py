from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
import sqlalchemy

engine = create_engine('postgres://uwtmzhbfvujfkb:d66ebd309832961e7ba01b6eec6f964a28981c543f9f235f7650cb9108df07ac@ec2-54-235-70-127.compute-1.amazonaws.com:5432/dcvoji6oqnp1ab', echo=True)
connection = engine.connect()
metadata = MetaData()
formulario = Table('formulario', metadata,
    Column('id', Integer, primary_key=True),
    Column('post', String),
    Column('tokens', String),
    Column('groups', String),
    Column('notification', String)
)
metadata.create_all(engine)

def insert(groups, usuarios, message):
	ins = formulario.insert().values(post=message, tokens=str(usuarios), groups=groups, notification='Done')
	ins.compile().params
	result = connection.execute(ins)
	ins.bind = engine
	result.inserted_primary_key

def table():
	s = select([formulario])
	connection = engine .connect()
	result = connection.execute("select * from formulario")
	return result