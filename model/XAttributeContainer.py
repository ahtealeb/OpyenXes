from model.XAttributeCollection import XAttributeCollection


class XAttributeContainer(XAttributeCollection):
    """Attribute with child attributes. Theses child attributes are not ordered.

    :param key: The key of the attribute.
    :type key: str
    :param extension: The extension defining the attribute (set to None, if
     the attribute is not associated to an extension)
    :type extension: XExtension or None
    """
    def __init__(self, key, extension=None):
        super().__init__(key, extension)
