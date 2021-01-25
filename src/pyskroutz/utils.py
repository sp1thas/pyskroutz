import functools
from typing import Any


def rsetattr(obj: object, attr: str, val):
    """Set attribute recursively.

    Examples:
        >>> from argparse import Namespace
        >>> from pyskroutz.utils import rsetattr
        >>> ns_obj = Namespace()
        >>> ns_obj.a = Namespace()
        >>> rsetattr(ns_obj, 'a.b', 1)
        >>> ns_obj.a.b
        1

    Args:
        obj: Object.
        attr: Attribute name (period separated for nested attributes).
        val: Attribute value.

    Returns:

    """
    pre, _, post = attr.rpartition(".")
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)


def rgetattr(obj, attr: str, *args) -> Any:
    """Get recursive attribute.

    Examples:
        >>> from argparse import Namespace
        >>> from pyskroutz.utils import rgetattr
        >>> ns_obj = Namespace()
        >>> ns_obj.a = Namespace()
        >>> ns_obj.a.b = 1
        >>> rgetattr(ns_obj, 'a.b')
        1

    Args:
        obj: Object.
        attr: Attribute name (period separated for nested attributes).
        *args:

    Returns: Attribute value

    """

    def _getattr(obj, attr) -> Any:
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))
