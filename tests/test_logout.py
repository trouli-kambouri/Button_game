from flask import session

"""
if a user is currently logged in,
when they hit the GET /users/logout route
then the session is cleared, they are redirected to '/', 
and the navigation bar reverts to showing 'Login'.
 """


def test_logout_clears_session_and_redirects(web_client):
    
    with web_client.session_transaction() as sess:
        sess['user_id'] = 1
        sess['email'] = 'test@example.com'

    response = web_client.get('/users/logout', follow_redirects=True)

    assert response.status_code == 200
    
    assert 'user_id' not in session or session.get('user_id') is None
    assert 'email' not in session or session.get('email') is None


    html_content = response.data.decode('utf-8')
    assert "Login" in html_content
    assert "Sign Up" in html_content
    assert "Logged in as:" not in html_content