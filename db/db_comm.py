# from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbComm
from .comms_feed import comms

def db_feed(db: Session):
    new_comm_list = [DbComm(
        content = comm["content"],
        article_id = comm["article_id"],
        user_id = comm["user_id"]
    ) for comm in comms]
    db.query(DbComm).delete()
    db.commit()
    db.add_all(new_comm_list)
    db.commit()
    return db.query(DbComm).all()

