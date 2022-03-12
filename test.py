from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, get_doc_shelf, show_all_docs_info
import pytest


class TestSomething:

    @pytest.mark.parametrize('input_for_test, expected', (['11-2', True], ['10006', True], ['2207 876234', True], [11-2, False]))
    def test_check_document_existance(self, input_for_test, expected):
        assert check_document_existance(input_for_test) is expected
    
    @pytest.mark.parametrize('input_for_test, expected', (['11-2', 'Геннадий Покемонов'], ['10006', 'Аристарх Павлов'], ['2207 876234', 'Василий Гупкин'], [11-2, None]))
    def test_get_doc_owner_name(self, input_for_test, expected):
        assert get_doc_owner_name(input_for_test) == expected

    def test_get_all_doc_owners_names(self):
        expected = {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        assert get_all_doc_owners_names() == expected

    def test_show_all_docs_info(self):
        expected = '\npassport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\ninsurance 10006 Аристарх Павлов\n'
        assert show_all_docs_info() == expected

    @pytest.mark.parametrize('input_for_test, expected', (['2', False], ['4', True]))
    def test_add_new_shelf(self, input_for_test, expected):
        assert add_new_shelf(input_for_test) is expected

    @pytest.mark.parametrize('input_for_test, expected', (['10006', '2'], ['11-2', '1'], ['2207 876234', '1'], [11-2, None]))
    def test_get_doc_shelf(self, input_for_test, expected):
        assert get_doc_shelf(input_for_test) == expected
