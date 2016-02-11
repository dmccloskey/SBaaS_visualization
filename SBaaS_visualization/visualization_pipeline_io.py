# System
import json
from .visualization_pipeline_query import visualization_pipeline_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from ddt_python.ddt_container import ddt_container

class visualization_pipeline_io(visualization_pipeline_query,sbaas_template_io):

    def export_visualizationPipeline_js(self,pipeline_id_I,data_dir_I="tmp"):
        """export visualization_pipeline for visualization"""

        print("exporting visualization_pipeline...")

        # query the pipeline info
        data1_pipeline = {};
        data1_pipeline = self.get_pipeline_pipelineID_visualizationPipeline(pipeline_id_I);
        data1_O = [];
        data1_O = self.get_rows_pipelineID_visualizationPipeline(pipeline_id_I);
        # query the pipeline description
        data2_O = [];
        data2_O = self.get_rows_pipelineID_visualizationPipelineDescription(pipeline_id_I);
        # query user privileges (new table?)
        data1_query_O=[];
        #data1_query_O.g
        # data parameters
        data1_keys = ['table_name','data_export_id','pipeline_id'#,'container_export_id'
                      ];
        data1_nestkeys = ['data_export_id'];
        data1_keymap = {'buttonparameter':'data_export_id','liparameter':'table_name',
                        'buttontext':'data_export_id','litext':'table_name'};
        data2_keys = ['pipeline_id','pipeline_section','pipeline_heading','pipeline_tileorder'
                      ];
        data2_nestkeys = ['pipeline_id'];
        data2_keymap = {'htmlmediasrc':'pipeline_media','htmlmediaalt':'',
                        'htmlmediahref':'pipeline_href','htmlmediaheading':'pipeline_heading',
                        'htmlmediaparagraph':'pipeline_paragraph'};
        # make the data, parameters, and tile2datamap variables:
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};
        tile_cnt = 0;
        # pipeline_description:
        if data2_O:
            for i,d in enumerate(data2_O):
                tileid = "tile" + str(tile_cnt);
                colid = "col" + str(i);
                tileheader = d['pipeline_section'];
                htmlid = "html" + str(tile_cnt);
                tileparameters = {'tileheader':tileheader,'tiletype':'html','tileid':tileid,'rowid':"row1",'colid':colid,
                'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
                htmlparameters={"htmlkeymap":[data2_keymap],
                            'htmltype':'media_01','htmlid':htmlid};
                tileparameters.update(htmlparameters);
                parametersobject_O.append(tileparameters);
                dataobject_O.append({"data":[d],"datakeys":data2_keys,"datanestkeys":data2_nestkeys});
                tile2datamap_O.update({tileid:[tile_cnt]});
                tile_cnt+=1;
        # pipeline:
        if data1_pipeline:
            data1_dict = {};
            for data_export_id in data1_pipeline['data_export_id']:
                if data_export_id is not None:
                    data1_dict[data_export_id]=[];
            for d in data1_O:
                if d['data_export_id'] is not None:
                    data1_dict[d['data_export_id']].append(d);
            data1_keys = list(data1_dict.keys());
            data1_keys.sort();
            col_cnt = 0;
            #for k,v in data1_dict.iteritems():
            for k in data1_keys:
                tileid = "tile" + str(tile_cnt);
                colid = "col" + str(col_cnt);
                tileheader = data1_dict[k][0]['pipeline_id'];
                htmlid = "html" + str(tile_cnt);
                #tileparameters = {'tileheader':tileheader,'tiletype':'html','tileid':tileid,'rowid':"row2",'colid':colid,
                #    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
                #hrefparameters = {"hrefurl":'pipeline.html',"htmlkeymap":[data1_keymap],
                #                'htmltype':'href_01','htmlid':htmlid};
                tileparameters = {
                    'tileheader':tileheader,
                    'tiletype':'html',
                    'tileid':tileid,
                    'rowid':"row2",
                    'colid':colid,
                    'tileclass':"panel panel-default",
                    'rowclass':"row",
                    'colclass':"col-sm-6",
                    "formsubmitbuttonidtext":{'id':'submit1','text':'submit'}};
                hrefparameters = {
                    "hrefurl":'pipeline.html',
                    "htmlkeymap":[data1_keymap],
                    'htmltype':'href_02',
                    'htmlid':htmlid};
                tileparameters.update(hrefparameters);
                parametersobject_O.append(tileparameters);
                dataobject_O.append({"data":data1_dict[k],"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
                tile2datamap_O.update({tileid:[tile_cnt]});
                tile_cnt+=1;
                col_cnt+=1;
                
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
   