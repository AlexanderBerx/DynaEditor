class AttrTypeError(TypeError):
    """
    AttrTypeError class, for when an attribute of a non existing type is attempted to
    be created
    Note: Not using TypeError directly for this since this would also catch when an
    attribute would be attempted to be created with invalid arguments
    """
    pass
