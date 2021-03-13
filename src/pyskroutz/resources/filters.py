from .base import ApiResource
from ..resources import PaginationParams
from ..models import filters
from ..utils import fluent


class Filters(ApiResource):
    """This Class holds the group of Filters related endpoints.
    More details in [filters](https://developer.skroutz.gr/api/v3/filters/) section.
    """

    @fluent
    def get(self, category_id: int, **pag_params: PaginationParams) -> None:
        """List FilterGroups

        Args:
            category_id: Category identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/categories/{category_id}/filter_groups",
            method="GET",
            model=filters.FilterGroupsList,
            params=pag_params,
        )
