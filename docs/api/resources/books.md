## `get`
::: pyskroutz.books.get
    rendering:
      show_root_toc_entry: false

**Example**

Retrieve the book with ID: `242327`.

=== "Request"

    ```python
    pyskroutz.books(client).get(242327).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BooksRetrieve(
        book=BookItem(
            web_uri=HttpUrl(
                "https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
                scheme="https",
                host="www.skroutz.gr",
                tld="gr",
                host_type="domain",
                path="/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
            ),
            price_max=12.96,
            price_min=6.61,
            reviewable=True,
            reviews_count=15,
            reviewscore=4.93333,
            shop_count=42,
            id=242327,
            name="Ο Χάρι Πότερ και η φιλοσοφική λίθος",
            main_author_id=385,
            main_author="J. K. Rowling",
            images=ImageItemBase(
                alternatives=None,
                main=HttpUrl(
                    "https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                    scheme="https",
                    host="b.scdn.gr",
                    tld="gr",
                    host_type="domain",
                    path="/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                ),
            ),
        )
    )
    ```

## `get_details`
::: pyskroutz.books.get_details
    rendering:
      show_root_toc_entry: false

**Example**

Get details for the book with ID: `242327`.

=== "Request"

    ```python
    pyskroutz.books(client).get_details(242327).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BookDetailsRetrieve(
        book_details=BookDetailsItem(
            series="",
            cover="Μαλακό εξώφυλλο",
            pubyear="2001",
            pages=349,
            isbn="9602743484",
            shape="21×14",
            volume=None,
            ages=None,
            description="Ο Χάρι Πότερ είναι ένα αξιαγάπητο μικρό αγόρι που η μοίρα του επιφυλάσσει μια ζωή διαφορετική από των άλλων παιδιών της ηλικίας του. Χάνει τους γονείς του και αναγκάζεται να μείνει με το θείο, τη θεία του και τον κακομαθημένο ξάδελφό του. Καθώς τα χρόνια περνούν και ο Χάρι συνεχίζει να υποφέρει κοντά στους συγγενείς του, λαμβάνει μια επιστολή, με την οποία τον καλούν να παρουσιαστεί στη Σχολή Χόγκουαρτς, μια σχολή αλλιώτικη από τις άλλες, σ' έναν κόσμο αλλιώτικο. Έτσι, αρχίζουν οι περιπέτειες του μικρού Χάρι. Μαζί του, παρακολουθούμε κι εμείς μαθήματα ασυνήθιστα, διασκεδαστικά παιχνίδια, πολύτιμες σχέσεις φιλίας και αλληλοϋποστήριξης, καθώς ο Χάρι προσπαθεί να προστατέψει τον κόσμο από τον κίνδυνο που τον απειλεί. Η Αγγλίδα συγγραφέας μάς χαρίζει ένα ευφάνταστο, ξεκαρδιστικό, απολαυστικό, αστείο, πρωτότυπο βιβλίο για όλες τις ηλικίες. Μεγάλοι και μικροί θα μαγευτούν από τις περιπέτειες του Χάρι Πότερ. Οι διάλογοι είναι έξυπνοι και διασκεδαστικοί, οι ήρωες κατεργάρηδες αλλά αξιαγάπητοι. Πρόκειται για ένα συναρπαστικό βιβλίο που θα λατρέψουν όλοι οι αναγνώστες.",
        )
    )
    ```

## `get_author`
::: pyskroutz.books.get_author
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_author(385).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BookAuthorRetrieve(
        author=BookAuthorItem(
            id=385,
            name="J. K. Rowling",
            bio='Η Joanne K. Rowling (Τζόαν Ρόουλινγκ) γεννήθηκε στο Μπρίστολ το 1965. Άρχισε να γράφει την ιστορία του "Χάρι Πότερ" σε ώρες πολύ δύσκολες. Ο "Χάρι Πότερ" εξελίχθηκε σε βιβλίο-φαινόμενο. Τα δικαιώματα μετάφρασης πουλήθηκαν σε ολόκληρο τον κόσμο και τα βραβεία ακολούθησαν το ένα το άλλο: τρία βραβεία Νεστλέ-Σμάρτις, Γκάρντιαν, Σέφιλντ, ΑΒΒΥ, Whitbread, Locus, Hugo, κ.ά., ενώ η συγγραφέας ανακηρύχτηκε Βρετανίδα Συγγραφέας της Χρονιάς το 2000 και τιμήθηκε για το σύνολο του έργου της το 2008. Οι ταινίες με ήρωα τον "Χάρι Πότερ" έκαναν επίσης ρεκόρ εισιτηρίων όπου προβλήθηκαν. Τα βιβλία του "Χάρι Πότερ" πούλησαν περισσότερα από 250 εκατομμύρια αντίτυπα σε όλο τον κόσμο, έχοντας μεταφραστεί σε 60 γλώσσες. H επιτυχία, μάλιστα, τη συνοδεύει, μετά την ολοκλήρωση της σειράς, και στο πρώτο της μυθιστόρημα για ενηλίκους, με τίτλο "The Casual Vacancy", 2012 (ελλ. έκδ. "Ένας ξαφνικός θάνατος"), καθώς και στο πρώτο της αστυνομικό μυθιστόρημα με ήρωα τον ντετέκτιβ Κόρμοραν Στράικ, "The Cuckoo\'s Calling" ("Το κάλεσμα του κούκου", 2013), που εξέδωσε με το ψευδώνυμο Ρόμπερτ Γκαλμπρέιθ. Στηρίζει πολλούς φιλανθρωπικούς σκοπούς μέσω του Φιλανθρωπικού Καταπιστεύματος Volant και έχει ιδρύσει το Lumos, που στόχο έχει να βελτιώσει τη ζωή των απόρων -και όχι μόνο- παιδιών. Για περισσότερες πληροφορίες μπορείτε να επισκεφθείτε την προσωπική ιστοσελίδα της συγγραφέως: www.jkrowling.com, καθώς και την ιστοσελίδα: www.volanttrust.com',
            image=HttpUrl(
                "https://d.scdn.gr/ds/books/authors/385/20160721172728_1f8fd6c7.jpeg",
                scheme="https",
                host="d.scdn.gr",
                tld="gr",
                host_type="domain",
                path="/ds/books/authors/385/20160721172728_1f8fd6c7.jpeg",
            ),
        )
    )
    ```

## `get_author_books`
::: pyskroutz.books.get_author_books
    rendering:
      show_root_toc_entry: false

**Example**

Get the first two books from author with ID: `385`.

=== "Request"

    ```python
    pyskroutz.books(client).get_author_books(385, per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BooksList(
        books=[
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
                ),
                price_max=12.96,
                price_min=6.61,
                reviewable=True,
                reviews_count=15,
                reviewscore=4.93333,
                shop_count=42,
                id=242327,
                name="Ο Χάρι Πότερ και η φιλοσοφική λίθος",
                main_author_id=385,
                main_author="J. K. Rowling",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                        scheme="https",
                        host="b.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                    ),
                ),
            ),
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/242082.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CE%BA%CE%AC%CE%BC%CE%B1%CF%81%CE%B1-%CE%BC%CE%B5-%CF%84%CE%B1-%CE%BC%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/242082.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CE%BA%CE%AC%CE%BC%CE%B1%CF%81%CE%B1-%CE%BC%CE%B5-%CF%84%CE%B1-%CE%BC%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC.html",
                ),
                price_max=14.4,
                price_min=9.94,
                reviewable=True,
                reviews_count=8,
                reviewscore=4.5,
                shop_count=44,
                id=242082,
                name="Ο Χάρι Πότερ και η κάμαρα με τα μυστικά",
                main_author_id=385,
                main_author="J. K. Rowling",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://a.scdn.gr/images/sku_main_images/000242/242082/medium_20181123130007_o_chari_poter_kai_i_kamara_me_ta_mystika.jpeg",
                        scheme="https",
                        host="a.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/000242/242082/medium_20181123130007_o_chari_poter_kai_i_kamara_me_ta_mystika.jpeg",
                    ),
                ),
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=11, total_results=21),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `get_similar_by_author`
::: pyskroutz.books.get_similar_by_author
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_similar_by_author(242327, per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BooksList(
        books=[
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/107865.%CE%9F%CE%B9-%CE%B9%CF%83%CF%84%CE%BF%CF%81%CE%AF%CE%B5%CF%82-%CF%84%CE%BF%CF%85-%CE%9C%CF%80%CE%B9%CE%BD%CF%84%CE%BB-%CF%84%CE%BF%CF%85-%CE%92%CE%AC%CF%81%CE%B4%CE%BF%CF%85.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/107865.%CE%9F%CE%B9-%CE%B9%CF%83%CF%84%CE%BF%CF%81%CE%AF%CE%B5%CF%82-%CF%84%CE%BF%CF%85-%CE%9C%CF%80%CE%B9%CE%BD%CF%84%CE%BB-%CF%84%CE%BF%CF%85-%CE%92%CE%AC%CF%81%CE%B4%CE%BF%CF%85.html",
                ),
                price_max=7.92,
                price_min=7.92,
                reviewable=True,
                reviews_count=0,
                reviewscore=0.0,
                shop_count=1,
                id=107865,
                name="Οι ιστορίες του Μπιντλ του Βάρδου",
                main_author_id=385,
                main_author="J. K. Rowling",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://d.scdn.gr/images/sku_main_images/000107/107865/medium_20160719175022_oi_istories_tou_mpintl_tou_vardou.jpeg",
                        scheme="https",
                        host="d.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/000107/107865/medium_20160719175022_oi_istories_tou_mpintl_tou_vardou.jpeg",
                    ),
                ),
            ),
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/121274.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%BF%CE%B9-%CE%BA%CE%BB%CE%AE%CF%81%CE%BF%CE%B9-%CF%84%CE%BF%CF%85-%CE%B8%CE%B1%CE%BD%CE%AC%CF%84%CE%BF%CF%85.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/121274.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%BF%CE%B9-%CE%BA%CE%BB%CE%AE%CF%81%CE%BF%CE%B9-%CF%84%CE%BF%CF%85-%CE%B8%CE%B1%CE%BD%CE%AC%CF%84%CE%BF%CF%85.html",
                ),
                price_max=15.5,
                price_min=10.32,
                reviewable=True,
                reviews_count=3,
                reviewscore=4.66667,
                shop_count=51,
                id=121274,
                name="Ο Χάρι Πότερ και οι κλήροι του θανάτου",
                main_author_id=385,
                main_author="J. K. Rowling",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://b.scdn.gr/images/sku_main_images/000121/121274/medium_20201103152340_o_chari_poter_kai_oi_kliroi_tou_thanatou.jpeg",
                        scheme="https",
                        host="b.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/000121/121274/medium_20201103152340_o_chari_poter_kai_oi_kliroi_tou_thanatou.jpeg",
                    ),
                ),
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=10, total_results=20),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `get_similar_by_author`
::: pyskroutz.books.get_similar_by_author
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_publisher(78).execute()
    ```

=== "Response (pydantic object)"

    ```python
    PublisherRetrieve(
        publisher=PublisherItem(
            id=78,
            name="Ψυχογιός",
            address="Τατοΐου 121 144 52 Μεταμόρφωση",
            email="info@psichogios.gr",
            website="www.psichogios.gr",
            fax="210 2819550",
            phone="210 2804800",
        )
    )
    ```

## `get_publisher_books`
::: pyskroutz.books.get_publisher_books
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_publisher_books(78, per=2).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BooksList(
        books=[
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html",
                ),
                price_max=12.96,
                price_min=6.61,
                reviewable=True,
                reviews_count=15,
                reviewscore=4.93333,
                shop_count=42,
                id=242327,
                name="Ο Χάρι Πότερ και η φιλοσοφική λίθος",
                main_author_id=385,
                main_author="J. K. Rowling",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                        scheme="https",
                        host="b.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg",
                    ),
                ),
            ),
            BookItem(
                web_uri=HttpUrl(
                    "https://www.skroutz.gr/books/16712787.%CE%97-%CE%B4%CE%B9%CE%BA%CE%AE-%CE%BC%CE%BF%CF%85-%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AE-%CE%BA%CE%BF%CF%85%CE%B6%CE%AF%CE%BD%CE%B1.html",
                    scheme="https",
                    host="www.skroutz.gr",
                    tld="gr",
                    host_type="domain",
                    path="/books/16712787.%CE%97-%CE%B4%CE%B9%CE%BA%CE%AE-%CE%BC%CE%BF%CF%85-%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AE-%CE%BA%CE%BF%CF%85%CE%B6%CE%AF%CE%BD%CE%B1.html",
                ),
                price_max=35.0,
                price_min=24.5,
                reviewable=True,
                reviews_count=5,
                reviewscore=4.8,
                shop_count=26,
                id=16712787,
                name="Η δική μου ελληνική κουζίνα",
                main_author_id=111086,
                main_author="Άκης Πετρετζίκης",
                images=ImageItemBase(
                    alternatives=None,
                    main=HttpUrl(
                        "https://b.scdn.gr/images/sku_main_images/016712/16712787/medium_20200219105637_i_diki_mou_elliniki_kouzina.jpeg",
                        scheme="https",
                        host="b.scdn.gr",
                        tld="gr",
                        host_type="domain",
                        path="/images/sku_main_images/016712/16712787/medium_20200219105637_i_diki_mou_elliniki_kouzina.jpeg",
                    ),
                ),
            ),
        ],
        meta=MetaItemBase(
            available_filters=None,
            order_by=None,
            order_by_methods=None,
            pagination=PaginationItem(page=1, per=2, total_pages=2030, total_results=4060),
            personalization=None,
            sku_rating_breakdown=None,
            sku_reviews_aggregation=None,
        ),
    )
    ```

## `get_book_categories`
::: pyskroutz.books.get_book_categories
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_book_categories().execute()
    ```

=== "Response (pydantic object)"

    ```python
    BookCategoriesList(
        categories=[
            BookCategory(id=38, name="Παιδικά", match_count=None),
            BookCategory(id=78, name="Λογοτεχνία", match_count=None),
            BookCategory(id=50, name="Ελεύθερος Χρόνος - Χόμπυ", match_count=None),
            BookCategory(id=150, name="Ψυχολογία", match_count=None),
            BookCategory(id=121, name="Επιστήμες", match_count=None),
            BookCategory(id=1, name="Σχολικά", match_count=None),
            BookCategory(id=23, name="Εκμάθηση Ξένων Γλωσσών", match_count=None),
            BookCategory(id=103, name="Τέχνες", match_count=None),
            BookCategory(id=120, name="Κόμικς", match_count=None),
            BookCategory(id=92, name="Θρησκείες - Μεταφυσική", match_count=None),
            BookCategory(id=156, name="Ιστορία", match_count=None),
            BookCategory(id=173, name="Κλασική Γραμματεία", match_count=None),
            BookCategory(id=177, name="Φιλοσοφία", match_count=None),
            BookCategory(id=178, name="Οικονομικά", match_count=None),
            BookCategory(id=183, name="Πολιτική", match_count=None),
            BookCategory(id=184, name="Λεξικά", match_count=None),
            BookCategory(id=197, name="Εκπαίδευση - Παιδαγωγικά", match_count=None),
            BookCategory(id=202, name="Γλώσσα - Φιλολογία", match_count=None),
            BookCategory(id=205, name="Δοκίμια", match_count=None),
            BookCategory(id=206, name="Περιοδικά", match_count=None),
        ]
    )
    ```

## `get_category`
::: pyskroutz.books.get_category
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_category(1857).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BookCategoryRetrieve(category=None)
    ```

## `get_category_books`
::: pyskroutz.books.get_category_books
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.books(client).get_category_books(1857).execute()
    ```

=== "Response (pydantic object)"

    ```python
    BooksList(books=None, meta=None)
    ```

## Response Models
::: pyskroutz.models.books
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3