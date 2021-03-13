## `get`
::: pyskroutz.filters.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.filters(client).get(40, per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    FilterGroupsList(
        filter_groups=[
            FilterGroupsItem(
                id=75300,
                name="RAM",
                active=True,
                category_id=40,
                created_at=datetime.datetime(
                    2014,
                    12,
                    24,
                    19,
                    40,
                    50,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)),
                ),
                updated_at=datetime.datetime(
                    2019,
                    6,
                    27,
                    10,
                    36,
                    52,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=10800)),
                ),
                hint="",
                combined=False,
                filter_type=2,
            ),
            FilterGroupsItem(
                id=158086,
                name="Τύπος",
                active=True,
                category_id=40,
                created_at=datetime.datetime(
                    2018,
                    8,
                    3,
                    10,
                    25,
                    58,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=10800)),
                ),
                updated_at=datetime.datetime(
                    2019,
                    4,
                    25,
                    16,
                    44,
                    33,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=10800)),
                ),
                hint="",
                combined=False,
                filter_type=2,
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
::: pyskroutz.models.filters
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3