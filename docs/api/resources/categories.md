## `get`
::: pyskroutz.categories.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get(88).execute()
    ```

=== "Response (pydantic object)"

    ```python
    CategoryRetrieve(
        category=CategoryItem(
            web_uri=HttpUrl(
                "https://skroutz.gr/c/88/ssd-sklhroi-diskoi.html",
                scheme="https",
                host="skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/c/88/ssd-sklhroi-diskoi.html",
            ),
            id=88,
            name="SSD Σκληροί Δίσκοι",
            children_count=0,
            image_url=HttpUrl(
                "https://d.scdn.gr/ds/categories/88/20171113120930_4a77e901.jpeg",
                scheme="https",
                host="d.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/categories/88/20171113120930_4a77e901.jpeg",
            ),
            parent_id=1716,
            fashion=True,
            layout_mode="tiles",
            code="esoterikoi-sklhroi-diskoi",
            path="76,1269,22,27,46,1716,88",
            show_specifications=True,
            manufacturer_title="Κατασκευαστές",
        )
    )
    ```

## `get_parent`
::: pyskroutz.categories.get_parent
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get_parent(88).execute()
    ```

=== "Response (pydantic object)"

    ```python
    CategoryRetrieve(
        category=CategoryItem(
            web_uri=HttpUrl(
                "https://skroutz.gr/c/1716/esoterikoi_sklhroi_diskoi.html",
                scheme="https",
                host="skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/c/1716/esoterikoi_sklhroi_diskoi.html",
            ),
            id=1716,
            name="Εσωτερικοί Σκληροί Δίσκοι",
            children_count=2,
            image_url=HttpUrl(
                "https://b.scdn.gr/ds/categories/1716/20171113121535_f0cdd20f.jpeg",
                scheme="https",
                host="b.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/categories/1716/20171113121535_f0cdd20f.jpeg",
            ),
            parent_id=46,
            fashion=True,
            layout_mode="tiles",
            code="esoterikoi_sklhroi_diskoi",
            path="76,1269,22,27,46,1716",
            show_specifications=False,
            manufacturer_title="Κατασκευαστές",
        )
    )
    ```

## `get_root`
::: pyskroutz.categories.get_root
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get_root().execute()
    ```

=== "Response (pydantic object)"

    ```python
    CategoryRetrieve(
        category=CategoryItem(
            web_uri=HttpUrl(
                "https://skroutz.gr/c/76/skroutz.html",
                scheme="https",
                host="skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/c/76/skroutz.html",
            ),
            id=76,
            name="Skroutz",
            children_count=8,
            image_url=HttpUrl(
                "https://a.scdn.gr/ds/categories/76/76.jpg
                scheme="https",
                host="a.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/categories/76/76.jpg",
            ),
            parent_id=0,
            fashion=True,
            layout_mode="tiles",
            code="skroutz",
            path="76",
            show_specifications=False,
            manufacturer_title="Κατασκευαστές",
        )
    )
    ```

## `list_children`
::: pyskroutz.categories.list_children
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).list_children(252).execute()
    ```

=== "Response (pydantic object)"

    ```python
    CategoryList(
        categories=[
            CategoryItem(
                web_uri=HttpUrl(
                    "https://skroutz.gr/c/283/gynaikeia-rouxa.html",
                    scheme="https",
                    host="skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/c/283/gynaikeia-rouxa.html",
                ),
                id=283,
                name="Γυναικεία Ρούχα",
                children_count=26,
                image_url=HttpUrl(
                    "https://c.scdn.gr/ds/categories/283/20201104173829_801473e1.jpeg",
                    scheme="https",
                    host="c.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/ds/categories/283/20201104173829_801473e1.jpeg",
                ),
                parent_id=252,
                fashion=True,
                layout_mode="tiles",
                code="gynaikeia-endysh",
                path="76,274,252,283",
                show_specifications=False,
                manufacturer_title="Κατασκευαστές",
            ),
            CategoryItem(
                web_uri=HttpUrl(
                    "https://skroutz.gr/c/372/gynaikeia-ypodhmata.html",
                    scheme="https",
                    host="skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/c/372/gynaikeia-ypodhmata.html",
                ),
                id=372,
                name="Γυναικεία Παπούτσια",
                children_count=17,
                image_url=HttpUrl(
                    "https://c.scdn.gr/ds/categories/372/20201103153126_32f1759a.jpeg",
                    scheme="https",
                    host="c.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/ds/categories/372/20201103153126_32f1759a.jpeg",
                ),
                parent_id=252,
                fashion=True,
                layout_mode="tiles",
                code="gynaikeia-ypodhmata",
                path="76,274,252,372",
                show_specifications=False,
                manufacturer_title="Brands",
            ),
            CategoryItem(
                web_uri=HttpUrl(
                    "https://skroutz.gr/c/281/gynakeia-aksesouar-endyshs-ypo.html",
                    scheme="https",
                    host="skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/c/281/gynakeia-aksesouar-endyshs-ypo.html",
                ),
                id=281,
                name="Γυναικεία Αξεσουάρ",
                children_count=3,
                image_url=HttpUrl(
                    "https://b.scdn.gr/ds/categories/281/20200811151908_c187ba11.jpeg",
                    scheme="https",
                    host="b.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/ds/categories/281/20200811151908_c187ba11.jpeg",
                ),
                parent_id=252,
                fashion=True,
                layout_mode="tiles",
                code="gynakeia-aksesouar-endyshs-ypo",
                path="76,274,252,281",
                show_specifications=False,
                manufacturer_title="Κατασκευαστές",
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=25, total_pages=1, total_results=3),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `get_specifications`
::: pyskroutz.categories.get_specifications
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get_specifications(40, include_group=True).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SpecificationList(
        groups=[
            GroupItem(id=165, name="Βασικά Χαρακτηριστικά", order=0),
            GroupItem(id=167, name="Επεξεργαστής Μνήμη ", order=5),
            GroupItem(id=2164, name="Οθόνη", order=10),
            GroupItem(id=2163, name="Κάμερα", order=15),
            GroupItem(id=168, name="Δίκτυο &#38; Συνδεσιμότητα", order=20),
            GroupItem(id=1957, name="Μπαταρία", order=25),
            GroupItem(id=2166, name="Ειδικά Χαρακτηριστικά", order=30),
            GroupItem(id=170, name="Μέγεθος &#38; Βάρος", order=35),
        ],
        specifications=[
            SpecificationItem(id=1792, name="Τύπος Κινητού", values=[], order=5, unit=""),
            SpecificationItem(id=906, name="SIM", values=[], order=10, unit=""),
            SpecificationItem(
                id=575, name="Λειτουργικό Σύστημα", values=[], order=20, unit=""
            ),
            SpecificationItem(
                id=1528, name="Έτος Κυκλοφορίας", values=[], order=30, unit=""
            ),
            SpecificationItem(id=13192, name="Χρώμα", values=[], order=40, unit=""),
            SpecificationItem(
                id=5485, name="Ισχύς Βασικού Επεξεργαστή", values=[], order=2, unit="GHz"
            ),
            SpecificationItem(
                id=1424, name="Πυρήνες Επεξεργαστή", values=[], order=5, unit=""
            ),
            SpecificationItem(
                id=6859, name="Μοντέλο Επεξεργαστή", values=[], order=20, unit=""
            ),
            SpecificationItem(id=5455, name="RAM", values=[], order=40, unit="GB"),
            SpecificationItem(id=579, name="Χωρητικότητα", values=[], order=50, unit="GB"),
            SpecificationItem(id=580, name="Card Slot", values=[], order=55, unit=""),
            SpecificationItem(id=1526, name="Μέγεθος", values=[], order=5, unit='"'),
            SpecificationItem(id=1522, name="Ανάλυση", values=[], order=10, unit="pixels"),
            SpecificationItem(id=6226, name="Τύπος", values=[], order=20, unit=""),
            SpecificationItem(id=1530, name="Χειρισμός", values=[], order=50, unit=""),
            SpecificationItem(id=9801, name="Πίσω Κάμερα", values=[], order=5, unit=""),
            SpecificationItem(
                id=21036, name="Φακοί Πίσω Κάμερας", values=[], order=10, unit=""
            ),
            SpecificationItem(
                id=6228, name="Βίντεο Πίσω Κάμερας", values=[], order=20, unit=""
            ),
            SpecificationItem(
                id=2067, name="Flash Πίσω Κάμερας", values=[], order=25, unit=""
            ),
            SpecificationItem(
                id=21037, name="Φακοί Selfie Κάμερας", values=[], order=30, unit=""
            ),
            SpecificationItem(id=4321, name="Δίκτυο Σύνδεσης", values=[], order=0, unit=""),
            SpecificationItem(id=1521, name="Συνδεσιμότητα", values=[], order=10, unit=""),
            SpecificationItem(
                id=1426, name="Δείκτης SAR (Head)", values=[], order=20, unit="W/kg"
            ),
            SpecificationItem(
                id=3737, name="Χωρητικότητα", values=[], order=10, unit="mAh"
            ),
            SpecificationItem(id=3738, name="Αποσπώμενη", values=[], order=20, unit=""),
            SpecificationItem(
                id=5449, name="Γρήγορη Φόρτιση", values=[], order=30, unit=""
            ),
            SpecificationItem(
                id=19435, name="Ισχύς Φόρτισης", values=[], order=40, unit="W"
            ),
            SpecificationItem(
                id=5450, name="Ασύρματη Φόρτιση", values=[], order=50, unit=""
            ),
            SpecificationItem(
                id=601, name="Διάρκεια Αναμονής", values=[], order=70, unit="hrs"
            ),
            SpecificationItem(
                id=602, name="Διάρκεια Ομιλίας", values=[], order=80, unit="hrs"
            ),
            SpecificationItem(id=4315, name="Προστασία", values=[], order=5, unit=""),
            SpecificationItem(
                id=5875, name="Πιστοποίηση Προστασίας", values=[], order=20, unit=""
            ),
            SpecificationItem(id=4316, name="Αισθητήρες", values=[], order=30, unit=""),
            SpecificationItem(
                id=7194, name="Δακτυλικό Αποτύπωμα", values=[], order=50, unit=""
            ),
            SpecificationItem(id=603, name="Διαστάσεις", values=[], order=5, unit="mm"),
            SpecificationItem(id=604, name="Βάρος", values=[], order=10, unit="gr"),
        ],
    )
    ```

## `get_manufacturers`
::: pyskroutz.categories.get_manufacturers
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get_manufacturers(2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SpecificationList(groups=None, specifications=None)
    ```

## `get_favorites`
::: pyskroutz.categories.get_favorites
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.categories(client).get_favorites(40).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SpecificationList(groups=None, specifications=None)
    ```

## Response Models
::: pyskroutz.models.categories
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3