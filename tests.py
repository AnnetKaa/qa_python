import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    #проверяем, что книга добавлена в список books_genre
    def test_add_new_book_add_search_in_list(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert 'Гордость и предубеждение и зомби' in collector.books_genre

    #проверяем, что жанр добавлен в список
    def test_set_book_genre_add_search_in_directory(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert 'Фантастика' in collector.books_genre.values()

    #проверяем, что книге присвоен жанр
    def test_get_book_genre_assign_the_genre_correctly(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    #проверяем, что функция выводит список книг по жанру
    def test_get_books_with_specific_genre_successfully(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')

        assert ['Гордость и предубеждение и зомби', 'Гарри Поттер'] == collector.get_books_with_specific_genre('Фантастика')

    #проверка, что книги другого жанра не попападают в вывод функции
    def test_get_books_with_specific_genre_extra_genre_not_added(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')

        assert ['Гордость и предубеждение и зомби', 'Король Лев'] != collector.get_books_with_specific_genre('Фантастика')

    #проверяем, что в словаре добавлены имя фильма и жанр
    def test_get_books_genre_the_correct_list_is_displayed(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    #проверяем, что ужасы не добавлены в список для детей
    def test_get_books_for_children_horror_is_not_on_the_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        assert 'Кошмар на улице Вязов' not in collector.get_books_for_children()

    #проверяем, что добавление в список для детей проходит
    def test_get_books_for_children_adding_to_the_list_of_desired_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        assert len(collector.get_books_for_children()) == 1

    # проверяем, что книги добавляются в избранное
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
        assert collector.favorites

    #проверяем, что книги удаляются из избранного
    @pytest.mark.parametrize(
        'name',
        (
                'Гордость и предубеждение и зомби',
                'Гарри Поттер'
        )
    )
    def test_delete_book_from_favorites_successfully_deleted(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    #проверяем получения списка избранного
    def test_get_list_of_favorites_books_successful_output_of_a_list_of_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби']

