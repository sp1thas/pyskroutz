import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict

from typing import Optional


class PaginationParams(TypedDict):
    """Pagionation parameters.

    Attributes:
        per: number of entries per page.
        page: page number.
    """

    per: Optional[int]
    page: Optional[int]
