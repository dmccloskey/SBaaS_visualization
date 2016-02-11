from SBaaS_base.postgresql_orm_base import *
import datetime
#class visualization_user(Base):
#    __tablename__ = 'visualization_user'
#    id = Column(Integer, Sequence('visualization_user_id_seq'), primary_key=True)
#    user_name = Column(String(100));
#    #user_attributes = Column(Postgresql.JSON())
#    #user_privileges = Column(Postgresql.JSON())
#    user_password = Column(String(100));
#    user_role = Column(String(100));
#    user_host = Column(String(100));
#    user_database = Column(String(100));
#    user_schema = Column(String(100));
#    used_ = Column(Boolean);
#    comment_ = Column(Text);

#    __table_args__ = (UniqueConstraint('user_name'),
#            )

#    def __init__(self,data_dict_I):
#        self.user_name=data_dict_I['user_name'];
#        self.user_password=data_dict_I['user_password'];
#        self.user_role=data_dict_I['user_role'];
#        self.user_host=data_dict_I['user_host'];
#        self.user_database=data_dict_I['user_database'];
#        self.user_schema=data_dict_I['user_schema'];
#        self.used_=data_dict_I['used_'];
#        self.comment_=data_dict_I['comment_'];

#    def __set__row__(self,
#                    user_name_I,
#                    user_password_I,
#                    user_role_I,
#                    user_host_I,
#                    user_database_I,
#                    user_schema_I,
#                    used__I,
#                    comment__I):
#        self.user_name=user_name_I
#        self.user_password=user_password_I
#        self.user_role=user_role_I
#        self.user_host=user_host_I
#        self.user_database=user_database_I
#        self.user_schema=user_schema_I
#        self.used_=used__I
#        self.comment_=comment__I

#    def __repr__dict__(self):
#        return {'id':self.id,
#                'user_name':self.user_name,
#                'user_password':self.user_password,
#                'user_role':self.user_role,
#                'user_host':self.user_host,
#                'user_database':self.user_database,
#                'user_schema':self.user_schema,
#                'used_':self.used_,
#                'comment_':self.comment_}
    
#    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_user_projects(Base):
    __tablename__ = 'visualization_user_projects'
    id = Column(Integer, Sequence('visualization_user_projects_id_seq'), primary_key=True)
    project_id = Column(String(100))
    user_name = Column(String(100));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('user_name','project_id'),
            )

    def __init__(self,data_dict_I):
        self.project_id=data_dict_I['project_id'];
        self.user_name=data_dict_I['user_name'];
        self.used_=data_dict_I['used_'];
        self.comment_=data_dict_I['comment_'];

    def __set__row__(self,
                    project_id_I,
                    user_name_I,
                    used__I,
                    comment__I):
        self.project_id=project_id_I
        self.user_name=user_name_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'project_id':self.project_id,
                'user_name':self.user_name,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class visualization_user_pipelines(Base):
    __tablename__ = 'visualization_user_pipelines'
    id = Column(Integer, Sequence('visualization_user_pipelines_id_seq'), primary_key=True)
    pipeline_id = Column(String(100))
    user_name = Column(String(100));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('user_name','pipeline_id'),
            )

    def __init__(self,data_dict_I):
        self.pipeline_id=data_dict_I['pipeline_id'];
        self.user_name=data_dict_I['user_name'];
        self.used_=data_dict_I['used_'];
        self.comment_=data_dict_I['comment_'];

    def __set__row__(self,
                    pipeline_id_I,
                    user_name_I,
                    used__I,
                    comment__I):
        self.pipeline_id=pipeline_id_I
        self.user_name=user_name_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'pipeline_id':self.pipeline_id,
                'user_name':self.user_name,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class visualization_user(Base):
    __tablename__='visualization_user'
    id=Column(Integer, Sequence('visualization_user_id_seq'), primary_key=True)
    user_name=Column(String(100));
    user_firstName=Column(String(100));
    user_middleName=Column(String(100));
    user_lastName=Column(String(100));
    user_dateOfBirth=Column(DateTime);
    user_sex=Column(String(10));
    isActive=Column(Boolean);
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    expirationDateAndTime=Column(DateTime);
    role_name=Column(String(100));
    user_database=Column(String(100));
    user_host=Column(String(100));
    user_schema=Column(String(100));
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('user_name'),)
    def __init__(self,data_dict_I):
        self.user_name=data_dict_I['user_name']
        self.user_firstName=data_dict_I['user_firstName']
        self.user_middleName=data_dict_I['user_middleName']
        self.user_lastName=data_dict_I['user_lastName']
        self.user_dateOfBirth=data_dict_I['user_dateOfBirth']
        self.user_sex=data_dict_I['user_sex']
        self.isActive=data_dict_I['isActive']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.expirationDateAndTime=data_dict_I['expirationDateAndTime']
        self.role_name=data_dict_I['role_name']
        self.user_database=data_dict_I['user_database']
        self.user_host=data_dict_I['user_host']
        self.user_schema=data_dict_I['user_schema']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'user_name':self.user_name,
        'user_firstName':self.user_firstName,
        'user_middleName':self.user_middleName,
        'user_lastName':self.user_lastName,
        'user_dateOfBirth':self.user_dateOfBirth,
        'user_sex':self.user_sex,
        'isActive':self.isActive,
        'creationDateAndTime':self.creationDateAndTime,
        'expirationDateAndTime':self.expirationDateAndTime,
        'role_name':self.role_name,
        'user_database':self.user_database,
        'user_host':self.user_host,
        'user_schema':self.user_schema,
        'used_':self.used_,
        'comment_':self.comment_,
        };
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_user_login(Base):
    __tablename__='visualization_user_login'
    id=Column(Integer, Sequence('visualization_user_login_id_seq'), primary_key=True)
    user_name=Column(String(100));
    login_attempt=Column(String(100));
    ip_address=Column(String(100));
    browser_type=Column(String(100));
    login_success=Column(Boolean)
    login_dateAndTime=Column(DateTime,default=datetime.datetime.now());
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('user_name','login_dateAndTime'),)
    def __init__(self,data_dict_I):
        self.user_name=data_dict_I['user_name']
        self.login_attempt=data_dict_I['login_attempt']
        self.ip_address=data_dict_I['ip_address']
        self.browser_type=data_dict_I['browser_type']
        self.login_success=data_dict_I['login_success']
        self.login_dateAndTime=data_dict_I['login_dateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'user_name':self.user_name,
        'login_attempt':self.login_attempt,
        'ip_address':self.ip_address,
        'browser_type':self.browser_type,
        'login_success':self.login_success,
        'login_dateAndTime':self.login_dateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_user_password(Base):
    __tablename__='visualization_user_password'
    id=Column(Integer, Sequence('visualization_user_password_id_seq'), primary_key=True)
    user_name=Column(String(100));
    user_password=Column(String(100));
    isActive=Column(Boolean)
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    expirationDateAndTime=Column(DateTime);
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('user_name','user_password'),)
    def __init__(self,data_dict_I):
        self.user_name=data_dict_I['user_name']
        self.user_password=data_dict_I['user_password']
        self.isActive=data_dict_I['isActive']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.expirationDateAndTime=data_dict_I['expirationDateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'user_name':self.user_name,
        'user_password':self.user_password,
        'isActive':self.isActive,
        'creationDateAndTime':self.creationDateAndTime,
        'expirationDateAndTime':self.expirationDateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_user_contact(Base):
    __tablename__='visualization_user_contact'
    id=Column(Integer, Sequence('visualization_user_contact_id_seq'), primary_key=True)
    user_name=Column(String(100));
    user_contact=Column(postgresql.JSON);
    contact_description=Column(String(100));
    contact_type=Column(String(100));
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    modifiedDateAndTime=Column(DateTime,default=datetime.datetime.now());
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('user_name','user_contact'),)
    def __init__(self,data_dict_I):
        self.user_name=data_dict_I['user_name']
        self.user_contact=data_dict_I['user_contact']
        self.contact_description=data_dict_I['contact_description']
        self.contact_type=data_dict_I['contact_type']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.modifiedDateAndTime=data_dict_I['modifiedDateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'user_name':self.user_name,
        'user_contact':self.user_contact,
        'contact_description':self.contact_description,
        'contact_type':self.contact_type,
        'creationDateAndTime':self.creationDateAndTime,
        'modifiedDateAndTime':self.modifiedDateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
