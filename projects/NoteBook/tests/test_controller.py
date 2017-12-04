#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tests.content import NoteService


def note_service_test():
    """Test service"""
    service = NoteService()
    data = service.list_all_note()
    for note in data:
        service.delete_all_note(note.user)

    assert service.create_note("1", "helloworld", "huang")
    data2 = service.list_all_note()
    assert data2[0].title == "1"
    assert data2[0].data == "helloworld"

    assert service.create_note("2", "hi= = = = ", "huang")
    assert not service.create_note("2", "", "huang")

    assert len(service.querry_note_by_title("1")) == 1
    assert len(service.querry_note_by_keyword("h")) == 2

    assert service.update_note_title("1", "11", "huang") == 1
    data2 = service.list_all_note()
    assert data2[0].title == "11"
    assert service.update_note_data("11", "hi- - - - ", "huang") == 1
    assert len(service.querry_note_by_keyword("hi")) == 2

    assert service.delete_note("2", "huang") == 1
    data2 = service.list_all_note()
    assert len(data2) == 1

    service.write_data()
    return data


def note_service_test2(data):
    """make data return"""
    service = NoteService()
    data2 = service.list_all_note()
    assert len(data2) == 1
    service.delete_all_note("huang")

    for note in data:
        service.create_note(note.title, note.data, note.user)
    service.write_data()

DATA = note_service_test()
note_service_test2(DATA)
