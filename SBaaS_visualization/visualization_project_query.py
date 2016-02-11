from .visualization_project_postgresql_models import *

#from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class visualization_project_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for visualization
        '''
        tables_supported = {'visualization_project':visualization_project,
                            'visualization_project_description':visualization_project_description,
                        };
        self.set_supportedTables(tables_supported);

    def drop_visualization(self):
        try:
            visualization_project.__table__.drop(self.engine,True);
            visualization_project_description.__table__.drop(self.engine,True);
            #visualization_project_status.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_visualization(self,project_id_I = None):
        try:
            if project_id_I:
                reset = self.session.query(visualization_project).filter(visualization_project.project_id.like(project_id_I)).delete(synchronize_session=False);
                reset = self.session.query(visualization_project_description).filter(visualization_project_description.project_id.like(project_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(visualization_project).delete(synchronize_session=False);
                reset = self.session.query(visualization_project_description).delete(synchronize_session=False);
                #reset = self.session.query(visualization_project_status).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_visualization(self):
        try:
            visualization_project.__table__.create(self.engine,True);
            visualization_project_description.__table__.create(self.engine,True);
            #visualization_project_status.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def add_visualizationProject(self, data_I):
        '''add rows of visualization_project'''
        if data_I:
            for d in data_I:
                try:
                    data_add = visualization_project(d);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_visualizationProject(self,data_I):
        '''update rows of visualization_project'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(visualization_project).filter(
                            visualization_project.id == d['id']).update(
                            {
                            'project_id':d['project_id'],
                            'pipeline_id':d['pipeline_id'],
                            'analysis_id':d['analysis_id'],
                            'data_export_id':d['data_export_id'],
                            'container_export_id':d['container_export_id'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query data from visualization_project
    def get_project_projectID_visualizationProject(self,project_id_I):
        '''Query rows that are used from the project'''
        try:
            data = self.session.query(visualization_project).filter(
                    visualization_project.project_id.like(project_id_I),
                    visualization_project.used_.is_(True)).order_by(
                    visualization_project.pipeline_id.asc(),
                    visualization_project.data_export_id.asc()).all();
            project_id_O = []
            pipeline_id_O = []
            analysis_id_O = []
            data_export_id_O = []
            container_export_id_O = []
            project_O = {};
            if data: 
                for d in data:
                    project_id_O.append(d.project_id);
                    pipeline_id_O.append(d.pipeline_id);
                    analysis_id_O.append(d.analysis_id);
                    data_export_id_O.append(d.data_export_id);
                    container_export_id_O.append(d.container_export_id);
                project_id_O = list(set(project_id_O))
                pipeline_id_O = list(set(pipeline_id_O))
                analysis_id_O = list(set(analysis_id_O))
                data_export_id_O = list(set(data_export_id_O))
                container_export_id_O = list(set(container_export_id_O))
                project_O={
                        'project_id':project_id_O,
                        'pipeline_id':pipeline_id_O,
                        'analysis_id':analysis_id_O,
                        'data_export_id':data_export_id_O,
                        'container_export_id':container_export_id_O};
                
            return project_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_projectID_visualizationProject(self,project_id_I):
        '''Query rows that are used from the project'''
        try:
            data = self.session.query(visualization_project).filter(
                    visualization_project.project_id.like(project_id_I),
                    visualization_project.used_.is_(True)).order_by(
                    visualization_project.data_export_id.asc(),
                    visualization_project.analysis_id.asc(),
                    visualization_project.container_export_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.__repr__dict__());
                    #data_O.append({'project_id':d.project_id,
                    #    'pipeline_id':d.pipeline_id,
                    #    'analysis_id':d.analysis_id,
                    #    'data_export_id':d.data_export_id,
                    #    'container_export_id':d.container_export_id
                    #});
            return  data_O;
        except SQLAlchemyError as e:
            print(e);

    # query data from visualization_project_description
    def get_rows_projectID_visualizationProjectDescription(self,project_id_I):
        '''Query rows that are used from the project'''
        try:
            data = self.session.query(visualization_project_description).filter(
                    visualization_project_description.project_id.like(project_id_I),
                    visualization_project_description.used_.is_(True)).order_by(
                    visualization_project_description.project_tileorder.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append({'project_id':d.project_id,
                    'project_section':d.project_section,
                    'project_heading':d.project_heading,
                    'project_paragraph':d.project_paragraph,
                    'project_media':d.project_media,
                    'project_href':d.project_href,
                    'project_tileorder':d.project_tileorder,
                    'used_':d.used_,
                    'comment_':d.comment_
                    });
            return  data_O;
        except SQLAlchemyError as e:
            print(e);