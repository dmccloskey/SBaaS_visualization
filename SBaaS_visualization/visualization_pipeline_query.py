from .visualization_pipeline_postgresql_models import *

#from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class visualization_pipeline_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for visualization
        '''
        tables_supported = {
                            'visualization_pipeline':visualization_pipeline,
                            'visualization_pipeline_description':visualization_pipeline_description,
                            'visualization_pipeline_status':visualization_pipeline_status,
                        };
        self.set_supportedTables(tables_supported);
            
    # query data from visualization_pipeline
    def get_pipeline_pipelineID_visualizationPipeline(self,pipeline_id_I):
        '''Query rows that are used from the pipeline'''
        try:
            data = self.session.query(visualization_pipeline).filter(
                    visualization_pipeline.pipeline_id.like(pipeline_id_I),
                    visualization_pipeline.used_.is_(True)).order_by(
                    visualization_pipeline.pipeline_id.asc(),
                    visualization_pipeline.data_export_id.asc()).all();
            pipeline_id_O = []
            table_name_O = []
            data_export_id_O = []
            container_export_id_O = []
            pipeline_O = {};
            if data: 
                for d in data:
                    pipeline_id_O.append(d.pipeline_id);
                    table_name_O.append(d.table_name);
                    data_export_id_O.append(d.data_export_id);
                    container_export_id_O.append(d.container_export_id);
                pipeline_id_O = list(set(pipeline_id_O))
                table_name_O = list(set(table_name_O))
                data_export_id_O = list(set(data_export_id_O))
                container_export_id_O = list(set(container_export_id_O))
                pipeline_O={
                        'pipeline_id':pipeline_id_O,
                        'table_name':table_name_O,
                        'data_export_id':data_export_id_O,
                        'container_export_id':container_export_id_O};
                
            return pipeline_O;
        except SQLAlchemyError as e:
            print(e);
            self.session.rollback()
    def get_rows_pipelineID_visualizationPipeline(self,pipeline_id_I):
        '''Query rows that are used from the pipeline'''
        try:
            data = self.session.query(visualization_pipeline).filter(
                    visualization_pipeline.pipeline_id.like(pipeline_id_I),
                    visualization_pipeline.used_.is_(True)).order_by(
                    visualization_pipeline.data_export_id.asc(),
                    visualization_pipeline.table_name.asc(),
                    visualization_pipeline.container_export_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.__repr__dict__());
            return  data_O;
        except SQLAlchemyError as e:
            print(e);
            self.session.rollback()

    # query data from visualization_pipeline_description
    def get_rows_pipelineID_visualizationPipelineDescription(self,pipeline_id_I):
        '''Query rows that are used from the pipeline'''
        try:
            data = self.session.query(visualization_pipeline_description).filter(
                    visualization_pipeline_description.pipeline_id.like(pipeline_id_I),
                    visualization_pipeline_description.used_.is_(True)).order_by(
                    visualization_pipeline_description.pipeline_tileorder.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append({'pipeline_id':d.pipeline_id,
                    'pipeline_section':d.pipeline_section,
                    'pipeline_heading':d.pipeline_heading,
                    'pipeline_paragraph':d.pipeline_paragraph,
                    'pipeline_media':d.pipeline_media,
                    'pipeline_href':d.pipeline_href,
                    'pipeline_tileorder':d.pipeline_tileorder,
                    'used_':d.used_,
                    'comment_':d.comment_
                    });
            return  data_O;
        except SQLAlchemyError as e:
            print(e);
            self.session.rollback()