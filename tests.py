import pytest

from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_search_in_list(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert collector.get_books_genre(), {'Гордость и предубеждение и зомби': '', 'Что делать, если ваш кот хочет вас убить': ''}

    def test_set_book_genre_genre_added_to_the_directory(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби')

    def test_get_book_genre_assign_the_genre_correctly(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_successfully(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')

        assert ['Гордость и предубеждение и зомби', 'Гарри Поттер'] == collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre_the_correct_list_is_displayed(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_for_children_horror_is_not_on_the_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        assert 'Кошмар на улице Вязов' not in collector.get_books_for_children()

    def test_get_books_for_children_adding_to_the_list_of_desired_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        assert len(collector.get_books_for_children()) == 1

    @pytest.mark.parametrize(
        'name',
        (
                'Гордость и предубеждение и зомби',
                'Гарри Поттер',
                'Король Лев'
        )
    )
    def test_add_book_in_favorites_successfully_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_successfully_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert not collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_successful_output_of_a_list_of_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

