from SBaaS_base.postgresql_orm_base import *
import datetime
class visualization_role(Base):
    __tablename__='visualization_role'
    id=Column(Integer, Sequence('visualization_role_id_seq'), primary_key=True)
    role_name=Column(String(100));
    role_password=Column(String(100));
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    expirationDateAndTime=Column(DateTime);
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('role_name'),)
    def __init__(self,data_dict_I):
        self.role_name=data_dict_I['role_name']
        self.role_password=data_dict_I['role_password']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.expirationDateAndTime=data_dict_I['expirationDateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'role_name':self.role_name,
        'role_password':self.role_password,
        'creationDateAndTime':self.creationDateAndTime,
        'expirationDateAndTime':self.expirationDateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_role_attributes(Base):
    __tablename__='visualization_role_attributes'
    id=Column(Integer, Sequence('visualization_role_attributes_id_seq'), primary_key=True)
    role_name=Column(String(100));
    role_attribute=Column(String(100));
    # where attributes consist of the following:
        #SUPERUSER
        #NOSUPERUSER
        #CREATEDB
        #NOCREATEDB
        #CREATEROLE
        #NOCREATEROLE
        #CREATEUSER
        #NOCREATEUSER
        #INHERIT
        #NOINHERIT
        #LOGIN
        #NOLOGIN
        #REPLICATION
        #NOREPLICATION
        #BYPASSRLS
        #NOBYPASSRLS
        #CONNECTION LIMIT connlimit
        #PASSWORD password
        #ENCRYPTED
        #UNENCRYPTED
        #VALID UNTIL 'timestamp'
    attribute_value=Column(String(100));
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('role_name','role_attribute'),)
    def __init__(self,data_dict_I):
        self.role_name=data_dict_I['role_name']
        self.role_attribute=data_dict_I['role_attribute']
        self.attribute_value=data_dict_I['attribute_value']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'role_name':self.role_name,
        'role_attribute':self.role_attribute,
        'attribute_value':self.attribute_value,
        'creationDateAndTime':self.creationDateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
class visualization_role_tablePrivileges(Base):
    __tablename__='visualization_role_tablePrivileges'
    id=Column(Integer, Sequence('visualization_role_tablePrivileges_id_seq'), primary_key=True)
    role_name=Column(String(100));
    table_name=Column(String(100)); #Table or Sequence
    #type_=Column(String(100));
    schema_name=Column(String(100));
    database_name=Column(String(100));
    privilege_type=Column(String(500));
    # where privilege_type can be any of the following:
        #SELECT
        #UPDATE
        #INSERT
        #DELETE
        #TRUNCATE
        #REFERENCES
        #TRIGGER
        #EXECUTE
        #USAGE
        #CREATE
        #CONNECT
        #TEMPORARY
        #ALL PRIVILEGES
    creationDateAndTime=Column(DateTime,default=datetime.datetime.now());
    used_=Column(Boolean);
    comment_=Column(Text);
    __table_args__=(UniqueConstraint('role_name','privilege_type','table_name','schema_name','database_name'),)
    def __init__(self,data_dict_I):
        self.role_name=data_dict_I['role_name']
        self.table_name=data_dict_I['table_name']
        self.schema_name=data_dict_I['schema_name']
        self.database_name=data_dict_I['database_name']
        self.privilege_type=data_dict_I['privilege_type']
        self.creationDateAndTime=data_dict_I['creationDateAndTime']
        self.used_=data_dict_I['used_']
        self.comment_=data_dict_I['comment_']
    def __repr__dict__(self):
        return {
        'role_name':self.role_name,
        'table_name':self.table_name,
        'schema_name':self.schema_name,
        'database_name':self.database_name,
        'privilege_type':self.privilege_type,
        'creationDateAndTime':self.creationDateAndTime,
        'used_':self.used_,
        'comment_':self.comment_,};
    def __repr__json__(self): return json.dumps(self.__repr__dict__())
