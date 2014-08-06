# -*- coding: utf-8 -*-
"""
    test_api_translator
    ~~~~~~~~~~~~~~~~~~~

    Test the Sphinx API for translator.

    :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import sys

from nose.tools import with_setup

from util import with_app, test_roots


def setup_module():
    sys.path.insert(0, test_roots / 'test-api-set-translator')


def teardown_module():
    sys.path.remove(test_roots / 'test-api-set-translator')


def teardown_websupport():
    (test_roots / 'test-api-set-translator' / 'generated').rmtree(True)
    (test_roots / 'test-api-set-translator' / 'websupport').rmtree(True)


@with_app(
    buildername='html',
    srcdir=(test_roots / 'test-api-set-translator'),
    confdir=(test_roots / 'test-api-set-translator' / 'nonext'),
)
def test_html_translator(app):
    # no set_translator(), no html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'SmartyPantsHTMLTranslator'


@with_app(
    buildername='html',
    srcdir=(test_roots / 'test-api-set-translator'),
    confdir=(test_roots / 'test-api-set-translator' / 'nonext'),
    confoverrides={
        'html_translator_class': 'translator.ExtHTMLTranslator'},
)
def test_html_with_html_translator_class(app):
    # no set_translator(), but html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ExtHTMLTranslator'


@with_app(
    buildername='html',
    srcdir=(test_roots / 'test-api-set-translator'),
    confdir=(test_roots / 'test-api-set-translator' / 'nonext'),
    confoverrides={'html_use_smartypants': False},
)
def test_html_with_smartypants(app):
    # no set_translator(), html_use_smartypants=False
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'HTMLTranslator'


@with_app(
    buildername='html',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_html_(app):
    # use set_translator(), no html_translator_class
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfHTMLTranslator'


@with_app(
    buildername='html',
    srcdir=(test_roots / 'test-api-set-translator'),
    confoverrides={'html_translator_class': 'ext.ExtHTMLTranslator'},
)
def test_html_with_set_translator_for_html_and_html_translator_class(app):
    # use set_translator() and html_translator_class.
    # set_translator() is given priority over html_translator_clas.
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfHTMLTranslator'


## this test break test_websupport.test_comments test. why?
# @with_app(
#     buildername='dirhtml',
#     srcdir=(test_roots / 'test-api-set-translator'),
# )
# def test_dirhtml_set_translator_for_dirhtml(app):
#     translator_class = app.builder.translator_class
#     assert translator_class
#     assert translator_class.__name__ == 'ConfDirHTMLTranslator'


@with_app(
    buildername='singlehtml',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_singlehtml_set_translator_for_singlehtml(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfSingleHTMLTranslator'


@with_app(
    buildername='pickle',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_pickle_set_translator_for_pickle(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfPickleTranslator'


@with_app(
    buildername='json',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_json_set_translator_for_json(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfJsonTranslator'


@with_app(
    buildername='latex',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_latex(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfLaTeXTranslator'


@with_app(
    buildername='man',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_man(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfManualPageTranslator'


@with_app(
    buildername='texinfo',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_texinfo(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfTexinfoTranslator'


@with_app(
    buildername='text',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_text(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfTextTranslator'


@with_setup(teardown=teardown_websupport)
@with_app(
    buildername='websupport',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_websupport(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfWebSupportTranslator'


@with_app(
    buildername='xml',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_xml(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfXMLTranslator'


@with_app(
    buildername='pseudoxml',
    srcdir=(test_roots / 'test-api-set-translator'),
)
def test_html_with_set_translator_for_pseudoxml(app):
    translator_class = app.builder.translator_class
    assert translator_class
    assert translator_class.__name__ == 'ConfPseudoXMLTranslator'
