## `get`
::: pyskroutz.shops.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.shops(client).get(452).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ShopRetrieve(
        shop=ShopItem(
            web_uri=HttpUrl(
                "https://skroutz.gr/m/452/Kotsovolos",
                scheme="https",
                host="skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/m/452/Kotsovolos",
            ),
            id=452,
            name="Kotsovolos",
            link=HttpUrl(
                "https://www.kotsovolos.gr/site/",
                scheme="https",
                host="www.kotsovolos.gr",
                tld="gr",
                host_type="domain",
                path="/site/",
            ),
            phone="2102899999",
            image_url=HttpUrl(
                "https://a.scdn.gr/ds/shops/logos/452/mid_20200304165249_98e5ec3a.jpeg",
                scheme="https",
                host="a.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/shops/logos/452/mid_20200304165249_98e5ec3a.jpeg",
            ),
            thumbshot_url=HttpUrl(
                "https://d.scdn.gr/ds/shops/screenshots/452/20200707083048_bce89826.jpeg",
                scheme="https",
                host="d.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/shops/screenshots/452/20200707083048_bce89826.jpeg",
            ),
            reviews_count=1819,
            latest_reviews_count=800,
            review_score=0.6,
            payment_methods=PaymentMethodsItem(
                credit_card=True, paypal=False, bank=True, spot_cash=True, installments=None
            ),
            shipping=ShippingItem(
                free=False,
                free_from=0,
                free_from_info="",
                min_price="",
                shipping_cost_enabled=False,
            ),
            extra_info=ExtraInfoItem(time_on_platform="3+ χρόνια", orders_per_week="1000+"),
            top_positive_reasons=[],
        )
    )
    ```

## `get`
::: pyskroutz.shops.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.shops(client).get(452).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ShopRetrieve(
        shop=ShopItem(
            web_uri=HttpUrl(
                "https://skroutz.gr/m/452/Kotsovolos",
                scheme="https",
                host="skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/m/452/Kotsovolos",
            ),
            id=452,
            name="Kotsovolos",
            link=HttpUrl(
                "https://www.kotsovolos.gr/site/",
                scheme="https",
                host="www.kotsovolos.gr",
                tld="gr",
                host_type="domain",
                path="/site/",
            ),
            phone="2102899999",
            image_url=HttpUrl(
                "https://a.scdn.gr/ds/shops/logos/452/mid_20200304165249_98e5ec3a.jpeg",
                scheme="https",
                host="a.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/shops/logos/452/mid_20200304165249_98e5ec3a.jpeg",
            ),
            thumbshot_url=HttpUrl(
                "https://d.scdn.gr/ds/shops/screenshots/452/20200707083048_bce89826.jpeg",
                scheme="https",
                host="d.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/shops/screenshots/452/20200707083048_bce89826.jpeg",
            ),
            reviews_count=1848,
            latest_reviews_count=826,
            review_score=0.4,
            payment_methods=PaymentMethodsItem(
                credit_card=True, paypal=False, bank=True, spot_cash=True, installments=None
            ),
            shipping=ShippingItem(
                free=False,
                free_from=0,
                free_from_info="",
                min_price="",
                shipping_cost_enabled=False,
            ),
            extra_info=ExtraInfoItem(time_on_platform="3+ χρόνια", orders_per_week="1000+"),
            top_positive_reasons=[],
        )
    )
    ```

## Response Models
::: pyskroutz.models.shops
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3