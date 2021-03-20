from typing import List, Optional

from . import PaginationParams
from .base import ApiResource
from .categories import Categories
from ..models.skus import (
    SkuList,
    SkuRetrieve,
    ReviewList,
    ReviewFormRetrieve,
    VoteRetrieve,
)
from ..utils import fluent


class Skus(ApiResource):
    """This Class holds the group of SKU related endpoints. A SKU (Stock Keeping Unit) is an aggregation of products.
    More details in [sku](https://developer.skroutz.gr/api/v3/sku/) section.
    """

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
        """
        params: dict = dict(**pag_params)

        params.update(
            {
                n: v
                for n, v in zip(
                    ("q", "manufacturer_ids[]", "filter_ids"),
                    (q, manufacturer_ids, filter_ids),
                )
                if v is not None
            }
        )
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
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}", model=SkuRetrieve
        )

    @fluent
    def get_similar(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve similar SKUs.

        Args:
            id: SKU identifier.
            pag_params: pagination parameters.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar",
            model=SkuList,
            params=pag_params,
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
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/flags",
            method="POST",
            model=VoteRetrieve,
            json={"vote": {"reason": reason}},
        )

    @fluent
    def get_review_form(self, id: int) -> None:
        """Retrieve a SKU review form

        Args:
            id: SKU Identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/new",
            model=ReviewFormRetrieve,
        )
