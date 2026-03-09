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

from . import operators
from .operators_to_import import ExampleImportedOperator, ExampleImportedOperator1, ExampleImportedOperator2, ExampleImportedOperator3
from bpy.utils import register_class, unregister_class


class ExampleObjectOperator(bpy.types.Operator):
    bl_idname = "object.example_operator"
    bl_label = "Example Object Operator"
    bl_description = "This is an example object operator"

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


class ExampleFooOperator(bpy.types.Operator):
    bl_idname = "foo.example_operator"
    bl_label = "Example Foo Operator"
    bl_description = "This is an example foo operator"

    string_property: bpy.props.StringProperty(name="String Property", default="Hello World")
    int_property: bpy.props.IntProperty(name="Integer Property", default=42)

    def execute(self, context):
        self.report(
            {'INFO'}, f"Example Foo Operator executed with string: {self.string_property}, int: {self.int_property}"
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        self.report(
            {'INFO'}, f"Example Foo Operator invoked with string: {self.string_property}, int: {self.int_property}"
        )
        return self.execute(context)

classes = (
    ExampleImportedOperator1,
    operators.ExampleExtensionOperator2,
    ExampleImportedOperator3,
)

classes_list = [
    operators.ExampleExtensionOperator1,
    ExampleImportedOperator2,
    operators.ExampleExtensionOperator3,
]

def register():
    bpy.utils.register_class(ExampleObjectOperator)
    bpy.utils.register_class(ExampleFooOperator)
    bpy.utils.register_class(ExampleImportedOperator)
    bpy.utils.register_class(operators.ExampleExtensionOperator)

    for cls in classes:
        register_class(cls)
    for cls in classes_list:
        register_class(cls)

    # OK
    bpy.ops.object.example_operator()
    bpy.ops.foo.example_operator()
    bpy.ops.object.example_operator("INVOKE_DEFAULT")
    bpy.ops.foo.example_operator("INVOKE_DEFAULT")
    bpy.ops.object.example_operator("EXEC_DEFAULT")
    bpy.ops.foo.example_operator("EXEC_DEFAULT")
    bpy.ops.object.example_operator("INVOKE_DEFAULT", string_property="Custom String", int_property=99)
    bpy.ops.foo.example_operator("INVOKE_DEFAULT", string_property="Custom String", int_property=99)
    bpy.ops.object.example_operator("EXEC_DEFAULT", string_property="Custom String", int_property=99)
    bpy.ops.foo.example_operator("EXEC_DEFAULT", string_property="Custom String", int_property=99)

    bpy.ops.my_extension.example_operator("EXEC_DEFAULT")
    bpy.ops.my_extension.example_operator1("EXEC_DEFAULT")
    bpy.ops.my_extension.example_operator2("EXEC_DEFAULT")
    bpy.ops.my_extension_unique.example_operator3("EXEC_DEFAULT")
    bpy.ops.operators_to_import.example_operator("EXEC_DEFAULT")
    bpy.ops.operators_to_import.example_operator1("EXEC_DEFAULT")
    bpy.ops.operators_to_import.example_operator2("EXEC_DEFAULT")
    bpy.ops.operators_to_import_unique.example_operator3("EXEC_DEFAULT")

    # ERRORS
    bpy.ops.nonexistent_module.example_operator("INVOKE_DEFAULT") # Try to call operator from nonexistent module
    bpy.ops.wm.example_operator("INVOKE_DEFAULT") # Try to call operator from nonexistent module
    bpy.ops.object.nonexistent_operator("INVOKE_DEFAULT") # Try to call nonexistent operator

    bpy.ops.my_extension.example_operator() # Call operator without execution context
    bpy.ops.object.example_operator("INVALID_CONTEXT") # Execution context only accepts its enum values
    bpy.ops.object.example_operator("INVOKE_DEFAULT", string_property="Custom String", float_property=99.0) # Nonexistent property


def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
    for cls in reversed(classes_list):
        unregister_class(cls)

    bpy.utils.unregister_class(ExampleObjectOperator)
    bpy.utils.unregister_class(ExampleFooOperator)
    bpy.utils.unregister_class(ExampleImportedOperator)
    bpy.utils.unregister_class(operators.ExampleExtensionOperator)

