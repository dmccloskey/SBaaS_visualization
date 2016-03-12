from SBaaS_base.postgresql_orm_base import *
class visualization_pipeline(Base):
    __tablename__ = 'visualization_pipeline'
    id = Column(Integer, Sequence('visualization_pipeline_id_seq'), primary_key=True)
    pipeline_id = Column(String(100))
    table_name = Column(String(500))
    data_export_id = Column(String(100))
    container_export_id = Column(String(100))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('pipeline_id','table_name','data_export_id','container_export_id'),
            )

    def __init__(self,data_dict_I):
        self.pipeline_id = data_dict_I['pipeline_id'];
        self.table_name = data_dict_I['table_name'];
        self.data_export_id = data_dict_I['data_export_id'];
        self.container_export_id = data_dict_I['container_export_id'];
        self.used_ = data_dict_I['used_'];
        self.comment_ = data_dict_I['comment_'];

    def __set__row__(self, pipeline_id_I, table_name_I, data_export_id_I,container_export_id_I,used_I,comment_I):
        self.pipeline_id = pipeline_id_I;
        self.table_name = table_name_I;
        self.data_export_id = data_export_id_I;
        self.container_export_id = container_export_id_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {
            'id':self.id,
            'pipeline_id':self.pipeline_id,
            'table_name':self.table_name,
            'data_export_id':self.data_export_id,
            'container_export_id':self.container_export_id,
            'used_':self.used_,
            'comment_':self.comment_
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class visualization_pipeline_description(Base):
    __tablename__ = 'visualization_pipeline_description'
    id = Column(Integer, Sequence('visualization_pipeline_description_id_seq'), primary_key=True)
    pipeline_id = Column(String(100))
    pipeline_section = Column(String(250));
    pipeline_heading = Column(String(250));
    pipeline_paragraph = Column(Text);
    pipeline_media = Column(Text);
    pipeline_href = Column(Text);
    pipeline_tileorder = Column(Text);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('pipeline_id','pipeline_section','pipeline_heading','pipeline_tileorder'),
            )
    
    def __init__(self,data_dict_I):        
        self.comment_=data_dict_I['comment_'];
        self.pipeline_id=data_dict_I['pipeline_id'];
        self.pipeline_section=data_dict_I['pipeline_section'];
        self.pipeline_heading=data_dict_I['pipeline_heading'];
        self.pipeline_paragraph=data_dict_I['pipeline_paragraph'];
        self.pipeline_media=data_dict_I['pipeline_media'];
        self.pipeline_href=data_dict_I['pipeline_href'];
        self.used_=data_dict_I['used_'];
        self.pipeline_tileorder=data_dict_I['pipeline_tileorder'];

    def __set__row__(self, pipeline_id_I, pipeline_section_I, pipeline_heading_I,
                 pipeline_paragraph_I,pipeline_media_I,pipeline_href_I,pipeline_tileorder_I,
                 used_I,comment_I):
        self.pipeline_id = pipeline_id_I;
        self.pipeline_section = pipeline_section_I;
        self.pipeline_heading = pipeline_heading_I;
        self.pipeline_paragraph = pipeline_paragraph_I;
        self.pipeline_media = pipeline_media_I;
        self.pipeline_href = pipeline_href_I;
        self.pipeline_tileorder = pipeline_tileorder_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {
            'id':self.id,
            'pipeline_id':self.pipeline_id,
            'pipeline_section':self.pipeline_section,
            'pipeline_heading':self.pipeline_heading,
            'pipeline_paragraph':self.pipeline_paragraph,
            'pipeline_media':self.pipeline_media,
            'pipeline_href':self.pipeline_href,
            'pipeline_tileorder':self.pipeline_tileorder,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class visualization_pipeline_status(Base):
    __tablename__ = 'visualization_pipeline_status'
    id = Column(Integer, Sequence('visualization_pipeline_status_id_seq'), primary_key=True)
    pipeline_id = Column(String(100))
    pipeline_progress = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('pipeline_id'),
            )
    
    def __init__(self,data_dict_I):       
        self.comment_=data_dict_I['comment_'];
        self.used_=data_dict_I['used_'];
        self.pipeline_id=data_dict_I['pipeline_id'];
        self.pipeline_progress=data_dict_I['pipeline_progress'];

    def __set__row__(self, pipeline_id_I,pipeline_progress_I,used_I,comment_I):
        self.pipeline_id = pipeline_id_I;
        self.pipeline_progress = pipeline_progress_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {
            'id':self.id,
            'pipeline_id':self.pipeline_id,
            'pipeline_progress':self.pipeline_progress,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())