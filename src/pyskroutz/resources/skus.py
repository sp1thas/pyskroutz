from typing import List, Optional

from . import PaginationParams
from .base import ApiResource
from .categories import Categories
from ..models.skus import (
    SkuList,
    SkuRetrieve,
    ReviewList,
    VoteRetrieve,
)
from ..utils import fluent


class Skus(ApiResource):
    """This Class holds the group of SKU related endpoints. More details in [sku](https://developer.skroutz.gr/api/v3/sku/) section."""

    ENDPOINT_PATH: str = "skus"

    @fluent
    def list(
        self,
        id: int,
        q: Optional[str] = None,
        manufacturer_ids: Optional[List[int]] = None,
        filter_ids: Optional[List[int]] = None,
        **pag_params: PaginationParams,
    ) -> None:
        """List SKUs of specific category

        Args:
            id: Category identifier.
            q: The keyword to search by.
            manufacturer_ids: The ids of the manufacturers of the SKUs.
            filter_ids: The ids of the filters to be applied on the SKUs.
            **pag_params: pagination parameters

        Examples:

            >>> pyskroutz.skus(client).list(40).execute()
        """
        params: dict = dict(**pag_params)
        if q is not None:
            params["q"] = q
        if manufacturer_ids:
            params["manufacturer_ids[]"] = manufacturer_ids
        if filter_ids:
            params["filter_ids"] = filter_ids
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{Categories.ENDPOINT_PATH}/{id}/skus",
            model=SkuList,
            params=params,
        )

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single SKU.

        Args:
            id: SKU identifier.

        Examples:
            >>> pyskroutz.skus(client).get(3443837).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}", model=SkuRetrieve
        )

    @fluent
    def get_similar(self, id: int) -> None:
        """Retrieve similar SKUs.

        Args:
            id: SKU identifier.

        Examples:

            >>> pyskroutz.skus(client).get_similar(3034682).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar", model=SkuList
        )

    @fluent
    def get_reviews(
        self,
        id: int,
        include_meta: Optional[str] = None,
        **pag_params: PaginationParams,
    ) -> None:
        """Retrieve a SKU's reviews

        Args:
            id: sku identifier
            include_meta: You may choose to include extra meta information using the following parameters: (sku_rating_breakdown, sku_reviews_aggregation)
            **pag_params: pagination params

        Examples:

            >>> pyskroutz.skus(client).get_reviews(3783654, include_meta='sku_rating_breakdown').execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews",
            params=dict(**pag_params)
            if include_meta is None
            else dict(include_meta=include_meta, **pag_params),
            model=ReviewList,
        )

    @fluent
    def vote_review(self, id: int, review_id: int, helpful: bool) -> None:
        """Vote a SKU's review

        Args:
            id: SKU Identifier.
            review_id: Review identifier.
            helpful: Helpful or not.

        Examples:

            >>> pyskroutz.skus(client).vote_review(3982592, 21943, True).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/votes",
            method="POST",
            json={"vote": {"helpful": helpful}},
            model=VoteRetrieve,
        )

    @fluent
    def flag_review(self, id: int, review_id: int, reason: str) -> None:
        """Flag a SKU's review

        Args:
            id: SKU Identifier.
            review_id: Review identifier.
            reason: bad_language, wrong_section or spam

        Examples:

            >>> pyskroutz.skus(client).flag_review(9783213, 240896, "spam").execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/flags",
            method="POST",
            model=VoteRetrieve,
            json={"vote": {"reason": reason}},
        )

    @fluent
    def get_review_form(self, id: int) -> None:
        """

        Args:
            id:
        """
        pass
