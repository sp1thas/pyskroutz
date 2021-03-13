## `get`
::: pyskroutz.products.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.products(client).get(10296508).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ```

## `get_sku_products`
::: pyskroutz.products.get_sku_products
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.products(client).get_sku_products(242327).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ```

## `get_sku_products_grouped_cards`
::: pyskroutz.products.get_sku_products_grouped_cards
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.products(client).get_sku_products_grouped_cards(3783654).execute()
    ```

=== "Response (pydantic object)"

    ```python
    CardsList(
        product_cards=[],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=15, total_pages=0, total_results=0),
            personalization=PersonalizationItem(
                location=LocationItem(
                    address_id=None,
                    country_code="GR",
                    label="Αθήνα",
                    lat="37.975553",
                    lng="23.734902",
                    type="default",
                ),
                payment_method=PaymentMethodTypeItem(type={"spot_cash": "Αντικαταβολή"}),
            ),
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `get_personalization`
::: pyskroutz.products.get_personalization
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.products(client).get_personalization().execute()
    ```

=== "Response (pydantic object)"

    ```python
    ```

## Response Models
::: pyskroutz.models.products
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3