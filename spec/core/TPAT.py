from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('TPAT',
                 doc="""
The full name of the pattern.
ex: "felsic volcanics"
Code:          Short-form of the pattern description. This is the value
which typically appears (for instance) in the "Rock code"
channel in a Wholeplot From-To data group.
ex: "FVOL"
The code is CASE-SENSITIVE.

Label:         Text to use as a short-form in labels, graphs etc.
By default, this is the same as the code.
ex: "FVol."
Pattern Attributes:  (See DEFAULT.:class:`PAT` in \\src\\etc for more inforation)
Pattern:       The Pattern Index; defined in DEFAULT.:class:`PAT`, or in the user's
USER.:class:`PAT` file. If not specified, defaults to 0 (solid fill).
Size:          The pattern tile size. If not specified, defaults to 2.0mm.
Density:       The tiling density. If not specified, defaults to 1.0.
Thickness:     The line thickness in the tile, expressed as a integer
percentage (0-100) of the tile size.
Colour:        The pattern line work colour. If not specified, defaults to black.

Background colour: The pattern background colour. If not specified, defaults to
transparent (C_ANY_NONE)


Symbols:

Symbol Font     The name of the symbol font to use for a given symbol index

Symbol Number   Index into the font.

Symbol Rotation: Rotation in degrees CCW.

Symbol Scaling  Additional scale factor to apply to symbol size (Default 1.0)
""")


gx_defines = [
    Define('TPAT_STRING_SIZE',
           doc="Default string sizes.",
           constants=[
               Constant('TPAT_CODE_SIZE', value='21', type=Type.INT32_T)                        ,
               Constant('TPAT_LABEL_SIZE', value='32', type=Type.INT32_T)                        ,
               Constant('TPAT_DESC_SIZE', value='128', type=Type.INT32_T)                        ,
               Constant('TPAT_SYMBFONT_SIZE', value='32', type=Type.INT32_T)                        
           ])]


gx_methods = {
    'Miscellaneous': [

        Method('AddColor_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Add a new color to the list",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Code (required - CASE SENSITIVE)"),
                   Parameter('p3', type=Type.STRING,
                             doc='Label (optional, can be "")'),
                   Parameter('p4', type=Type.STRING,
                             doc='Description (optional, can be "")'),
                   Parameter('p5', type=Type.INT32_T,
                             doc="Color (use :func:`iColor_MVIEW` to convert to int).")
               ]),

        Method('Create_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Creates an empty thematic pattern object.",
               return_type="TPAT",
               return_doc=":class:`TPAT` object"),

        Method('Destroy_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Destroys a pattern object.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` Handle")
               ]),

        Method('iCode_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Find the index of a given thematic pattern",
               return_type=Type.INT32_T,
               return_doc="The code index, -1 if not found",
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Pattern code (case sensitive)")
               ]),

        Method('IGetSolidPattern_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Get solid pattern info from the :class:`TPAT`.",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` handle"),
                   Parameter('p2', type=Type.INT32_T,
                             doc="index"),
                   Parameter('p3', type=Type.STRING, is_ref=True, size_of_param='3',
                             doc="Returned Code"),
                   Parameter('p4', type=Type.INT32_T, default_length='TPAT_CODE_SIZE',
                             doc="length of supplied code string variable"),
                   Parameter('p5', type=Type.STRING, is_ref=True, size_of_param='5',
                             doc="Returned Label"),
                   Parameter('p6', type=Type.INT32_T, default_length='TPAT_LABEL_SIZE',
                             doc="length of supplied code string variable"),
                   Parameter('p7', type=Type.STRING, is_ref=True, size_of_param='7',
                             doc="Returned Description"),
                   Parameter('p8', type=Type.INT32_T, default_length='TPAT_DESC_SIZE',
                             doc="length of supplied code string variable"),
                   Parameter('p9', type=Type.INT32_T, is_ref=True,
                             doc="Color.")
               ]),

        Method('iSize_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Returns the number of rows (items) in the :class:`TPAT` object.",
               return_type=Type.INT32_T,
               return_doc="Number of :class:`TPAT` items.",
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` Handle")
               ]),

        Method('LoadCSV_TPAT', module='geoengine.core', version='7.0.0',
               availability=Availability.PUBLIC, 
               doc="Load thematic patterns from a CSV file",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` handle"),
                   Parameter('p2', type=Type.STRING,
                             doc="Thematic Pattern file name")
               ]),

        Method('SetupTranslationVV_TPAT', module='geoengine.core', version='7.3.0',
               availability=Availability.PUBLIC, 
               doc="Initializes a :class:`VV` used to map :class:`TPAT` indices to output values",
               return_type=Type.VOID,
               parameters = [
                   Parameter('p1', type="TPAT",
                             doc=":class:`TPAT` Handle"),
                   Parameter('p2', type="LTB",
                             doc="Table containing :class:`TPAT` codes as the key"),
                   Parameter('p3', type=Type.INT32_T,
                             doc="Field in :class:`LTB` with the output values (numeric or string)"),
                   Parameter('p4', type="VV",
                             doc="Returned values for each :class:`TPAT` index")
               ])
    ]
}
