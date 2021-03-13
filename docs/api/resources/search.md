## `search`
::: pyskroutz.search.__call__
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.search(client)("iphone").execute()
    ```

=== "Response (pydantic object)"

    ```python
    SearchResultsList(
        categories=[],
        meta=SearchMeta(
            q=None,
            alternatives=[],
            strong_matches=StrongMatcheItem(
                sku=None,
                manufacturer=ManufacturerItem(
                    id=356,
                    name="Apple",
                    image_url=HttpUrl(
                        "https://a.scdn.gr/ds/manufacturers/356/20160322115406_ae6f9a87.png",
                        scheme="https",
                        host="a.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/ds/manufacturers/356/20160322115406_ae6f9a87.png",
                    ),
                ),
            ),
            pagination=PaginationItem(page=1, per=25, total_pages=0, total_results=0),
        ),
    )
    ```

## `autocomplete`
::: pyskroutz.search.autocomplete
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.search(client).autocomplete("iph").execute()
    ```

=== "Response (pydantic object)"

    ```python
    AutocompleteList(
        autocomplete=[
            AutocompleteItem(k="iphone", i=3, d=None),
            AutocompleteItem(k="iphone 11", i=3, d=None),
            AutocompleteItem(k="iphone 12", i=3, d=None),
            AutocompleteItem(k="iphone 12 pro max", i=3, d=None),
            AutocompleteItem(k="iphone 11 pro", i=3, d=None),
            AutocompleteItem(k="iphone 12 pro", i=3, d=None),
            AutocompleteItem(k="iphone xr", i=3, d=None),
            AutocompleteItem(k="iphone 11 pro max", i=3, d=None),
            AutocompleteItem(k="iphone x", i=3, d=None),
            AutocompleteItem(k="iphone 12 mini", i=3, d=None),
            AutocompleteItem(k="iphone 8", i=3, d=None),
        ]
    )
    ```

## Response Models
::: pyskroutz.models.search
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3