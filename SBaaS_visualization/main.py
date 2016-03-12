import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_visualization')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

from SBaaS_visualization.visualization_project_execute import visualization_project_execute
visproj01 = visualization_project_execute(session,engine,pg_settings.datadir_settings);
visproj01.initialize_supportedTables();
visproj01.initialize_tables();
#visproj01.reset_visualization('ALEsKOs01');
# upload the projects
#visproj01.import_rows_table_add_csv(
#    table_I='visualization_project',
#    filename_I='data/tests/analysis_visualization/150905_ALEsKOs01_project01.csv');
#visproj01.import_rows_table_update_csv(
#    table_I='visualization_project',
#    filename_I='data/tests/analysis_visualization/150905_ALEsKOs01_projectUpdate01.csv');
#visproj01.import_rows_table_reset_csv(
#    table_I='visualization_project',
#    filename_I='data/tests/analysis_visualization/150905_ALEsKOs01_projectUpdate01.csv');
## export the projects
#visproj01.export_rows_tables_table_js(['visualization_project'],{'select':{'visualization_project':None}},data_dir_I='tmp');
#visproj01.export_visualizationProject_csv(project_id_I='ALEsKOs01',filename_O='data/tests/analysis_visualization/project01.csv');
visproj01.export_visualizationProject_js(project_id_I='ALEsKOs01');

#from SBaaS_visualization.visualization_pipeline_execute import visualization_pipeline_execute
#vispipe01 = visualization_pipeline_execute(session,engine,pg_settings.datadir_settings);
#vispipe01.initialize_supportedTables();
#vispipe01.initialize_tables();
#vispipe01.import_rows_table_add_csv(
#    table_I='visualization_pipeline',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160106_Visualization_pipeline02.csv'
#    );

#from SBaaS_visualization.visualization_user_execute import visualization_user_execute
#visuser01 = visualization_user_execute(session,engine,pg_settings.datadir_settings);
#visuser01.initialize_supportedTables();
##visuser01.drop_tables();
#visuser01.initialize_tables();
#visuser01.import_rows_table_add_csv(
#    table_I='visualization_user',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160106_Visualization_users02.csv'
#    );
#visuser01.import_rows_table_add_csv(
#    table_I='visualization_user_projects',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160106_Visualization_users_projects01.csv'
#    );
#visuser01.import_rows_table_add_csv(
#    table_I='visualization_user_pipelines',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160106_Visualization_users_pipelines01.csv'
#    );
#visuser01.import_rows_table_add_csv(
#    table_I='visualization_user_password',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160106_Visualization_users_password01.csv'
#    );

#from SBaaS_visualization.visualization_role_execute import visualization_role_execute
#visrole01 = visualization_role_execute(session,engine,pg_settings.datadir_settings);
#visrole01.initialize_supportedTables();
#visrole01.initialize_tables();
#visrole01.import_rows_table_add_csv(
#    table_I='visualization_role_tablePrivileges',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160201_Visualization_role_tablePrivileges01.csv'
#    );
#visrole01.import_rows_table_add_csv(
#    table_I='visualization_role_tablePrivileges',
#    filename_I=pg_settings.datadir_settings['workspace_data'] + '/_input/160201_Visualization_role_tablePrivileges02.csv'
#    );

