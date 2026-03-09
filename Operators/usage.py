import bpy

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
bpy.ops.operators_to_import.example_operator("EXEC_DEFAULT")

# ERRORS
bpy.ops.nonexistent_module.example_operator("INVOKE_DEFAULT")  # Try to call operator from nonexistent module
bpy.ops.wm.example_operator("INVOKE_DEFAULT")  # Try to call operator from nonexistent module
bpy.ops.object.nonexistent_operator("INVOKE_DEFAULT")  # Try to call nonexistent operator

bpy.ops.my_extension.example_operator()  # Call operator without execution context
bpy.ops.object.example_operator("INVALID_CONTEXT")  # Execution context only accepts its enum values
bpy.ops.object.example_operator("INVOKE_DEFAULT", string_property="Custom String", float_property=99.0)  # Nonexistent property