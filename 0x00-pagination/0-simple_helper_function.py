#!/usr/bin/env python3
"""
Given a list of items we want to break them down
into pages, and number of items in that particular list
"""


def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
