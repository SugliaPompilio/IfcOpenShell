import os
from bpy.types import Panel
from blenderbim.bim.ifc import IfcStore


class BIM_PT_project(Panel):
    bl_label = "IFC Project"
    bl_idname = "BIM_PT_project"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

    def draw(self, context):
        self.layout.use_property_decorate = False
        self.layout.use_property_split = True
        props = context.scene.BIMProperties
        self.file = IfcStore.get_file()
        if self.file or props.ifc_file:
            self.draw_project_ui(context)
        else:
            self.draw_create_project_ui(context)

    def draw_project_ui(self, context):
        props = context.scene.BIMProperties
        row = self.layout.row(align=True)
        row.label(text="IFC Filename", icon="FILE")
        row.label(text=os.path.basename(props.ifc_file) or "No File Found")

        if IfcStore.get_file():
            row = self.layout.row(align=True)
            row.label(text="IFC Schema", icon="FILE_CACHE")
            row.label(text=IfcStore.get_file().schema)
        else:
            row = self.layout.row(align=True)
            row.label(text="File Not Loaded", icon="ERROR")

        row = self.layout.row(align=True)
        row.prop(props, "ifc_file", text="")
        row.operator("bim.reload_ifc_file", icon="FILE_REFRESH", text="")
        row.operator("bim.select_ifc_file", icon="FILE_FOLDER", text="")

        row = self.layout.row(align=True)
        row.prop(props, "schema_dir")
        row.operator("bim.select_schema_dir", icon="FILE_FOLDER", text="")

        row = self.layout.row(align=True)
        row.prop(props, "data_dir")
        row.operator("bim.select_data_dir", icon="FILE_FOLDER", text="")

    def draw_create_project_ui(self, context):
        props = context.scene.BIMProperties
        row = self.layout.row()
        row.prop(props, "export_schema")
        row = self.layout.row()
        row.prop(context.scene.unit_settings, "system")
        row = self.layout.row()
        row.prop(context.scene.unit_settings, "length_unit")
        row = self.layout.row()
        row.prop(props, "area_unit", text="Area Unit")
        row = self.layout.row()
        row.prop(props, "volume_unit", text="Volume Unit")
        row = self.layout.row()
        row.operator("bim.create_project")
