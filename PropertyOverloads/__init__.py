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

class ExamplePropertyOverloads(bpy.types.PropertyGroup):
    # ------------------- ENUM PROPERTIES -------------------
    # str - no enum flag
    enum_prop1: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")])
    enum_prop2: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], default="1")
    enum_prop3: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], options={"HIDDEN"})
    enum_prop4: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], default="1", options={"HIDDEN"})
    enum_prop5: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], options={"HIDDEN", "SKIP_SAVE"})
    enum_prop6: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], default="1", options={"HIDDEN", "SKIP_SAVE"}
    )

    # should be an error - mixing defaults and options from different overloads
    enum_prop_error: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG"}, default="1")
    enum_prop_error: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], default={"1", "2"}
    )  # probably cannot enforce error on this statement?

    # set[str] - enum flag
    enum_prop_flag1: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG"})
    enum_prop_flag2: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG"}, default={"1", "2"}
    )
    enum_prop_flag3: bpy.props.EnumProperty(items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG", "HIDDEN"})
    enum_prop_flag4: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG", "HIDDEN"}, default={"1", "2"}
    )
    enum_prop_flag5: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG", "HIDDEN", "SKIP_SAVE"}
    )
    enum_prop_flag6: bpy.props.EnumProperty(
        items=[("1", "1", ""), ("2", "2", "")], options={"ENUM_FLAG", "HIDDEN", "SKIP_SAVE"}, default={"1", "2"}
    )
    # -------------------

def register():
    bpy.utils.register_class(ExamplePropertyOverloads)

def unregister():
    bpy.utils.unregister_class(ExamplePropertyOverloads)
