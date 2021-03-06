from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:DD10110dd@127.0.0.1:3306/changzhiServer?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 初始化redis数据库连接
Redis = redis.StrictRedis(host='localhost',port=6379,db=0)