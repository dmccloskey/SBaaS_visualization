# System
import json
from .visualization_role_query import visualization_role_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container

class visualization_role_io(visualization_role_query,sbaas_template_io):

    def import_visualizationUser_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_visualizationUser(data.data);
        data.clear_data();

    def import_visualizationUser_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_visualizationUser(data.data);
        data.clear_data();
