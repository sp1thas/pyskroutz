from pyskroutz.client.base import _SkroutzClient
from pyskroutz.models.categories import (
    CategoryList,
    CategoryRetrieve,
    SpecificationList,
)


class Categories(_SkroutzClient):
    ENDPOINT_PATH: str = "categories"

    def list(self, **pag_params) -> CategoryList:
        """List categories

        Examples:
            >>> client.categories.list()

        Args:
            **pag_params:

        Returns:

        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}"
        self._params = pag_params
        self._json: dict = {}
        self._data = None
        self._model = CategoryList
        self._method = "GET"
        return self.fetch()

    def retrive(self, id: int) -> CategoryRetrieve:
        """Retrieve a single category.

        Examples:
            >>> client.categories.retrieve(88)

        Args:
            id: category identifier

        Returns:
            Category details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}"
        # self._params = pag_params
        self._json = {}
        self._data = None
        self._model = CategoryRetrieve
        self._method = "GET"
        return self.fetch()

    def retrieve_parent(self, id: int) -> CategoryRetrieve:
        """Retrieve the parent of a category.

        Examples:
            >>> client.categories.retrieve_parent(88)

        Args:
            id: category identifier.

        Returns:
            Parent category details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/parent"
        # self._params = pag_params
        self._json = {}
        self._data = None
        self._model = CategoryRetrieve
        self._method = "GET"
        return self.fetch()

    def retrieve_root(self) -> CategoryRetrieve:
        """Retrieve the root category.

        Examples:
            >>> client.categories.retrieve_root()

        Returns:
            Root category details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/root"
        # self._params = pag_params
        self._json = {}
        self._data = None
        self._model = CategoryRetrieve
        self._method = "GET"
        return self.fetch()

    def list_children(self, id: int, **pag_params) -> CategoryList:
        """List the children categories of a category.

        Examples:
            >>> client.categories.list_children(252)

        Args:
            id: category identifier.
            **pag_params: pagination params.

        Returns:
            List details of children categories.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/children"
        self._params = pag_params
        self._json = {}
        self._data = None
        self._model = CategoryList
        self._method = "GET"
        return self.fetch()

    def list_specifications(
        self, id: int, include_group: bool = None, **pag_params
    ) -> SpecificationList:
        """List a category's specifications.

        Examples:
            >>> client.categories.list_specifications(40, include_group=True)

        Args:
            id: category identifier.
            include_group: Include group.
            **pag_params: pagination params.

        Returns:
            List of specification details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/specifications"
        self._params = pag_params
        if include_group is True:
            self._params["include"] = "group"
        self._json = {}
        self._data = None
        self._model = SpecificationList
        self._method = "GET"
        return self.fetch()

    def list_manufacturers(
        self, id: int, order_dir: str = None, **pag_params
    ) -> SpecificationList:
        """List a category's manufacturers.

        Examples:
            >>> client.categories.list_manufacturers(2)

        Args:
            id: category identifier.
            order_dir: Order ascending or descending (`asc`, `desc` default)
            **pag_params: pagination params.

        Returns:
            List manufactures details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/manufacturers"
        self._params = pag_params
        if order_dir is not None:
            self._params["order_dir"] = order_dir
        self._json = {}
        self._data = None
        self._model = SpecificationList
        self._method = "GET"
        return self.fetch()

    def list_favorites(self, id: int) -> SpecificationList:
        """List a category's favorites.

        Examples:
            >>> client.categories.list_favorites(40)

        Args:
            id: category identifier.
            **pag_params: pagination params.

        Returns:
            List favorites details.
        """
        self._url = f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/favorites"
        # self._params = pag_params
        self._json = {}
        self._data = None
        self._model = SpecificationList
        self._method = "GET"
        return self.fetch()
