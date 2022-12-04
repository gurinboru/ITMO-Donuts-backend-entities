from werkzeug.wrappers import Response
from logging import getLogger, StreamHandler, Formatter
import sys


class MiddleWare:
    def __init__(self, app):
        self.app = app

        self.logger = getLogger("middleware")
        self.logger.setLevel("INFO")
        handler = StreamHandler(sys.stdout)
        handler.setFormatter(Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]'))
        self.logger.addHandler(handler)

        self.logger.info("Middleware initialized")

    def __call__(self, environ, start_response):
        self.logger.info("Called path %s", environ["PATH_INFO"])
        try:
            return self.app(environ, start_response)
        except Exception as e:
            self.logger.error(f"Exception: {e} occurred in middleware layer while processing request "
                              f"{environ['PATH_INFO']} with method {environ['REQUEST_METHOD']}")
            res = Response(u'Internal Server Error', mimetype='text/plain', status=500, body=str(e))
            return res(environ, start_response)
