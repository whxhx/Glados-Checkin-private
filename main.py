import os
from glados_checkin import glados_check_in

serve = (os.environ['SERVE'] == 'on')
sc_key = os.environ['SERVE_KEY']
cookie = os.environ['COOKIE']


if __name__ == '__main__':
    glados_check_in(cookie, serve, sc_key)

