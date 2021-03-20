## `list`
::: pyskroutz.skus.list
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).list(40, per=1).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SkuList(
        skus=[
            SkuItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/s/24678558/Xiaomi-Poco-X3-NFC-128GB-Shadow-Gray.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/s/24678558/Xiaomi-Poco-X3-NFC-128GB-Shadow-Gray.html",
                ),
                price_max=349.0,
                price_min=211.0,
                reviewable=True,
                reviews_count=499,
                reviewscore=4.6994,
                shop_count=58,
                id=24678558,
                name="Poco X3 NFC (128GB) Shadow Gray",
                ean="",
                pn=None,
                display_name="Xiaomi Poco X3 NFC (128GB) Shadow Gray",
                category_id=40,
                first_product_shop_info=None,
                click_url=None,
                plain_spec_summary='Μοντέλο: 2020, Οθόνη: IPS 6.67", RAM: 6GB, 5160mAh',
                manufacturer_id=15053,
                future=False,
                virtual=False,
                images=ImageItemBase(
                    alternatives=[
                        HttpUrl(
                            "https://c.scdn.gr/images/sku_images/038039/38039081/20210128121207_45d0a621.jpeg",
                            scheme="https",
                            host="c.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039081/20210128121207_45d0a621.jpeg",
                        ),
                        HttpUrl(
                            "https://c.scdn.gr/images/sku_images/038039/38039103/20210128121216_efae4e2e.jpeg",
                            scheme="https",
                            host="c.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039103/20210128121216_efae4e2e.jpeg",
                        ),
                        HttpUrl(
                            "https://b.scdn.gr/images/sku_images/038039/38039116/20210128121222_9cebddfa.jpeg",
                            scheme="https",
                            host="b.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039116/20210128121222_9cebddfa.jpeg",
                        ),
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/038039/38039133/20210128121228_89277651.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039133/20210128121228_89277651.jpeg",
                        ),
                        HttpUrl(
                            "https://a.scdn.gr/images/sku_images/034464/34464291/20200916101703_864fbeac.jpeg",
                            scheme="https",
                            host="a.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/034464/34464291/20200916101703_864fbeac.jpeg",
                        ),
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/034464/34464358/20200916101740_f7680384.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/034464/34464358/20200916101740_f7680384.jpeg",
                        ),
                        HttpUrl(
                            "https://a.scdn.gr/images/sku_images/038039/38039162/20210128121240_95e93f54.jpeg",
                            scheme="https",
                            host="a.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039162/20210128121240_95e93f54.jpeg",
                        ),
                        HttpUrl(
                            "https://b.scdn.gr/images/sku_images/038039/38039177/20210128121245_36c27daa.jpeg",
                            scheme="https",
                            host="b.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039177/20210128121245_36c27daa.jpeg",
                        ),
                        HttpUrl(
                            "https://c.scdn.gr/images/sku_images/038039/38039190/20210128121249_621be65d.jpeg",
                            scheme="https",
                            host="c.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039190/20210128121249_621be65d.jpeg",
                        ),
                        HttpUrl(
                            "https://b.scdn.gr/images/sku_images/038039/38039207/20210128121253_19aaa6af.jpeg",
                            scheme="https",
                            host="b.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039207/20210128121253_19aaa6af.jpeg",
                        ),
                        HttpUrl(
                            "https://a.scdn.gr/images/sku_images/038039/38039219/20210128121256_a668d463.jpeg",
                            scheme="https",
                            host="a.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039219/20210128121256_a668d463.jpeg",
                        ),
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/038039/38039256/20210128121302_d8fa9dde.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039256/20210128121302_d8fa9dde.jpeg",
                        ),
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/038039/38039266/20210128121306_e71d0c4f.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/038039/38039266/20210128121306_e71d0c4f.jpeg",
                        ),
                        HttpUrl(
                            "https://a.scdn.gr/images/sku_images/034464/34464319/20200916101718_bbda4f45.jpeg",
                            scheme="https",
                            host="a.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/034464/34464319/20200916101718_bbda4f45.jpeg",
                        ),
                    ],
                    main=HttpUrl(
                        "https://a.scdn.gr/images/sku_main_images/024678/24678558/medium_20200916101811_xiaomi_poco_x3_nfc.jpeg",
                        scheme="https",
                        host="a.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/024678/24678558/medium_20200916101811_xiaomi_poco_x3_nfc.jpeg",
                    ),
                ),
                favorited=None,
                comparable=True,
                name_source="display_name",
            )
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods={
                "popularity_desc": "Δημοτικότητα",
                "pricevat_asc": "Αύξουσα τιμή",
                "pricevat_desc": "Φθίνουσα τιμή",
                "reviews_desc": "Βαθμολογία",
            },
            pagination=PaginationItem(page=1, per=1, total_pages=1636, total_results=1636),
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
        available_filters=None,
    )
    ```

## `get`
::: pyskroutz.skus.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).get(3443837).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SkuRetrieve(
        sku=SkuItem(
            web_uri=HttpUrl(
                "https://www.skroutz.gr/s/3443837/Frezyderm-Hydrating-Restructuring-Moisturizing-Plus-30-Cream-50ml.html",
                scheme="https",
                host="www.skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/s/3443837/Frezyderm-Hydrating-Restructuring-Moisturizing-Plus-30-Cream-50ml.html",
            ),
            price_max=26.97,
            price_min=15.35,
            reviewable=True,
            reviews_count=94,
            reviewscore=4.29787,
            shop_count=187,
                id=3443837,
            name="Hydrating & Restructuring Moisturizing Plus 30+ Cream 50ml",
            ean="",
            pn="",
            display_name="Frezyderm Hydrating & Restructuring Moisturizing Plus 30+ Cream 50ml",
            category_id=835,
            first_product_shop_info=None,
            click_url=None,
            plain_spec_summary="Ενυδάτωση, Επιδερμίδα: Ξηρή, 24ωρη, 30+",
            manufacturer_id=7444,
            future=False,
            virtual=False,
            images=ImageItemBase(
                alternatives=[
                    HttpUrl(
                        "https://d.scdn.gr/images/sku_images/041132/41132768/20210308161228_0f63e688.jpeg",
                        scheme="https",
                        host="d.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_images/041132/41132768/20210308161228_0f63e688.jpeg",
                    ),
                    HttpUrl(
                        "https://c.scdn.gr/images/sku_images/041132/41132763/20210308161218_f8597bac.jpeg",
                        scheme="https",
                        host="c.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_images/041132/41132763/20210308161218_f8597bac.jpeg",
                    ),
                ],
                main=HttpUrl(
                    "https://a.scdn.gr/images/sku_main_images/003443/3443837/medium_20210308161209_frezyderm_hydrating_restructuring_moisturizing_plus_30_cream_50ml.jpeg",
                    scheme="https",
                    host="a.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/images/sku_main_images/003443/3443837/medium_20210308161209_frezyderm_hydrating_restructuring_moisturizing_plus_30_cream_50ml.jpeg",
                ),
            ),
            favorited=None,
            comparable=True,
            name_source="display_name",
        )
    )
    ```

## `get_similar`

::: pyskroutz.skus.get_similar
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).get_similar(3443837, per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    SkuList(
        skus=[
            SkuItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/s/4509801/Frezyderm-Long-Lasting-Hydrating-Moisturizing-24H-Face-20-Light-Cream-50ml.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/s/4509801/Frezyderm-Long-Lasting-Hydrating-Moisturizing-24H-Face-20-Light-Cream-50ml.html",
                ),
                price_max=22.67,
                price_min=12.45,
                reviewable=True,
                reviews_count=127,
                reviewscore=4.40945,
                shop_count=190,
                id=4509801,
                name="Long Lasting Hydrating Moisturizing 24H Face 20+ Light Cream 50ml",
                ean="",
                pn="",
                display_name="Frezyderm Long Lasting Hydrating Moisturizing 24H Face 20+ Light Cream 50ml",
                category_id=835,
                first_product_shop_info=None,
                click_url=None,
                plain_spec_summary="Ενυδάτωση, Επιδερμίδα: Ξηρή, 24ωρη, 20+",
                manufacturer_id=7444,
                future=False,
                virtual=False,
                images=ImageItemBase(
                    alternatives=[
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/041132/41132806/20210308161332_7fb7c717.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/041132/41132806/20210308161332_7fb7c717.jpeg",
                        ),
                        HttpUrl(
                            "https://d.scdn.gr/images/sku_images/041132/41132825/20210308161343_a19e16a7.jpeg",
                            scheme="https",
                            host="d.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/041132/41132825/20210308161343_a19e16a7.jpeg",
                        ),
                    ],
                    main=HttpUrl(
                        "https://a.scdn.gr/images/sku_main_images/004509/4509801/medium_20210308161325_frezyderm_long_lasting_hydrating_moisturizing_24h_face_20_light_cream_50ml.jpeg",
                        scheme="https",
                        host="a.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/004509/4509801/medium_20210308161325_frezyderm_long_lasting_hydrating_moisturizing_24h_face_20_light_cream_50ml.jpeg",
                    ),
                ),
                favorited=None,
                comparable=True,
                name_source="display_name",
            ),
            SkuItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/s/5246308/La-Roche-Posay-Hydraphase-Intense-Legere-50ml.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/s/5246308/La-Roche-Posay-Hydraphase-Intense-Legere-50ml.html",
                ),
                price_max=31.15,
                price_min=12.16,
                reviewable=True,
                reviews_count=134,
                reviewscore=4.42537,
                shop_count=167,
                id=5246308,
                name="Hydraphase Intense Legere 50ml",
                ean="",
                pn="",
                display_name="La Roche Posay Hydraphase Intense Legere 50ml",
                category_id=835,
                first_product_shop_info=None,
                click_url=None,
                plain_spec_summary="Ενυδάτωση, Επιδερμίδα: Κανονική/Μικτή, 24ωρη, Για Όλες τις Ηλικίες",
                manufacturer_id=7415,
                future=False,
                virtual=False,
                images=ImageItemBase(
                    alternatives=[
                        HttpUrl(
                            "https://b.scdn.gr/images/sku_images/017681/17681567/20170808130043_b68e00bd.jpeg",
                            scheme="https",
                            host="b.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/017681/17681567/20170808130043_b68e00bd.jpeg",
                        ),
                        HttpUrl(
                            "https://c.scdn.gr/images/sku_images/018331/18331470/20171017094906_5bf87396.jpeg",
                            scheme="https",
                            host="c.scdn.gr",
                            tld="gr",
                            host_type="domain",
                            path="/images/sku_images/018331/18331470/20171017094906_5bf87396.jpeg",
                        ),
                    ],
                    main=HttpUrl(
                        "https://a.scdn.gr/images/sku_main_images/005246/5246308/medium_20171017094906_la_roche_posay_hydraphase_intense_legere_50ml.jpeg",
                        scheme="https",
                        host="a.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/005246/5246308/medium_20171017094906_la_roche_posay_hydraphase_intense_legere_50ml.jpeg",
                    ),
                ),
                favorited=None,
                comparable=True,
                name_source="display_name",
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=10, total_results=19),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
        available_filters=None,
    )
    ```

## `get_reviews`

::: pyskroutz.skus.get_reviews
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).get_reviews(3783654, include_meta='sku_rating_breakdown', per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ReviewList(
        reviews=[
            ReviewItem(
                id=1001458,
                user_id=2778937,
                review="Λοιπόν έχω το iPhone 5s εδώ και τρία με τέσσερα χρόνια. Το ένα που το πήρα από την νονά μου μεταχειρισμένο πέντε χρόνια πήγαινε τέλεια. Μετά καταλάθος το βραχυκύκλωσα και έτσι όταν πήρε ο νονός μου το iPhone 7 μου έδωσε το 5s του. Έχω να πω ότι είναι πολύ καλό κινητό αν και δεν υπάρχει στην αγορά και επίσης δεν υποστηρίζεται από την Apple αλλά άμα το έχεις από πριν δεν νομίζω ότι χρειάζεται να το αλλάξεις. Βέβαια το κακό είναι ότι η μπαταρία του είναι πολύ μικρή, κρατάει πολύ λίγο. Όμως δεν ξέρω πως γίνεται αυτό: της νονάς μου που ήταν και πέντε χρονών άντεχε η μπαταρία του πάρα πολύ μετά όμως όταν πήρα του νονού μου η μπαταρία ήταν χάλια όπως και τώρα δεν ξέρω τι έχει πάθει. Πάντως αν είσαι φαν του Among us πρέπει να αλλάξεις κινητό ή να μην μπεις στον κόπο να το αγοράσεις δεν παίζει among us. Για εμένα η φότο και τα βίντεο είναι ικανοποιητικά! Επίσης έχει και Jack και μπορείς να ακούς με οποιαδήποτε ακουστικά! Είμαι ικανοποιημένος ακόμα και με τα 16gb.",
                rating=4,
                created_at=datetime.datetime(
                    2021,
                    1,
                    26,
                    10,
                    0,
                    25,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)),
                ),
                demoted=False,
                votes_count=3,
                helpful_votes_count=3,
                voted=False,
                flagged=False,
                helpful=False,
                sentiments=SentimentItem(
                    positive=["Φωτογραφίες", "Καταγραφή Video", "Μουσική", "Ταχύτητα"],
                    mediocre=["Ανάλυση οθόνης"],
                ),
            ),
            ReviewItem(
                id=930564,
                user_id=1423160,
                review="Κατά την γνώμη είναι μακράν το ποιο καλό και το ποιο θρυλικό iPhone που έχει βγει ποτέ μαζί με το 6s",
                rating=5,
                created_at=datetime.datetime(
                    2020,
                    12,
                    14,
                    23,
                    24,
                    20,
                    tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)),
                ),
                demoted=False,
                votes_count=2,
                helpful_votes_count=1,
                voted=False,
                flagged=False,
                helpful=False,
                sentiments=SentimentItem(
                    positive=[
                        "Ποιότητα κλήσης",
                        "Μουσική",
                        "Ταχύτητα",
                        "Σχέση ποιότητας τιμής",
                        "Ανάλυση οθόνης",
                    ],
                    mediocre=["Φωτογραφίες", "Καταγραφή Video"],
                ),
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=271, total_results=541),
            personalization=None,
            sku_rating_breakdown=[
                SkuRatingBreakDownItem(count=342, percentage=63, star=5),
                SkuRatingBreakDownItem(count=123, percentage=23, star=4),
                SkuRatingBreakDownItem(count=32, percentage=6, star=3),
                SkuRatingBreakDownItem(count=14, percentage=3, star=2),
                SkuRatingBreakDownItem(count=30, percentage=6, star=1),
            ],
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `vote_review`

::: pyskroutz.skus.vote_review
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).vote_review(3982592, 21943, True).execute()
    ```

=== "Response (pydantic object)"

    ```python
    VoteRetrieve(sku_review_vote=None)
    ```

## `flag_review`

::: pyskroutz.skus.flag_review
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).flag_review(9783213, 240896, "spam").execute()
    ```

=== "Response (pydantic object)"

    ```python
    VoteRetrieve(sku_review_vote=None)
    ```

## `get_review_form`

::: pyskroutz.skus.get_review_form
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.skus(client).get_review_form(3783654).execute()
    ```

=== "Response (pydantic object)"

    ```python
    ReviewFormRetrieve(
        review_form=ReviewFormItem(
            requires_body=False,
            questions=[
                QuestionItem(
                    text="Πως χρησιμοποιείς το κινητό σου τηλέφωνο;",
                    type="profiling_multiple",
                    answers=[
                        AnswerItem(id=546, text="Κλήσεις"),
                        AnswerItem(id=547, text="Social Media"),
                        AnswerItem(id=548, text="Φωτογραφίες - Video"),
                        AnswerItem(id=549, text="Browsing"),
                        AnswerItem(id=550, text="Παιχνίδια"),
                        AnswerItem(id=551, text="Μουσική"),
                    ],
                ),
                QuestionItem(
                    text="Μιλάς και ακούγεσαι καθαρά κατά την κλήση;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=504, text="Ναι"),
                        AnswerItem(id=505, text="Έτσι κι έτσι"),
                        AnswerItem(id=506, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Βγάζει καλές φωτογραφίες;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=507, text="Ναι"),
                        AnswerItem(id=508, text="Έτσι κι έτσι"),
                        AnswerItem(id=509, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Τραβάει καλής ποιότητας video;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=510, text="Ναι"),
                        AnswerItem(id=511, text="Έτσι κι έτσι"),
                        AnswerItem(id=512, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="To ηχείο έχει καλή ποιότητα για μουσική;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=537, text="Ναι"),
                        AnswerItem(id=538, text="Έτσι κι έτσι"),
                        AnswerItem(id=539, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Είναι γρήγορο κατά τη λειτουργία του;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=555, text="Ναι"),
                        AnswerItem(id=556, text="Έτσι κι έτσι"),
                        AnswerItem(id=557, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Αξίζει τα χρήματά του;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=561, text="Ναι"),
                        AnswerItem(id=562, text="Έτσι κι έτσι"),
                        AnswerItem(id=563, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Η οθόνη του έχει καλή ανάλυση;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=3944, text="Ναι"),
                        AnswerItem(id=3945, text="Έτσι κι έτσι"),
                        AnswerItem(id=3946, text="Όχι"),
                    ],
                ),
                QuestionItem(
                    text="Είναι ικανοποιητική η διάρκεια της μπαταρίας;",
                    type="eval_sentiment",
                    answers=[
                        AnswerItem(id=9448, text="Ναι"),
                        AnswerItem(id=9449, text="Έτσι κι έτσι"),
                        AnswerItem(id=9450, text="Όχι"),
                    ],
                ),
            ],
        )
    )

    ```

## Response Models
::: pyskroutz.models.skus
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3