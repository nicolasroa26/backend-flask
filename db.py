from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
import sqlalchemy

engine = create_engine('postgres://uxeczfkzzczdvz:27380b4ecab444300530ce43b70d26820f6e9232c6dbafe74225314caf570e8b@ec2-107-20-249-68.compute-1.amazonaws.com:5432/d34655kqicm837', echo=True)
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