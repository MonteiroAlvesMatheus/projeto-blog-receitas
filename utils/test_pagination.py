from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse
from utils.pagination import make_pagination_range


class PaginationTest(RecipeTestBase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        # 1 2 3 4 5 6 7 8 9 10
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa E501
        # current_page=1
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # current_page=2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # current_page=3
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']

        self.assertEqual([2, 3, 4, 5], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        # current_page=1
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # current_page=2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # current_page=1
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
