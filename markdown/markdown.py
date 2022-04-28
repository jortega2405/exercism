from re import (sub, M, S)

def parse(markdown: str):
    str = markdown
    str = sub(r'__(.+?)__', r'<strong>\1</strong>', str)
    str = sub(r'_(.+?)_', r'<em>\1</em>', str)
    str = sub(r'^\* (.*?$)', r'<li>\1</li>', str, flags=M)
    str = sub(r'(<li>.*</li>)', r'<ul>\1</ul>', str, flags=S)
    for i in range(6, 0, -1):
        str = sub(r'^{} (.*?$)'.format('#' * i),
                r'<h{0}>\1</h{0}>'.format(i), str, flags=M)
    str = sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', str, flags=M)
    str = sub(r'\n', '', str)
    return str