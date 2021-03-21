from .base import ApiResource
from .categories import Categories
from ..models import users
from ..utils import fluent


class Users(ApiResource):
    """This Class holds the group of User related endpoints. Provides information about Users.
    More details in [user](https://developer.skroutz.gr/api/v3/user) section.

    **Field Guide**:

    Field                 | Type   | Description
    -------------         | ------ | ------------
    `id`                  | Number | The unique identifier reference to the resource
    `username`            | String | The username of the user
    `type`                | String | The type of the account. Possible values: `"skroutz"`, `"open_id"`, `"twitter"`, `"facebook"`, `"google"`
    `sex`                 | String | `"male"` or `"female"` or `null`
    `avatar`              | String | URI of the avatar image of the user
    `created_at`          | String | Account creation date
    `email`               | String | The email of the user
    `birthyear`           | Number | The birthyear of the user
    `mobile`              | String | The mobile number of the user
    `stats`               | Hash   | Review / comment related stats
    `email_notifications` | Array  | Available email preferences and their status
    `is_staff`            | String | True when user is a staff member
    """

    ENDPOINT_PATH: str = "user"

    @fluent
    def get(
        self,
    ) -> None:
        """Retrieve the profile of the authenticated user"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}", model=users.UserRetrieve
        )

    @fluent
    def update(self, **kwargs) -> None:
        """
        Update profile information

        Args:
            **kwargs: Pass the field name and the new value.
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}",
            model=users.UserRetrieve,
            method="PATCH",
            json=kwargs,
        )

    @fluent
    def get_avatars(self) -> None:
        """Retrieve the selection of predefined avatars"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/avatars", model=users.AvatarList
        )

    @fluent
    def get_addresses(self) -> None:
        """Retrieve user addresses"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/addresses",
            model=users.AddressList,
        )

    @fluent
    def get_address_form(self) -> None:
        """Retrieve user address form"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/addresses/new",
            model=users.AddressFormRetrieve,
        )

    @fluent
    def new_address_form(self, **address_kwargs) -> None:
        """Create a new user address

        Args:
            **address_kwargs:
                label: address label
                first_name: first name
                last_name: last name
                street_name: street name
                street_number: street number
                city: city
                zip: zip code
                reqion_id: region id
                phone: phone number
                mobile: mobile number
                lng: longtitude
                lat: latitude
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/addresses",
            model=users.AddressItem,
            json=address_kwargs,
            method="POST",
        )

    @fluent
    def update_address(self, id, **address_kwargs) -> None:
        """Update an existing user address

        Args:
            id: Addres identifier
            **address_kwargs:
                label: address label
                first_name: first name
                last_name: last name
                street_name: street name
                street_number: street number
                city: city
                zip: zip code
                reqion_id: region id
                phone: phone number
                mobile: mobile number
                lng: longtitude
                lat: latitude
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/addresses/{id}",
            model=users.AddressItem,
            json=address_kwargs,
            method="POST",
        )

    @fluent
    def delete_address(self, id) -> None:
        """Delete an existing user address

        Args:
            id: Address identifier
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/addresses/{id}",
            method="DELETE",
            model=None,
        )

    @fluent
    def saved_orders(self) -> None:
        """User saved orders"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/saved_orders",
            model=users.SavedOdersList,
        )

    @fluent
    def logout(self) -> None:
        """User logout"""
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/logout",
            model=None,
            method="DELETE",
        )
