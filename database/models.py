from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from database.configur import PATH
from data.data import timetable
from config import URL_O745B, URL_E742B, URL_R146B

groups = ['o745b', 'e742b', 'r146b']


class Base(DeclarativeBase):    pass


class Day(Base):
    __tablename__ = 'Days_3'
    id_ = Column(Integer, primary_key=True)
    first_string = Column(String)
    second_string = Column(String)
    third_string = Column(String)
    fourth_string = Column(String)
    day_of_week = Column(String)
    group = Column(String)


def write_to_db(string, ind_group):
    groups = ['o745b', 'e742b', 'r146b']
    day_obj = Day()
    string = string.split('\n')
    list_ = []
    for i in range(len(string)):
        list_.append(string[i])
    day_ = list_[0]
    list_ = list_[2:]
    final_list = []
    for i in range(len(list_)):
        if list_[i] == '':
            list_[i] = list_[i].split('  ')
            final_list.extend(list_[i])
        else:
            final_list.append(list_[i])
    engine = create_engine(PATH)
    Session_class = sessionmaker(bind=engine)
    db_session = Session_class()
    count = 0
    for i in range(len(final_list)):
        count += 1
        if final_list[i] != '':
            if count == 1:
                day_obj.first_string = final_list[i]
            elif count == 2:
                day_obj.second_string = final_list[i]
            elif count == 3:
                day_obj.third_string = final_list[i]
            elif count == 4:
                day_obj.fourth_string = final_list[i]
        else:
            count = 0
            day_obj.day_of_week = day_
            day_obj.group = groups[ind_group]
            db_session.add(day_obj)
            db_session.commit()
            del day_obj
            day_obj = Day()

    return day_


def models_main(PATH, number, URL_group, ind_group):
    day_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    groups = ['o745b', 'e742b', 'r146b']
    engine = create_engine(PATH)
    Session_class = sessionmaker(bind=engine)
    db_session = Session_class()
    Base.metadata.create_all(bind=engine)
    db_session.commit()
    '''  запись в бд / 
    for numb in range(7):
        str = timetable(URL_group, numb)
        write_to_db(str, ind_group)
    '''
    number = day_of_week[number]
    gr = groups[ind_group]
    day_list = db_session.query(Day.first_string, Day.second_string, Day.third_string, Day.fourth_string, Day.group).filter_by(group=gr, day_of_week=number).order_by(Day.first_string).distinct().all()
    return_string = number + '\n\n'
    if len(day_list) == 0:
        return_string += 'В этот день расписания нет'
    else:
        for i in range(len(day_list)):
            day_list[i] = list(day_list[i])[:-1]
            for j in range(len(day_list[i])):
                try:
                    if day_list[i][j] != ' ':
                        return_string += day_list[i][j]
                        return_string += '\n'

                except TypeError:
                    continue
            return_string += '\n'
    return return_string


if __name__ == '__main__':
    ind_group = 1
    #print(groups[ind_group])
    models_main(PATH, 2, URL_E742B, ind_group)
    #str = timetable(URL_O745B, 0)
    #write_to_db(str, ind_group)
