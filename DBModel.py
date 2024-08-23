from http import HTTPStatus
from matplotlib.font_manager import json_dump
from sqlalchemy import PrimaryKeyConstraint, Sequence, String, Integer, ForeignKey, ExceptionContext
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped, mapped_column, relationship 

import json
from typing import List, Optional
import datetime


class Base(DeclarativeBase):
    pass

class WaterCans(Base):
    __tablename__ = "water_cans"
    id: Mapped[int] = mapped_column(Sequence('id'), primary_key=True)
    added_date: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"WaterCan(id={self.id}, added_date={self.added_date})"

engine = create_engine("sqlite:///chronotrack.db", echo=True)
Base.metadata.create_all(engine)

# database model is written here, the following functions will be for database maintanence.
# business operations will be setup in controller, but could be written here first and moved later.

## ADD OPERATIONS
def add_sample_data():
    item_1 = WaterCans(added_date = "22nd Aug")
    item_2 = WaterCans(added_date = "22nd Aug")
    item_3 = WaterCans(added_date = "23nd Aug")
    item_4 = WaterCans(added_date = "23nd Aug")
    item_5 = WaterCans(added_date = "25nd Aug")

    with Session(engine) as session:
        session.add_all([item_1, item_2, item_3, item_4, item_5])
        try:
            session.commit()
            return 200
        except Exception as e:
            print(e)
            return 500

def add_watercan(added_date):
    item = WaterCans(added_date = added_date)
    with Session(engine) as session:
        session.add(item)
        try:
            session.commit()
            return 200
        except Exception as e:
            print(e)
            return 500


## EDIT OPERATIONS
def edit_watercan(search_id, new_added_date):
    with Session(engine) as session:
        item_to_update = session.query(WaterCans).filter_by(id=search_id).first()
        if item_to_update: 
            try:
                item_to_update.added_date = new_added_date
                session.commit()
                print(f'updated {item_to_update.id} with new value of {item_to_update.added_date}')
                return 200
            except Exception as e:
                print (e)
                return 500

def edit_multiple_watercans(search_ids, updated_added_dates):
    if len(search_ids) == len(updated_added_dates): 
        with Session(engine) as session:
            for search_id, updated_added_date in zip(search_ids, updated_added_dates):
                item_to_update = session.query(WaterCans).filter_by(id=search_id).first() 
                if item_to_update:
                        try:
                            item_to_update.added_date = updated_added_date
                            session.commit()
                            print(f'updated {item_to_update.id} with new value of {item_to_update.added_date}')
                        except Exception as e:
                            print(e)
                            return 500


    else:
        print(f'{len(search_id)} was given, but there were {len(updated_added_dates)} values, this cannot happen.')

## FETCH OPERATIONS
def get_all_watercans():
    try:
        with Session(engine) as session:
            items = session.query(WaterCans)
            return_json = {}

            for item in items:
                return_json[item.id] = item.added_date

            return return_json
    except Exception as e:
        print (e)
        return HTTPStatus()


if __name__ == "__main__":
    # add_sample_data()
    # add_watercan('Testing')
    # edit_watercan(10, "25th Aug")
    # edit_multiple_watercans(search_ids = [1,2,3], updated_added_dates = ['23rd Aug','24th Aug','25th Aug'])

    watercans = get_all_watercans()
    print(watercans)
    pass