from typing import List, Optional

from . import PaginationParams
from .categories import Categories
from ..client.base import _SkroutzClient
from ..models.skus import (
    SkuList,
    SkuRetrieve,
    ReviewList,
    VoteRetrieve,
    FlagRetrieve,
    ReviewFormRetrieve,
)


class Skus(_SkroutzClient):
    """This Class holds the group of SKU related endpoints. More details in [sku](https://developer.skroutz.gr/api/v3/sku/) section."""

    ENDPOINT_PATH: str = "skus"

    def list(
        self,
        id: int,
        q: Optional[str] = None,
        manufacturer_ids: Optional[List[int]] = None,
        filter_ids: Optional[List[int]] = None,
        **pag_params: PaginationParams,
    ) -> SkuList:
        """List SKUs of specific category

        Examples:

            >>> client.skus.list(40)

        Args:
            id: Category identifier.
            q: The keyword to search by.
            manufacturer_ids: The ids of the manufacturers of the SKUs.
            filter_ids: The ids of the filters to be applied on the SKUs.
            **pag_params: pagination parameters

        Returns:
            List of skus under the given category.
        """
        params: dict = dict(**pag_params)
        if q is not None:
            params["q"] = q
        if manufacturer_ids:
            params["manufacturer_ids[]"] = manufacturer_ids
        if filter_ids:
            params["filter_ids"] = filter_ids
        return self.fetch(
            f"{self.BASE_URL}/{Categories.ENDPOINT_PATH}/{id}/skus",
            "GET",
            SkuList,
            params=params,
        )

    def get(self, id: int) -> SkuRetrieve:
        """Retrieve a single SKU.

        Examples:
            >>> client.skus.get(3443837)

        Args:
            id: SKU identifier.

        Returns:
            SKU details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}", "GET", SkuRetrieve
        )

    def get_similar(self, id: int) -> SkuList:
        """Retrieve similar SKUs.

        Examples:

            >>> client.skus.get_similar(3034682)

        Args:
            id: SKU identifier.

        Returns:
            Similar SKU details.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar", "GET", SkuList
        )

    def get_reviews(
        self,
        id: int,
        include_meta: Optional[str] = None,
        **pag_params: PaginationParams,
    ) -> ReviewList:
        """Retrieve a SKU's reviews

        Examples:

            >>> client.skus.get_reviews(3783654, include_meta='sku_rating_breakdown')

        Args:
            id: sku identifier
            include_meta: You may choose to include extra meta information using the following parameters: (sku_rating_breakdown, sku_reviews_aggregation)
            **pag_params: pagination params

        Returns:
            list of reviews.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews",
            "GET",
            ReviewList,
            dict(**pag_params)
            if include_meta is None
            else dict(include_meta=include_meta, **pag_params),
        )

    def vote_review(self, id: int, review_id: int, helpful: bool) -> VoteRetrieve:
        """Vote a SKU's review

        Examples:

            >>> client.skus.vote_review(3982592, 21943, True)

        Args:
            id: SKU Identifier.
            review_id: Review identifier.
            helpful: Helpful or not.

        Returns:
            Vote response.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/votes",
            "POST",
            VoteRetrieve,
            json={"vote": {"helpful": helpful}},
        )

    def flag_review(self, id: int, review_id: int, reason: str) -> FlagRetrieve:
        """Flag a SKU's review

        Examples:

            >>> client.skus.flag_review(9783213, 240896, "spam")

        Args:
            id: SKU Identifier.
            review_id: Review identifier.
            reason: bad_language, wrong_section or spam

        Returns:
            Vote response.
        """
        return self.fetch(
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/flags",
            "POST",
            VoteRetrieve,
            json={"vote": {"reason": reason}},
        )

    def get_review_form(self, id: int) -> ReviewFormRetrieve:
        """

        Args:
            id:

        Returns:
        """
        pass
