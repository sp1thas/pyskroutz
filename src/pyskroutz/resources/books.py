from typing import Optional

from .base import ApiResource
from ..models import books
from ..utils import fluent
from ..resources import PaginationParams


class Books(ApiResource):
    """This Class holds the group of Books related endpoints.
    More details in [category](https://developer.skroutz.gr/api/v3/category/) section.
    """

    ENDPOINT_PATH: str = "books"

    @fluent
    def get(self, id: int) -> None:
        """Retrieve a single Book

        Args:
            id: Book identifier

        Examples:
            Retrieve the book with ID: `242327`.

            >>> pyskroutz.books(client).get(242327).execute()

        <details>
            <summary>Response (as dictionary)</summary>
            <pre><code>
        {'book': {'id': 242327,
                  'images': {'alternatives': None,
                             'main': HttpUrl('https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg')},
                  'main_author': 'J. K. Rowling',
                  'main_author_id': 385,
                  'name': 'Ο Χάρι Πότερ και η φιλοσοφική λίθος',
                  'price_max': 12.96,
                  'price_min': 6.61,
                  'reviewable': True,
                  'reviews_count': 15,
                  'reviewscore': 4.93333,
                  'shop_count': 42,
                  'web_uri': HttpUrl('https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html')}}
            </code></pre>
        </details>

        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}",
            method="GET",
            model=books.BooksRetrieve,
        )

    @fluent
    def get_details(self, id: int) -> None:
        """Retrieve Book details

        Args:
            id: Book identifier.

        Examples:

            Get details for book with ID: `242327`.
            >>> pyskroutz.books(client).get_details(242327).execute()

            <details>
                <summary>Response (as dictionary)</summary>
                <pre><code>
            {'book_details': {'ages': None,
                              'cover': 'Μαλακό εξώφυλλο',
                              'description': 'Ο Χάρι Πότερ είναι ένα αξιαγάπητο μικρό '
                                             'αγόρι που η μοίρα του επιφυλάσσει μια ζωή '
                                             'διαφορετική από των άλλων παιδιών της '
                                             'ηλικίας του. Χάνει τους γονείς του και '
                                             'αναγκάζεται να μείνει με το θείο, τη θεία '
                                             'του και τον κακομαθημένο ξάδελφό του. Καθώς '
                                             'τα χρόνια περνούν και ο Χάρι συνεχίζει να '
                                             'υποφέρει κοντά στους συγγενείς του, λαμβάνει '
                                             'μια επιστολή, με την οποία τον καλούν να '
                                             'παρουσιαστεί στη Σχολή Χόγκουαρτς, μια σχολή '
                                             "αλλιώτικη από τις άλλες, σ' έναν κόσμο "
                                             'αλλιώτικο. Έτσι, αρχίζουν οι περιπέτειες του '
                                             'μικρού Χάρι. Μαζί του, παρακολουθούμε κι '
                                             'εμείς μαθήματα ασυνήθιστα, διασκεδαστικά '
                                             'παιχνίδια, πολύτιμες σχέσεις φιλίας και '
                                             'αλληλοϋποστήριξης, καθώς ο Χάρι προσπαθεί να '
                                             'προστατέψει τον κόσμο από τον κίνδυνο που '
                                             'τον απειλεί. Η Αγγλίδα συγγραφέας μάς '
                                             'χαρίζει ένα ευφάνταστο, ξεκαρδιστικό, '
                                             'απολαυστικό, αστείο, πρωτότυπο βιβλίο για '
                                             'όλες τις ηλικίες. Μεγάλοι και μικροί θα '
                                             'μαγευτούν από τις περιπέτειες του Χάρι '
                                             'Πότερ. Οι διάλογοι είναι έξυπνοι και '
                                             'διασκεδαστικοί, οι ήρωες κατεργάρηδες αλλά '
                                             'αξιαγάπητοι. Πρόκειται για ένα συναρπαστικό '
                                             'βιβλίο που θα λατρέψουν όλοι οι αναγνώστες.',
                              'isbn': '9602743484',
                              'pages': 349,
                              'pubyear': '2001',
                              'series': '',
                              'shape': '21×14',
                              'volume': None}}
                </code></pre>
            </details>
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/details",
            method="GET",
            model=books.BookDetailsRetrieve,
        )

    @fluent
    def get_author(self, id: int) -> None:
        """Retrieve Book Author

        Args:
            id: author identifier

        Examples:

            >>> pyskroutz.books(client).get_author(385).execute()

            <details>
                <summary>Response (as dictionary)</summary>
                <pre><code>
            {'author': {'bio': 'Η Joanne K. Rowling (Τζόαν Ρόουλινγκ) γεννήθηκε στο '
                               'Μπρίστολ το 1965. Άρχισε να γράφει την ιστορία του "Χάρι '
                               'Πότερ" σε ώρες πολύ δύσκολες. Ο "Χάρι Πότερ" εξελίχθηκε σε '
                               'βιβλίο-φαινόμενο. Τα δικαιώματα μετάφρασης πουλήθηκαν σε '
                               'ολόκληρο τον κόσμο και τα βραβεία ακολούθησαν το ένα το '
                               'άλλο: τρία βραβεία Νεστλέ-Σμάρτις, Γκάρντιαν, Σέφιλντ, '
                               'ΑΒΒΥ, Whitbread, Locus, Hugo, κ.ά., ενώ η συγγραφέας '
                               'ανακηρύχτηκε Βρετανίδα Συγγραφέας της Χρονιάς το 2000 και '
                               'τιμήθηκε για το σύνολο του έργου της το 2008. Οι ταινίες '
                               'με ήρωα τον "Χάρι Πότερ" έκαναν επίσης ρεκόρ εισιτηρίων '
                               'όπου προβλήθηκαν. Τα βιβλία του "Χάρι Πότερ" πούλησαν '
                               'περισσότερα από 250 εκατομμύρια αντίτυπα σε όλο τον κόσμο, '
                               'έχοντας μεταφραστεί σε 60 γλώσσες. H επιτυχία, μάλιστα, τη '
                               'συνοδεύει, μετά την ολοκλήρωση της σειράς, και στο πρώτο '
                               'της μυθιστόρημα για ενηλίκους, με τίτλο "The Casual '
                               'Vacancy", 2012 (ελλ. έκδ. "Ένας ξαφνικός θάνατος"), καθώς '
                               'και στο πρώτο της αστυνομικό μυθιστόρημα με ήρωα τον '
                               'ντετέκτιβ Κόρμοραν Στράικ, "The Cuckoo\'s Calling" ("Το '
                               'κάλεσμα του κούκου", 2013), που εξέδωσε με το ψευδώνυμο '
                               'Ρόμπερτ Γκαλμπρέιθ. Στηρίζει πολλούς φιλανθρωπικούς '
                               'σκοπούς μέσω του Φιλανθρωπικού Καταπιστεύματος Volant και '
                               'έχει ιδρύσει το Lumos, που στόχο έχει να βελτιώσει τη ζωή '
                               'των απόρων -και όχι μόνο- παιδιών. Για περισσότερες '
                               'πληροφορίες μπορείτε να επισκεφθείτε την προσωπική '
                               'ιστοσελίδα της συγγραφέως: www.jkrowling.com, καθώς και '
                               'την ιστοσελίδα: www.volanttrust.com',
                        'id': 385,
                        'image': HttpUrl('https://d.scdn.gr/ds/books/authors/385/20160721172728_1f8fd6c7.jpeg', scheme='https', host='d.scdn.gr', tld='gr', host_type='domain', path='/ds/books/authors/385/20160721172728_1f8fd6c7.jpeg'),
                        'name': 'J. K. Rowling'}}
                </code></pre>
            </details>
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}",
            model=books.BookAuthorRetrieve,
        )

    @fluent
    def get_author_books(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve Author Books

        Args:
            id: author identifier
            pag_params: pagination parameters

        Examples:

            Get the first two books from author with ID: `385`.
            >>> pyskroutz.books(client).get_author_books(385, per=2).execute()

            <details>
                <summary>Response (as dictionary)</summary>
                <pre><code>
            {'books': [{'id': 242327,
                        'images': {'alternatives': None,
                                   'main': HttpUrl('https://b.scdn.gr/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000242/242327/medium_20200219102603_o_chari_poter_kai_i_filosofiki_lithos.jpeg')},
                        'main_author': 'J. K. Rowling',
                        'main_author_id': 385,
                        'name': 'Ο Χάρι Πότερ και η φιλοσοφική λίθος',
                        'price_max': 12.96,
                        'price_min': 6.61,
                        'reviewable': True,
                        'reviews_count': 15,
                        'reviewscore': 4.93333,
                        'shop_count': 42,
                        'web_uri': HttpUrl('https://www.skroutz.gr/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/242327.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CF%86%CE%B9%CE%BB%CE%BF%CF%83%CE%BF%CF%86%CE%B9%CE%BA%CE%AE-%CE%BB%CE%AF%CE%B8%CE%BF%CF%82.html')},
                       {'id': 242082,
                        'images': {'alternatives': None,
                                   'main': HttpUrl('https://a.scdn.gr/images/sku_main_images/000242/242082/medium_20181123130007_o_chari_poter_kai_i_kamara_me_ta_mystika.jpeg', scheme='https', host='a.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000242/242082/medium_20181123130007_o_chari_poter_kai_i_kamara_me_ta_mystika.jpeg')},
                        'main_author': 'J. K. Rowling',
                        'main_author_id': 385,
                        'name': 'Ο Χάρι Πότερ και η κάμαρα με τα μυστικά',
                        'price_max': 14.4,
                        'price_min': 9.62,
                        'reviewable': True,
                        'reviews_count': 8,
                        'reviewscore': 4.5,
                        'shop_count': 43,
                        'web_uri': HttpUrl('https://www.skroutz.gr/books/242082.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CE%BA%CE%AC%CE%BC%CE%B1%CF%81%CE%B1-%CE%BC%CE%B5-%CF%84%CE%B1-%CE%BC%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/242082.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%B7-%CE%BA%CE%AC%CE%BC%CE%B1%CF%81%CE%B1-%CE%BC%CE%B5-%CF%84%CE%B1-%CE%BC%CF%85%CF%83%CF%84%CE%B9%CE%BA%CE%AC.html')}],
             'meta': {'available_filters': None,
                      'order_by': None,
                      'order_by_methods': None,
                      'pagination': {'page': 1,
                                     'per': 2,
                                     'total_pages': 11,
                                     'total_results': 21},
                      'personalization': None,
                      'sku_rating_breakdown': None,
                      'sku_reviews_aggregation': None}}
                </code></pre>
            </details>
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/author/{id}/books", model=books.BooksList, params=pag_params,
        )

    @fluent
    def get_similar_by_author(self, id: int, **pag_params: PaginationParams) -> None:
        """Retrieve similar Books by Author

        Args:
            id: author identifier
            pag_params: pagination parameters

        Examples:

            >>> pyskroutz.books(client).get_similar_by_author(242327, per=2).execute()

            <details>
                <summary>Response (as dictionary)</summary>
                <pre><code>
            {'books': [{'id': 107865,
                        'images': {'alternatives': None,
                                   'main': HttpUrl('https://d.scdn.gr/images/sku_main_images/000107/107865/medium_20160719175022_oi_istories_tou_mpintl_tou_vardou.jpeg', scheme='https', host='d.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000107/107865/medium_20160719175022_oi_istories_tou_mpintl_tou_vardou.jpeg')},
                        'main_author': 'J. K. Rowling',
                        'main_author_id': 385,
                        'name': 'Οι ιστορίες του Μπιντλ του Βάρδου',
                        'price_max': 7.92,
                        'price_min': 7.92,
                        'reviewable': True,
                        'reviews_count': 0,
                        'reviewscore': 0.0,
                        'shop_count': 1,
                        'web_uri': HttpUrl('https://www.skroutz.gr/books/107865.%CE%9F%CE%B9-%CE%B9%CF%83%CF%84%CE%BF%CF%81%CE%AF%CE%B5%CF%82-%CF%84%CE%BF%CF%85-%CE%9C%CF%80%CE%B9%CE%BD%CF%84%CE%BB-%CF%84%CE%BF%CF%85-%CE%92%CE%AC%CF%81%CE%B4%CE%BF%CF%85.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/107865.%CE%9F%CE%B9-%CE%B9%CF%83%CF%84%CE%BF%CF%81%CE%AF%CE%B5%CF%82-%CF%84%CE%BF%CF%85-%CE%9C%CF%80%CE%B9%CE%BD%CF%84%CE%BB-%CF%84%CE%BF%CF%85-%CE%92%CE%AC%CF%81%CE%B4%CE%BF%CF%85.html')},
                       {'id': 121274,
                        'images': {'alternatives': None,
                                   'main': HttpUrl('https://b.scdn.gr/images/sku_main_images/000121/121274/medium_20201103152340_o_chari_poter_kai_oi_kliroi_tou_thanatou.jpeg', scheme='https', host='b.scdn.gr', tld='gr', host_type='domain', path='/images/sku_main_images/000121/121274/medium_20201103152340_o_chari_poter_kai_oi_kliroi_tou_thanatou.jpeg')},
                        'main_author': 'J. K. Rowling',
                        'main_author_id': 385,
                        'name': 'Ο Χάρι Πότερ και οι κλήροι του θανάτου',
                        'price_max': 15.5,
                        'price_min': 10.32,
                        'reviewable': True,
                        'reviews_count': 3,
                        'reviewscore': 4.66667,
                        'shop_count': 48,
                        'web_uri': HttpUrl('https://www.skroutz.gr/books/121274.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%BF%CE%B9-%CE%BA%CE%BB%CE%AE%CF%81%CE%BF%CE%B9-%CF%84%CE%BF%CF%85-%CE%B8%CE%B1%CE%BD%CE%AC%CF%84%CE%BF%CF%85.html', scheme='https', host='www.skroutz.gr', tld='gr', host_type='domain', path='/books/121274.%CE%9F-%CE%A7%CE%AC%CF%81%CE%B9-%CE%A0%CF%8C%CF%84%CE%B5%CF%81-%CE%BA%CE%B1%CE%B9-%CE%BF%CE%B9-%CE%BA%CE%BB%CE%AE%CF%81%CE%BF%CE%B9-%CF%84%CE%BF%CF%85-%CE%B8%CE%B1%CE%BD%CE%AC%CF%84%CE%BF%CF%85.html')}],
             'meta': {'available_filters': None,
                      'order_by': None,
                      'order_by_methods': None,
                      'pagination': {'page': 1,
                                     'per': 2,
                                     'total_pages': 10,
                                     'total_results': 20},
                      'personalization': None,
                      'sku_rating_breakdown': None,
                      'sku_reviews_aggregation': None}}
            </code></pre>
        </details>
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/{self.ENDPOINT_PATH}/{id}/similar_by_author",
            model=books.BooksList, params=pag_params
        )

    @fluent
    def get_publisher(self, id: int) -> None:
        """Retrieve Book Publisher

        Args:
            id: publisher identifier

        Examples:

            >>> pyskroutz.books(client).get_publisher(78).execute()

            <details>
                <summary>Response (as dictionary)</summary>
            {'publisher': {'address': 'Τατοΐου 121 144 52 Μεταμόρφωση',
                           'email': 'info@psichogios.gr',
                           'fax': '210 2819550',
                           'id': 78,
                           'name': 'Ψυχογιός',
                           'phone': '210 2804800',
                           'website': 'www.psichogios.gr'}}
            </details>
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}", model=books.PublisherRetrieve
        )

    @fluent
    def get_publisher_books(self, id: int) -> None:
        """Retrieve Publisher Books

        Args:
            id: publisher identifier

        Examples:

            >>> pyskroutz.books(client).get_publisher_books(78).execute()

        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/publisher/{id}/books", model=books.BooksList
        )

    @fluent
    def get_book_categories(self) -> None:
        """Retrieve Book Categories

        Examples:

            >>> pyskroutz.books(client).get_book_categories().execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories", model=books.BookCategoriesList
        )

    def get_category(self, id: int) -> None:
        """Retrieve Book Category

        Args:
            id: book identifier

        Examples:

            >>> pyskroutz.books(client).get_category(1857).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}",
            model=books.BookCategoryRetrieve,
        )

    def get_category_books(
        self, id: int, order_by: Optional[str] = None, order_dir: Optional[str] = None
    ) -> None:
        """Retrieve Book Category's Books

        Args:
            id: category identifier

        Examples:

            >>> pyskroutz.books(client).get_category_books(1857).execute()
        """
        self._set_prepared_request(
            url=f"{self.BASE_URL}/book_categories/{id}/books", model=books.BooksList
        )
