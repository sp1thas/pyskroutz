## `get`
::: pyskroutz.user.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.user(client).get().execute()
    ```

=== "Response (pydantic object)"

## `update`
::: pyskroutz.user.update
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).update(sex="male", birthyear=1980).execute()
    ```

=== "Response (pydantic object)"


## `get_avatars`
::: pyskroutz.user.get_avatars
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).get_avatars().execute()
    ```

=== "Response (pydantic object)"


## `get_addresses`
::: pyskroutz.user.get_addresses
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).get_addresses().execute()
    ```

=== "Response (pydantic object)"


## `get_address_form`
::: pyskroutz.user.get_address_form
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).get_address_form().execute()
    ```

=== "Response (pydantic object)"


## `new_address_form`
::: pyskroutz.user.get_address_form
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).new_address_form(
        label="home", first_name="bill", last_name="Testopoulos",
        street_name="Panagouli", street_number="61",
        city="Nea Ionia", zip=14123, reqion_id=5
    ).execute()
    ```

=== "Response (pydantic object)"


## `update_address`
::: pyskroutz.user.update_address
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).update_address(
        48937, street_number=62
    ).execute()
    ```

=== "Response (pydantic object)"


## `delete_address`
::: pyskroutz.user.delete_address
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).delete_address(48937).execute()
    ```

=== "Response (pydantic object)"


## `saved_orders`
::: pyskroutz.user.saved_orders
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.user(client).saved_orders().execute()
    ```

=== "Response (pydantic object)"


## `logout`
::: pyskroutz.user.logout
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.users(client).logout().execute()
    ```

=== "Response (pydantic object)"


## Response Models
::: pyskroutz.models.users
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3