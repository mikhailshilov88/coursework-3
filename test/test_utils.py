from utils import filter_sort


def test_filter_sort():
    list_ = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2019-11-29T07:18:23.941293'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        }
    ]
    sorted_list = [
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-11-29T07:18:23.941293'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2019-11-29T07:18:23.941293'
        },
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2018-11-29T07:18:23.941293'
        }
    ]
    assert filter_sort(list_) == sorted_list