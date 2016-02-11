import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_visualization')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')

from SBaaS_visualization.visualization_execute import visualization_execute
vis01 = visualization_execute(session,engine,pg_settings.datadir_settings);
#vis01.drop_visualization();
vis01.initialize_visualization();
vis01.reset_visualization();
# upload the projects
vis01.import_visualizationProject_add('data/tests/analysis_visualization/150905_ALEsKOs01_project01.csv');
vis01.import_visualizationProject_add('data/tests/analysis_visualization/150905_chemoCLim01_project01.csv');
# export the projects
vis01.export_visualizationProject_csv(project_id_I='ALEsKOs01',filename_O='data/tests/analysis_visualization/project01.csv');
vis01.export_visualizationProject_csv(project_id_I='chemoCLim01',filename_O='data/tests/analysis_visualization/project02.csv');