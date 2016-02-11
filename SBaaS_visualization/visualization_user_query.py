from .visualization_user_postgresql_models import *

#from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class visualization_user_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for visualization
        '''
        tables_supported = {
                            'visualization_user':visualization_user,
                            'visualization_user_login':visualization_user_login,
                            'visualization_user_password':visualization_user_password,
                            'visualization_user_contact':visualization_user_contact,
                            'visualization_user_projects':visualization_user_projects,
                            'visualization_user_pipelines':visualization_user_pipelines,
                        };
        self.set_supportedTables(tables_supported);

    def get_row_userNameAndPassword_visualizationUser(self,user_name_I,password_I):
        '''Query row from visualization_user and user_password from visualization_user_password
        INPUT:
        user_name_I = string, user_name
        password_I = string, password
        OUTPUT:
        data_O = {}
        '''
        #tables_I = ['visualization_user'];
        #query_I = {};
        #query_I['select'] = {'visualization_user':None};
        #query_I['where'] = {'visualization_user':{'user_name':{'value':user_name_I,'operator':'LIKE'},
        #                                        'user_password':{'value':password_I,'operator':'LIKE'}
        #                                        },
        #                  };
        data_O = {};
        try:
            #table_model = self.convert_tableStringList2SqlalchemyModelDict(tables_I);
            #queryselect = sbaas_base_query_select(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            #query = queryselect.make_queryFromString(table_model,query_I);
            #data_O = queryselect.get_rows_sqlalchemyModel(
            #    query_I=query,
            #    output_O=output_O,
            #    dictColumn_I=dictColumn_I);
            data = self.session.query(visualization_user,
                    visualization_user_password.user_password).filter(
                    visualization_user.user_name.like(user_name_I),
                    visualization_user.user_name.like(visualization_user_password.user_name),
                    visualization_user_password.user_password.like(password_I),
                    visualization_user_password.isActive.is_(True),
                    visualization_user.used_.is_(True)).all();
            if data: 
                for d in data:
                    data_O=d.visualization_user.__repr__dict__();
                    data_O['user_password']=d.user_password;
        except Exception as e:
            print(e);
        return data_O;

    def get_rows_userName_visualizationUserProjects(self,user_name_I):
        '''Query rows from visualization_user_projects
        INPUT:
        user_name_I = string, user_name
        OUTPUT:
        data_O = {}
        '''
        data_O = {};
        try:
            data = self.session.query(visualization_user_projects).filter(
                    visualization_user_projects.user_name.like(user_name_I),
                    visualization_user_projects.used_.is_(True)).order_by(
                    visualization_user_projects.project_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append=d.__repr__dict__();
        except Exception as e:
            print(e);
        return data_O;
    def get_projectIDs_userName_visualizationUserProjects(self,user_name_I):
        '''Query rows from visualization_user_projects
        INPUT:
        user_name_I = string, user_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_user_projects).filter(
                    visualization_user_projects.user_name.like(user_name_I),
                    visualization_user_projects.used_.is_(True)).order_by(
                    visualization_user_projects.project_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.project_id);
        except Exception as e:
            print(e);
        return data_O;

    def get_rows_userName_visualizationUserPipelines(self,user_name_I):
        '''Query rows from visualization_user_pipelines
        INPUT:
        user_name_I = string, user_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_user_pipelines).filter(
                    visualization_user_pipelines.user_name.like(user_name_I),
                    visualization_user_pipelines.used_.is_(True)).order_by(
                    visualization_user_pipelines.pipeline_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.__repr__dict__());
        except Exception as e:
            print(e);
        return data_O;

    def get_pipelineIDs_userName_visualizationUserPipelines(self,user_name_I):
        '''Query rows from visualization_user_pipelines
        INPUT:
        user_name_I = string, user_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_user_pipelines).filter(
                    visualization_user_pipelines.user_name.like(user_name_I),
                    visualization_user_pipelines.used_.is_(True)).order_by(
                    visualization_user_pipelines.pipeline_id.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.pipeline_id);
        except Exception as e:
            print(e);
        return data_O;

   