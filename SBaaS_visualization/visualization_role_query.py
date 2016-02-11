from .visualization_role_postgresql_models import *

#from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class visualization_role_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for visualization
        '''
        tables_supported = {
                            'visualization_role':visualization_role,
                            'visualization_role_attributes':visualization_role_attributes,
                            'visualization_role_tablePrivileges':visualization_role_tablePrivileges,
                        };
        self.set_supportedTables(tables_supported);

    def get_row_roleNameAndPassword_visualizationRole(self,role_name_I,password_I):
        '''Query row from visualization_role
        INPUT:
        role_name_I = string, role_name
        password_I = string, password
        OUTPUT:
        data_O = {}
        '''
        #tables_I = ['visualization_role'];
        #query_I = {};
        #query_I['select'] = {'visualization_role':None};
        #query_I['where'] = {'visualization_role':{'role_name':{'value':role_name_I,'operator':'LIKE'},
        #                                        'role_password':{'value':password_I,'operator':'LIKE'}
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
            data = self.session.query(visualization_role).filter(
                    visualization_role.role_name.like(role_name_I),
                    visualization_role.role_password.like(password_I),
                    visualization_role.used_.is_(True)).all();
            if data: 
                for d in data:
                    data_O=d.__repr__dict__();
        except Exception as e:
            print(e);
        return data_O;

    def get_row_roleName_visualizationRole(self,role_name_I):
        '''Query row from visualization_role
        INPUT:
        role_name_I = string, role_name
        OUTPUT:
        data_O = {}
        '''
        #tables_I = ['visualization_role'];
        #query_I = {};
        #query_I['select'] = {'visualization_role':None};
        #query_I['where'] = {'visualization_role':{'role_name':{'value':role_name_I,'operator':'LIKE'},
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
            data = self.session.query(visualization_role).filter(
                    visualization_role.role_name.like(role_name_I),
                    visualization_role.used_.is_(True)).all();
            if data: 
                for d in data:
                    data_O=d.__repr__dict__();
        except Exception as e:
            print(e);
        return data_O;

    def get_rows_roleName_visualizationRoleAttributes(self,role_name_I):
        '''Query rows from visualization_role_attributes
        INPUT:
        role_name_I = string, role_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_role_attributes).filter(
                    visualization_role_attributes.role_name.like(role_name_I),
                    visualization_role_attributes.used_.is_(True)).order_by(
                    visualization_role_attributes.role_attribute.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.__repr__dict__());
        except Exception as e:
            print(e);
        return data_O;

    def get_roleAttributes_roleName_visualizationRoleAttributes(self,role_name_I):
        '''Query rows from visualization_role_tablePrivileges
        INPUT:
        role_name_I = string, role_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_role_attributes).filter(
                    visualization_role_attributes.role_name.like(role_name_I),
                    visualization_role_attributes.used_.is_(True)).order_by(
                    visualization_role_attributes.role_attribute.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.role_attribute);
        except Exception as e:
            print(e);
        return data_O;

    def get_rows_roleName_visualizationRoleTablePrivileges(self,role_name_I):
        '''Query rows from visualization_role_tablePrivileges
        INPUT:
        role_name_I = string, role_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_role_tablePrivileges).filter(
                    visualization_role_tablePrivileges.role_name.like(role_name_I),
                    visualization_role_tablePrivileges.used_.is_(True)).order_by(
                    visualization_role_tablePrivileges.privilege_type.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.__repr__dict__());
        except Exception as e:
            print(e);
        return data_O;

    def get_rolePrivileges_roleName_visualizationRolePrivileges(self,role_name_I):
        '''Query rows from visualization_role_tablePrivileges
        INPUT:
        role_name_I = string, role_name
        OUTPUT:
        data_O = {}
        '''
        data_O = [];
        try:
            data = self.session.query(visualization_role_tablePrivileges).filter(
                    visualization_role_tablePrivileges.role_name.like(role_name_I),
                    visualization_role_tablePrivileges.used_.is_(True)).order_by(
                    visualization_role_tablePrivileges.privilege_type.asc()).all();
            data_O = [];
            if data: 
                for d in data:
                    data_O.append(d.privilege_type);
        except Exception as e:
            print(e);
        return data_O;

   