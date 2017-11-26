# Qt constants
APP_NAME = "DynaEditor"
ORGANISATION_NAME = "dynaeditor"
PREF_WINDOW_POS = "main_window/pos"
PREF_WINDOW_SIZE = "main_window/size"
PREF_VISIBILITY = "visibility"
PREF_AFFECT_CHILDREN = "affectChildren"
PREF_RESTRICT_TO_TYPE = "restrictToType"

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

# default hidden items
DEFAULT_HIDDEN_ITEMS = {'intermediateObject': 0,
                        'smoothOsdColorizePatches': 0,
                        'numTriangles': 0,
                        'ghostColorPost': 0,
                        'initialSampleRate': 0,
                        'antialiasingLevel': 0,
                        'ignoreSelfShadowing': 0,
                        'smoothLevel': 0,
                        'useMinEdgeLength': 0,
                        'renderSmoothLevel': 0,
                        'isHierarchicalConnection': 0,
                        'smoothUVs': 0,
                        'keepHardEdge': 0,
                        'displayCenter': 0,
                        'useSmoothPreviewForRender': 0,
                        'ghostColorPre': 0,
                        'displayInvisibleFaces': 0,
                        'vrts': 0,
                        'visibleFraction': 0,
                        'frozen': 0,
                        'propagateEdgeHardness': 0,
                        'perInstanceIndex': 0,
                        'useMinScreen': 0,
                        'maxShadingSamples': 0,
                        'maxVisibilitySamplesOverride': 0,
                        'isCollapsed': 0,
                        'blackBox': 0,
                        'displayAlphaAsGreyScale': 0,
                        'useMaxSubdivisions': 0,
                        'displayNormal': 0,
                        'reuseTriangles': 0,
                        'renderVolume': 0,
                        'minEdgeLength': 0,
                        'ghostColorPreA': 0,
                        'smoothTessLevel': 0,
                        'displayUVs': 0,
                        'lodVisibility': 0,
                        'useGlobalSmoothDrawType': 0,
                        'uvPivot': 0,
                        'shadingSamples': 0,
                        'featureDisplacement': 0,
                        'uvSize': 0,
                        'boundaryRule': 0,
                        'continuity': 0,
                        'osdVertBoundary': 0,
                        'shadingSamplesOverride': 0,
                        'volumeSamplesOverride': 0,
                        'displayTangent': 0,
                        'vertexBackfaceCulling': 0,
                        'displayTriangles': 0,
                        'displayColors': 0,
                        'volumeSamples': 0,
                        'useMeshSculptCache': 0,
                        'loadTiledTextures': 0,
                        'borderWidth': 0,
                        'perInstanceTag': 0,
                        'normalSize': 0,
                        'asBackground': 0,
                        'osdFvarBoundary': 0,
                        'depthJitter': 0,
                        'vertexSize': 0,
                        'outForceNodeUVUpdate': 0,
                        'uvpt': 0,
                        'useMaxEdgeLength': 0,
                        'displayFacesWithGroupId': 0,
                        'useMeshTexSculptCache': 0,
                        'computeFromSculptCache': 0,
                        'enableOpenCL': 0,
                        'template': 0,
                        'controlPoints': 0,
                        'isHistoricallyInteresting': 0,
                        'osdFvarPropagateCorners': 0,
                        'displayImmediate': 0,
                        'maxTriangles': 0,
                        'normalType': 0,
                        'maxEdgeLength': 0,
                        'showDisplacements': 0,
                        'allowTopologyMod': 0,
                        'displaySubdComps': 0,
                        'vertexIdMap': 0,
                        'wireColorRGB': 0,
                        'selectionChildHighlighting': 0,
                        'tweak': 0,
                        'maxVisibilitySamples': 0,
                        'osdSmoothTriangles': 0,
                        'maxUv': 0,
                        'ghosting': 0,
                        'pnts': 0,
                        'boundingBoxScale': 0,
                        'geometryAntialiasingOverride': 0,
                        'keepBorder': 0,
                        'faceIdMap': 0,
                        'relativeTweak': 0,
                        'extraSampleRate': 0,
                        'minScreen': 0,
                        'useNumTriangles': 0,
                        'vertexNormalMethod': 0,
                        'displayVertices': 0,
                        'inForceNodeUVUpdate': 0,
                        'hardwareFogMultiplier': 0,
                        'osdIndependentUVChannels': 0,
                        'normalThreshold': 0,
                        'keepMapBorders': 0,
                        'edgeIdMap': 0,
                        'useOsdBoundaryMethods': 0,
                        'maxSubd': 0,
                        'smoothWarn': 0,
                        'ghostColorPostA': 0,
                        'quadSplit': 0,
                        'useMaxUV': 0,
                        'displayNonPlanar': 0,
                        'ignoreHwShader': 0,
                        'displayHWEnvironment': 0,
                        'objectColorRGB': 0,
                        'displayBorders': 0,
                        'viewMode': 0,
                        'edge': 0,
                        'weights': 0,
                        'normals': 0,
                        'caching': 0,
                        'smoothOffset': 0}
