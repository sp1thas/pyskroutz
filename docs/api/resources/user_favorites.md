## `get_lists`
::: pyskroutz.favorites.get_lists
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).get_lists().execute()
    ```

=== "Response (pydantic object)"


## `create_list`
::: pyskroutz.favorites.create_list
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).create_list("test name").execute()
    ```

=== "Response (pydantic object)"

## `destroy_list`
::: pyskroutz.favorites.destroy_list
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).destroy_list(973812).execute()
    ```

=== "Response (pydantic object)"

## `list_favorites`
::: pyskroutz.favorites.list_favorites
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).list_favorites().execute()
    ```

=== "Response (pydantic object)"

## `get_favorite`
::: pyskroutz.favorites.get_favorite
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).get_favorite(5896665).execute()
    ```

=== "Response (pydantic object)"

## `create_favorite`
::: pyskroutz.favorites.create_favorite
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).create_favorite(7957675).execute()
    ```

=== "Response (pydantic object)"

## `destroy_favorite`
::: pyskroutz.favorites.destroy_favorite
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.favorites(client).destroy_favorite(5896665).execute()
    ```

=== "Response (pydantic object)"


## Response Models
::: pyskroutz.models.favorites
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3