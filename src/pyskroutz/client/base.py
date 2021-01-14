from typing import Dict, Any
from ..exceptions import SkroutzApiError
import requests
from functools import wraps
from pydantic import BaseModel

ENABLED_ENDPOINT = ("categories",)


class HttpClient:
    DOMAIN: str = "www.skroutz.gr"
    BASE_URL = f"http://api.{DOMAIN}/api"
    client_id: str = None
    client_secret: str = None
    access_token: str = None
    access_token_exp: str = None
    headers: Dict[str, str] = None
    access_token_type: str = None
    s: requests.Session = None

    def __init__(self, client_id=None, client_secret=None):
        """
        Create an access token

        :param str client_id: your client id
        :param str client_secret: your client secret
        """
        if None in [client_id, client_secret]:
            raise ValueError("You have to give client_id and client_secret")
        self.client_id = client_id
        self.client_secret = client_secret
        self.s = requests.Session()
        self.authenticate()

    def authenticate(self):
        req = requests.post(
            f"https://{self.DOMAIN}/oauth2/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials",
                "scope": "public",
            },
        )
        if req.status_code == 200:
            self.access_token = req.json()["access_token"]
            self.access_token_exp = req.json()["expires_in"]
            self.access_token_type = req.json()["token_type"]
            self.headers = {
                "Accept": "application/vnd.skroutz+json; version=3",
                "Authorization": "%s %s"
                % (self.access_token_type.capitalize(), self.access_token),
            }
        elif req.status_code == 401:
            raise SkroutzApiError(req.json()["error"])
        else:
            raise SkroutzApiError("Something bad happened")

    def fetch(self, method: str, url: str, params: dict, json: dict, data: Any):
        resp = self.s.send(
            self.s.prepare_request(
                requests.Request(
                    method=method, url=url, data=data, headers=self.headers, params=params, json=json
                )
            )
        )
        return resp.json()


class SkroutzClient:
    http: HttpClient = None

    def __init__(self, client_id=None, client_secret=None):
        """
        Create an access token

        :param str client_id: your client id
        :param str client_secret: your client secret
        """
        self.http = HttpClient(client_id, client_secret)




    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Category
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def categories(self):
        """
        Lists all categories
        """
        req = requests.get("http://api.skroutz.gr/categories", headers=self.headers)
        return req.json()

    def category(self, category_id):
        """
        Retrieve a single category

        :param int category_id: Category ID
        :return: Category infos
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/categories/%s" % str(category_id),
            headers=self.headers,
        )
        return req.json()

    def category_parent(self, category_id):
        """
        Retrieve the parent of a category

        :param int category_id: Category ID
        :return: Parent category infos
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/categories/%s/parent" % str(category_id),
            headers=self.headers,
        )
        return req.json()

    def category_root(self):
        """
        Retrieve the root category

        :return: Root category infos
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/categories/root", headers=self.headers
        )
        return req.json()

    def category_children(self, category_id):
        """
        List the children categories of a category

        :param int category_id: Category ID
        :return: children categories
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/categories/%s/children" % str(category_id),
            headers=self.headers,
        )
        return req.json()

    def category_specifications(self, category_id, group=False):
        """
        List a category's specifications

        :param int category_id: Category ID
        :param bool group: specification group
        :return: category specifications
        :rtype: dict
        """
        if group:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/specifications?include=group"
                % str(category_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/specifications" % str(category_id),
                headers=self.headers,
            )
        return req.json()

    def category_manufacturers(self, category_id, order_by=None, order_dir=None):
        """
        List a category's manufacturers

        :param int category_id: Category ID
        :param bool group: manufacturers group
        :param str order_by: order by name, popularity default
        :param str order_dir: order asc, desc default
        :return: category manufacturers
        :rtype: dict
        """
        if order_by is not None and order_dir is None:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/manufacturers?order_by=%s"
                % (str(category_id), order_by),
                headers=self.headers,
            )
        elif order_by is None and order_dir is not None:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/manufacturers?order_dir=%s"
                % (str(category_id), order_dir),
                headers=self.headers,
            )
        elif order_by is not None and order_dir is not None:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/manufacturers?order_by=%s?order_dir=%s"
                % (str(category_id), order_by, order_dir),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/categories/%s/manufacturers" % str(category_id),
                headers=self.headers,
            )
        return req.json()

    def category_favorites(self, category_id):
        """
        List a category's favorites

        :param str category_id: Category ID
        :return: Category favorites
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/categories/%s/favorites" % str(category_id),
            headers=self.headers,
        )
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ SKU
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def sku_category(
        self,
        category_id,
        q=None,
        manufacturer_ids=None,
        filter_ids=None,
        order_by=None,
        order_dir=None,
        include_meta=None,
    ):
        """
        List SKUs of specific category

        :param int category_id: Category ID
        :param str q: query
        :param list manufacturer_ids: list of manufacturer ids
        :param list filter_ids: list of filter ids
        :param str order_by: order by name, popularity default
        :param str order_dir: order asc, desc default
        :return: list skus of category
        :rtype: dict
        """
        url = "http://api.skroutz.gr/categories/%s" % str(category_id)
        if manufacturer_ids is not None:
            url = "http://api.skroutz.gr/categories/%s/skus?manufacturer_ids[]=%s" % (
                str(category_id),
                "&manufacturer_ids[]=".join([str(_) for _ in manufacturer_ids]),
            )
        if q is not None:
            url = "http://api.skroutz.gr/categories/40/skus?q=%s" % q.replace(" ", "+")
        if filter_ids:
            url = "http://api.skroutz.gr/categories/%s/skus?filter_ids[]=%s" % (
                category_id,
                "&filter_ids[]=".join([str(_) for _ in filter_ids]),
            )
        if order_by:
            url += "?order_by=%s" % order_by
        elif order_dir:
            url += "?order_dir=%s" % order_dir
        if include_meta:
            url += "?include_meta=%s" % include_meta
        req = requests.get(url, headers=self.headers)
        return req.json()

    def sku_single(
        self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False
    ):
        """
        Retrieve a single SKU

        :param int sku_id: SKU ID
        :param bool sku_rating_breakdown: Review stats
        :param bool sku_reviews_aggregation: Reviews aggregation
        :return: sku details
        :rtype: dict
        """
        if sku_rating_breakdown is not None and sku_reviews_aggregation is None:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s?include_meta=sku_rating_breakdown"
                % str(sku_id),
                headers=self.headers,
            )
        elif sku_rating_breakdown is None and sku_reviews_aggregation is not None:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s?include_meta=sku_reviews_aggregation"
                % str(sku_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s" % str(sku_id), headers=self.headers
            )
        return req.json()

    def sku_similar(
        self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False
    ):
        """
        Retrieve similar SKUs

        :param int sku_id: SKU ID
        :param bool sku_rating_breakdown: Review stats
        :param bool sku_reviews_aggregation: Reviews aggregation
        :return: similar skus details
        :rtype: dict
        """
        if sku_rating_breakdown is not None and sku_reviews_aggregation is None:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/similar?include_meta=sku_rating_breakdown"
                % str(sku_id),
                headers=self.headers,
            )
        elif sku_reviews_aggregation:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/similar?include_meta=sku_reviews_aggregation"
                % str(sku_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/similar" % str(sku_id),
                headers=self.headers,
            )
        return req.json()

    def sku_products(
        self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False
    ):
        """
        Retrieve an SKU's products

        :param int sku_id: SKU ID
        :param bool sku_rating_breakdown: Review stats
        :param bool sku_reviews_aggregation: Reviews aggregation
        :return: skus products
        :rtype: dict
        """
        if sku_rating_breakdown:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/products?include_meta=sku_rating_breakdown"
                % str(sku_id),
                headers=self.headers,
            )
        elif sku_reviews_aggregation:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/products?include_meta=sku_reviews_aggregation"
                % str(sku_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/products" % str(sku_id),
                headers=self.headers,
            )
        return req.json()

    def sku_reviews(
        self, sku_id, sku_rating_breakdown=False, sku_reviews_aggregation=False
    ):
        """
        Retrieve an SKU's reviews

        :param int sku_id: SKU ID
        :param bool sku_rating_breakdown: Review stats
        :param bool sku_reviews_aggregation: Reviews aggregation
        :return: skus reviews
        :rtype: dict
        """
        if sku_rating_breakdown:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_rating_breakdown"
                % str(sku_id),
                headers=self.headers,
            )
        elif sku_reviews_aggregation:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/reviews?include_meta=sku_reviews_aggregation"
                % str(sku_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/reviews" % str(sku_id),
                headers=self.headers,
            )
        return req.json()

    def sku_vote_review(self, sku_id=None, review_id=None, helpful=None):
        """
        Vote a SKU's review

        :param int sku_id: SKU ID
        :param int review_id: Review id
        :helpful:
        :return:
        :rtype: dict
        """
        pass

    def sku_review_votes(self, sku_id=None, review_id=None):
        req = requests.post(
            "http://api.skroutz.gr/skus/%s/reviews/%s/votes"
            % (str(sku_id), str(review_id)),
            headers=self.headers,
        )
        return req.json()

    def sku_specifications(self, sku_id, group=False):
        """
        Retrieve an SKU's specifications

        :param int sku_id: SKU ID
        :param bool group: specification group
        :return: sku specifications
        :rtype: dict
        """
        if group:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/specifications?include=group"
                % str(sku_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/skus/%s/specifications" % str(sku_id),
                headers=self.headers,
            )
        return req.json()

    def sku_pricehistory(self, sku_id):
        """
        Retrieve a SKU's price history

        :param int sku_id: SKU ID
        :return: sku price history
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/skus/%s/price_history" % str(sku_id),
            headers=self.headers,
        )
        return req.json()

    def sku_favorite(self, sku_id):
        """
        Retrieve an SKU's favorite

        :param int sku_id: SKU ID
        :return: sku favorite
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/skus/%s/favorite" % str(sku_id), headers=self.headers
        )
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Product
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def product_single(self, pr_id):
        """
        Retrieve a single product

        :param int pr_id: product ID
        :return: product details
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/products/%s" % str(pr_id), headers=self.headers
        )
        return req.json()

    def product_search(self, shop_id=None, shop_uid=None):
        """
        Search for products

        :param int shop_id: shop id
        :param int shop_uid: shop unique id
        :return: search results
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/shops/%s/products/search?shop_uid=%s"
            % (str(shop_id), str(shop_uid)),
            headers=self.headers,
        )
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Shop
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def shop(self, shop_id):
        """
        Retrieve a single shop

        :param int shop_id: shop id
        :return: shot details
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/shops/%s" % str(shop_id), headers=self.headers
        )
        return req.json()

    def shop_reviews(self, shop_id):
        """
        Retrieve a shop's reviews

        :param int shop_id: shop id
        :return: shop's reviews
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/%s/reviews" % str(shop_id), headers=self.headers
        )
        return req.json()

    def shop_locations(self, shop_id, embed_address=False):
        """
        List shop locations

        :param int shop_id: shop id
        :param bool embed_address: include addresses
        :return: shop locations
        :rtype: dict
        """
        if not embed_address:
            req = requests.get(
                "http://api.skroutz.gr/shops/%s/locations" % str(shop_id),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/shops/%s/locations?embed=address" % str(shop_id),
                headers=self.headers,
            )
        return req.json()

    def shop_location(self, shop_id=None, lc_id=None, embed_address=False):
        """
        Retrieve a single shop location

        :param int shop_id: shop id
        :param lc_id: location id
        :param bool embed_address: include addresses
        :return: shop location
        :rtype: dict
        """
        if not embed_address:
            req = requests.get(
                "http://api.skroutz.gr/shops/%s/locations/%s"
                % (str(shop_id), str(lc_id)),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/shops/%s/locations/%s?embed=address"
                % (str(shop_id), str(lc_id)),
                headers=self.headers,
            )
        return req.json()

    def shop_search(self, q):
        """
        Search for shops

        :param str q: query
        :return: search results
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/shops/search?q=%s" % str(q), headers=self.headers
        )
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Manufacturer
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def manufacturer_listall(self):
        """
        List manufacturers

        :return: all manufacturers
        :rtype: dict
        """
        req = requests.get("http://api.skroutz.gr/manufacturers", headers=self.headers)
        return req.json()

    def manufacturer(self, mnfct_id):
        """
        Retrieve a single manufacturer

        :param int mnfct_id: manufacturer id
        :return: manufacturer details
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/manufacturers/%s" % str(mnfct_id),
            headers=self.headers,
        )
        return req.json()

    def manufacturer_categories(self, mnfct_id, order_by=None, order_dir=None):
        """
        Retrieve a manufacturer's categories

        :param int mnfct_id: manufacturer id
        :param str order_by: order by name, popularity default
        :param str order_dir: order asc, desc default
        :return: manufacturer categories
        :rtype: dict
        """
        if order_by:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/categories?order_by=%s"
                % (str(mnfct_id), order_by),
                headers=self.headers,
            )
        elif order_dir:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/categories?order_dir=%s"
                % (str(mnfct_id), order_dir),
                headers=self.headers,
            )
        else:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/categories" % str(mnfct_id),
                headers=self.headers,
            )
        return req.json()

    def manufacturer_sku(self, mnfct_id, order_by=None, order_dir=None):
        """
        Retrieve a manufacturer's SKUs

        :param int mnfct_id: manufacturer id
        :param str order_by: order by name, popularity default
        :param str order_dir: order asc, desc default
        :return: manufacturer's skus
        :rtype: dict
        """
        if order_by:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/skus?order_by=%s"
                % (str(mnfct_id), order_by),
                headers=self.headers,
            )
            return req.json()
        elif order_dir:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/skus?order_dir=%s"
                % (str(mnfct_id), order_dir),
                headers=self.headers,
            )
            return req.json()
        else:
            req = requests.get(
                "http://api.skroutz.gr/manufacturers/%s/skus" % str(mnfct_id),
                headers=self.headers,
            )
            return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Search
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def search(self, q):
        """
        Search

        :param str q: query
        :return: search results
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/search?q=%s" % q.replace(" ", "+"),
            headers=self.headers,
        )
        return req.json()

    def search_autocomplete(self, q):
        """
        Autocomplete

        :param str q: query
        :return: search results
        :rtype: dict
        """
        req = requests.get(
            "http://api.skroutz.gr/autocomplete?q=%s" % q.replace(" ", "+"),
            headers=self.headers,
        )
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ Flag
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def flags(self):
        """
        Retrieve all flags

        :return: all flags
        :rtype: dict
        """
        req = requests.get("http://api.skroutz.gr/flags", headers=self.headers)
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ User
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def user(self):
        """
        Retrieve the profile of the authenticated user

        :return: user details
        :rtype: dict
        """
        req = requests.get("http://api.skroutz.gr/user", headers=self.headers)
        return req.json()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~ User Favorite
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def user_favorite_list(self):
        """
        List favorite lists

        :return: user favorite list
        :rtype: dict
        """
        req = requests.get("http://api.skroutz.gr/favorite_lists", headers=self.headers)
        return req.json()

    def user_favorite_create_list(self, name):
        """
        Create a favorite_list

        :param str name: list name
        :rtype: dict
        """
        req = requests.post(
            "http://api.skroutz.gr/favorite_lists[name]=%s" % name.replace(" ", "+"),
            headers=self.headers,
        )
        return req.json()

    def user_favorite_destroy_list(self, usr_fv_id):
        """
        Destroy a favorite_list

        :param int usr_fv_id: favorite id
        :rtype: dict
        """
        req = requests.delete(
            "http://api.skroutz.gr/favorite_lists/%s" % str(usr_fv_id),
            headers=self.headers,
        )
        return req.json()
