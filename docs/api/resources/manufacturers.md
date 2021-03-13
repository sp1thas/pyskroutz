## `get`
::: pyskroutz.manufacturers.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.manufacturers(client).get(12907).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ManufacturerRetrieve(
        manufacturer=ManufacturerItem(id=12907, name="Rapala", image_url=None)
    )
    ```

## `get_manufacturer_categories`
::: pyskroutz.manufacturers.get_manufacturer_categories
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.manufacturers(client).get_manufacturer_categories(12907).execute()
    ```

=== "Response (pydantic object)"

    ```python
    CategoryList(
        categories=[
            CategoryItem(
                web_uri=HttpUrl(
                    "https://skroutz.gr/c/3163/technita-dolomata.html",
                    scheme="https",
                    host="skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/c/3163/technita-dolomata.html",
                ),
                id=3163,
                name="Τεχνητά Δολώματα",
                children_count=0,
                image_url=HttpUrl(
                    "https://a.scdn.gr/ds/categories/3163/20190212130743_6f6338f8.jpeg",
                    scheme="https",
                    host="a.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/ds/categories/3163/20190212130743_6f6338f8.jpeg",
                ),
                parent_id=1421,
                fashion=True,
                layout_mode="tiles",
                code="technita-dolomata",
                path="76,255,1421,3163",
                show_specifications=False,
                manufacturer_title="Κατασκευαστές",
            ),
            CategoryItem(
                web_uri=HttpUrl(
                    "https://skroutz.gr/c/3203/tsantes-psarematos.html",
                    scheme="https",
                    host="skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/c/3203/tsantes-psarematos.html",
                ),
                id=3203,
                name="Τσάντες Ψαρέματος",
                children_count=0,
                image_url=HttpUrl(
                    "https://a.scdn.gr/ds/categories/3203/20190225100127_f2ee6b9d.jpeg",
                    scheme="https",
                    host="a.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/ds/categories/3203/20190225100127_f2ee6b9d.jpeg",
                ),
                parent_id=3167,
                fashion=True,
                layout_mode="tiles",
                code="tsantes-psarematos",
                path="76,255,1421,3167,3203",
                show_specifications=False,
                manufacturer_title="Κατασκευαστές",
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=7, total_results=13),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## Response Models
::: pyskroutz.models.manufacturers
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3