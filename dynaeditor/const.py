# Qt constants
APP_NAME = "DynaEditor"
ORGANISATION_NAME = "dynaeditor"
PREF_WINDOW_POS = "main_window/pos"
PREF_WINDOW_SIZE = "main_window/size"
PREF_VISIBILITY = "visibility"

# argument keys
ATTR_ARG_TYPE = "type_"
ATTR_ARG_ATTR = "attr"
ATTR_ARG_NICE_NAME = "nice_name"
ATTR_ARG_MIN = "min_"
ATTR_ARG_MAX = "max_"
ATTR_ARG_DEFAULT_VALUE = "default_value"
ATTR_ARG_OPTIONS = "options"
ATTR_ARG_FILE_PATH = "file_path"
ATTR_ARG_COLOR = "color"

ARG_KEYS = [ATTR_ARG_TYPE,
            ATTR_ARG_ATTR,
            ATTR_ARG_NICE_NAME,
            ATTR_ARG_MIN,
            ATTR_ARG_MAX,
            ATTR_ARG_DEFAULT_VALUE,
            ATTR_ARG_OPTIONS,
            ATTR_ARG_FILE_PATH,
            ATTR_ARG_COLOR]

# maya argument keys, only needed for unit testing
M_ATTR_ARG_TYPE = "attributeType"
M_ATTR_ARG_ATTR = "shortName"
M_ATTR_ARG_NICE_NAME = "niceName"
M_ATTR_ARG_MIN = "minValue"
M_ATTR_ARG_MAX = "maxValue"
M_ATTR_ARG_DEFAULT_VALUE = "defaultValue"
M_ATTR_ARG_OPTIONS = "enumName"
M_ATTR_ARG_FILE_PATH = "usedAsFilename"
M_ATTR_ARG_COLOR = "usedAsColor"

M_ARG_KEYS = [M_ATTR_ARG_TYPE,
              M_ATTR_ARG_ATTR,
              M_ATTR_ARG_NICE_NAME,
              M_ATTR_ARG_MIN,
              M_ATTR_ARG_MAX,
              M_ATTR_ARG_DEFAULT_VALUE,
              M_ATTR_ARG_OPTIONS,
              M_ATTR_ARG_FILE_PATH,
              M_ATTR_ARG_COLOR]

# attribute types
ATYPE_BOOL = "bool"
ATYPE_ENUM = "enum"
ATYPE_TYPED = "typed"
ATYPE_FLOAT = "float"
ATYPE_FLOAT2 = "float2"
ATYPE_FLOAT3 = "float3"
ATYPE_DOUBLE = "double"
ATYPE_DOUBLE2 = "double2"
ATYPE_DOUBLE3 = "double3"
ATYPE_LONG = "long"
ATYPE_LONG2 = "long2"
ATYPE_LONG3 = "long3"
ATYPE_BYTE = "byte"
ATYPE_SHORT = "short"
