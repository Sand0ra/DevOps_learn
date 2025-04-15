import wsgiref.simple_server

def web_application(environ, start_response):
    response = b"Hello world!"
    status = "200 OK"
    headers = [
        ("Content-type", "text/html")
    ]
    start_response(status, headers)

    return [response]

if __name__ == "__main__":

    w_s = wsgiref.simple_server.make_server(
        "localhost",
        8080,
        web_application
    )
    w_s.handle_request()
