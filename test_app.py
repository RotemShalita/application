import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/search" method="POST">' in rv.data.decode('utf-8')



