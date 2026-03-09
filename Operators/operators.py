# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy


class ExampleExtensionOperator(bpy.types.Operator):
    bl_idname = "my_extension.example_operator"
    bl_label = "Example Extension Operator"
    bl_description = "This is an example extension operator"

    string_property: bpy.props.StringProperty(name="String Property", default="Hello World")
    int_property: bpy.props.IntProperty(name="Integer Property", default=42)

    def execute(self, context):
        self.report(
            {'INFO'}, f"Example Object Operator executed with string: {self.string_property}, int: {self.int_property}"
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        self.report(
            {'INFO'}, f"Example Object Operator invoked with string: {self.string_property}, int: {self.int_property}"
        )
        return self.execute(context)


class ExampleExtensionOperator1(bpy.types.Operator):
    bl_idname = "my_extension.example_operator1"
    bl_label = "Example Extension Operator"
    bl_description = "This is an example extension operator"

    string_property: bpy.props.StringProperty(name="String Property", default="Hello World")
    int_property: bpy.props.IntProperty(name="Integer Property", default=42)

    def execute(self, context):
        self.report(
            {'INFO'}, f"Example Object Operator executed with string: {self.string_property}, int: {self.int_property}"
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        self.report(
            {'INFO'}, f"Example Object Operator invoked with string: {self.string_property}, int: {self.int_property}"
        )
        return self.execute(context)


class ExampleExtensionOperator2(bpy.types.Operator):
    bl_idname = "my_extension.example_operator2"
    bl_label = "Example Extension Operator"
    bl_description = "This is an example extension operator"

    string_property: bpy.props.StringProperty(name="String Property", default="Hello World")
    int_property: bpy.props.IntProperty(name="Integer Property", default=42)

    def execute(self, context):
        self.report(
            {'INFO'}, f"Example Object Operator executed with string: {self.string_property}, int: {self.int_property}"
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        self.report(
            {'INFO'}, f"Example Object Operator invoked with string: {self.string_property}, int: {self.int_property}"
        )
        return self.execute(context)


class ExampleExtensionOperator3(bpy.types.Operator):
    bl_idname = "my_extension_unique.example_operator3"
    bl_label = "Example Extension Operator"
    bl_description = "This is an example extension operator"

    string_property: bpy.props.StringProperty(name="String Property", default="Hello World")
    int_property: bpy.props.IntProperty(name="Integer Property", default=42)

    def execute(self, context):
        self.report(
            {'INFO'}, f"Example Object Operator executed with string: {self.string_property}, int: {self.int_property}"
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        self.report(
            {'INFO'}, f"Example Object Operator invoked with string: {self.string_property}, int: {self.int_property}"
        )
        return self.execute(context)