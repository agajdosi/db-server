import tornado.ioloop
import tornado.web
import sqlite3

PORT = 8888

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class BrowserPluginHandler(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/browser-plugin", BrowserPluginHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print(f"Tornado running on http://localhost:{PORT}")
    tornado.ioloop.IOLoop.current().start()
