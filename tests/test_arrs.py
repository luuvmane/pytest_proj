from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"

    def test_get_negative_index():
        assert arrs.get([1, 2, 3], -1) == 3

    def test_get_negative_index_with_default():
        assert arrs.get([1, 2, 3], -1, "default") == "default"

    def test_get_index_out_of_range():
        assert arrs.get([1, 2, 3], 10) == None

    def test_get_index_out_of_range_with_default():
        assert arrs.get([1, 2, 3], 10, "default") == "default"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
def test_my_slice_with_negative_start():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]

def test_my_slice_with_negative_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]

def test_my_slice_with_negative_indices():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]

def test_my_slice_with_start_larger_than_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], start=3, end=1) == []

def test_my_slice_with_empty_list():
    assert arrs.my_slice([], 0, 3) == []

def test_my_slice_with_start_larger_than_list_length():
    assert arrs.my_slice([1, 2, 3, 4, 5], start=10) == []

def test_my_slice_with_end_larger_than_list_length():
    assert arrs.my_slice([1, 2, 3, 4, 5], end=10) == [1, 2, 3, 4, 5]