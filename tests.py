import bs4

from beautifulsoup4_helpers import select_one, select_all, select_text_one

html_example = bs4.BeautifulSoup(f'''
    <html>
        <body>
            <div class="foo" attr-name="attr-value">bar</div>
            <div class="foo">bar2</div>
        </body>
    </html>
''', 'lxml')


def test_select_one_selecting_attribute():
    assert select_one(html_example, '.foo', 'attr-name') == "attr-value"


def test_select_one_selecting_innertext():
    assert select_one(html_example, 'div', 'text') == "bar"


def test_select_one_selecting_non_existing_tag():
    assert select_one(html_example, '.fooerror', 'attr-name', 'default') == 'default'


def test_select_one_selecting_non_existing_attribute():
    assert select_one(html_example, '.foo', 'attr-error', 'default') == 'default'


def test_select_text_one():
    assert select_text_one(html_example, '[attr-name="attr-value"]') == "bar"


def test_select_all():
    assert select_all(html_example, '.foo', 'text') == ['bar', 'bar2']
    assert select_all(html_example, 'div', 'attr-name') == ['attr-value']
