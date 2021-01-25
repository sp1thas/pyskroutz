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
        self._url = f"{self.BASE_URL}/{Categories.ENDPOINT_PATH}/{id}/skus"
        self._params = dict(**pag_params)
        if q is not None:
            self._params["q"] = q
        if manufacturer_ids:
            self._params["manufacturer_ids[]"] = manufacturer_ids
        if filter_ids:
            self._params["filter_ids"] = filter_ids
        self._json = {}
        self._data = None
        self._model = SkuList
        self._method = "GET"
        return self.fetch()

    def retrieve(self, id: int) -> SkuRetrieve:
        """Retrieve a single SKU.

        Examples:
            >>> client.skus.retrieve(3443837)

        Args:
            id: SKU identifier.

        Returns:
            SKU details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
        self._params = {}
        self._json = {}
        self._data = None
        self._model = SkuRetrieve
        self._method = "GET"
        return self.fetch()

    def retrieve_similar(self, id: int) -> SkuList:
        """Retrieve similar SKUs.

        Examples:
            >>> client.skus.retrieve_similar(3034682)

        Args:
            id: SKU identifier.

        Returns:
            Similar SKU details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar"
        self._params = {}
        self._json: dict = {}
        self._data = None
        self._model = SkuList
        self._method = "GET"
        return self.fetch()

    def retrive_reviews(
        self,
        id: int,
        include_meta: Optional[str] = None,
        **pag_params: PaginationParams,
    ) -> ReviewList:
        """Retrieve a SKU's reviews

        Examples:

            >>> client.skus.retrive_reviews(3783654, include_meta='sku_rating_breakdown')

        Args:
            id: sku identifier
            include_meta: You may choose to include extra meta information using the following parameters: (sku_rating_breakdown, sku_reviews_aggregation)
            **pag_params: pagination params

        Returns:
            list of reviews.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews"
        self._params = dict(**pag_params)
        if include_meta:
            self._params["include_meta"] = include_meta
        self._json = {}
        self._data = None
        self._model = ReviewList
        self._method = "GET"
        return self.fetch()

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
        self._url = (
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/votes"
        )
        self._json = {"vote": {"helpful": helpful}}
        self._data = None
        self._model = VoteRetrieve
        self._method = "POST"
        return self.fetch()

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
        self._url = (
            f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/reviews/{review_id}/flags"
        )
        self._json = {"vote": {"reason": reason}}
        self._data = None
        self._model = VoteRetrieve
        self._method = "POST"
        return self.fetch()

    def retrieve_review_form(self, id: int) -> ReviewFormRetrieve:
        """

        Args:
            id:

        Returns:
        """
        pass
