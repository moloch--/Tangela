#!/usr/bin/env python
'''

@author: moloch

This is a collection of test cases for http://code.google.com/p/browsersec/

---------------------------------------------------------------------------------------
Copyright 2015

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
---------------------------------------------------------------------------------------
'''

import os
import time
import logging
import argparse
import tornado.log

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.escape import url_escape, url_unescape
from tornado.web import Application, RequestHandler, \
    StaticFileHandler, asynchronous


# Our working directory must be the app root
app_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(app_root)

# Dynamically generate the .html test file list
SERVER_PATH = "security_tests"  # This is only used for security tests
SECURITY_TESTS = sorted(
    filter(lambda test: test.endswith(".html") and not test.startswith("."),
           os.listdir(SERVER_PATH))
)

# Our crash test directory
CRASH_TESTS = sorted(
    filter(lambda test: test.endswith(".html") and not test.startswith("."),
           os.listdir("crash_tests"))
)


class HomeHandler(RequestHandler):

    def get(self):
        ''' Serves up the big list of tests '''
        self.render("templates/home.html",
                    security_tests=SECURITY_TESTS,
                    crash_tests=CRASH_TESTS)


class BrowserSecurityTests(RequestHandler):

    def get(self):
        self.render("templates/browsersec.html", tests=SECURITY_TESTS)


class BrowserCrashTests(RequestHandler):

    def get(self):
        self.render("templates/crashes.html", tests=CRASH_TESTS)


#
#  Server-side Logic for Security Tests
#
class ResponseCheck(RequestHandler):

    def get(self, *args):
        self.write(self.request.query)


class ResponseCheck2(RequestHandler):

    def get(self, *args):
        self.write(self.request.uri)


class ScriptResponse(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/javascript")
        self.write("var script_response = '%s';" % (
            url_escape(self.request.query)
        ))


class ScriptResponse2(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/javascript")
        self.write("var script_response2 = '%s';" % (
            url_escape(self.request.uri)
        ))


class PassManager(RequestHandler):

    ''' This test requires us to render the page with the SERVER_NAME, etc '''

    def get(self, *args):
        self.render("security_tests/pass_manager.html",
                    SERVER_NAME=self.application.settings['server_name'],
                    SERVER_PATH=SERVER_PATH)


class ReadPayloadPass(RequestHandler):

    def post(self, *args):
        self.render("security_tests/.read_payload_pass.html",
                    data=self.request.body)


class ChrPreced1(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/html; charset=iso-8859-2")
        self.render("security_tests/chr_preced1.html")


class ChrPreced2(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/html; charset=iso-8859-2")
        self.render("security_tests/chr_preced2.html")


class HtmlTagEquiv(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/html; charset=iso-8859-2")
        self.render("security_tests/html_tag_equiv.html")


class HtmlTagEquiv2(RequestHandler):

    def get(self, *args):
        self.set_header("Content-type", "text/html; charset=iso-8859-2")
        self.render("security_tests/html_tag_equiv2.html")


class GetTime(RequestHandler):

    @asynchronous
    def get(self, *args):
        io_loop = IOLoop.current()
        io_loop.add_timeout(io_loop.time() + 10, self.get_time)

    def get_time(self):
        self.set_header("Content-type", "text/plain")
        self.write(str(int(time.time())))
        self.finish()


class Stall(RequestHandler):

    @asynchronous
    def get(self, *args):
        io_loop = IOLoop.current()
        io_loop.add_timeout(io_loop.time() + (15 * 60), self.finish)


class ProbMisc(RequestHandler):

    def get(self, *args):
        self.render("security_tests/prob_misc.html",
                    SERVER_IP=self.application.settings["server_ip"],
                    SERVER_PATH=SERVER_PATH)


class ReturnCode(RequestHandler):

    def get(self, *args):
        self.set_header('HTTP/1.0', self.request.query + ' Foo')
        self.write("HELLO WORLD.")


class CookiesMisc(RequestHandler):

    def get(self, *args):
        self.set_header('Set-Cookie2', 'COOKIE2OK=YES; Version=1')
        self.set_header(
            'Set-Cookie',
            'COMMA1=1, COMMA2=comma2_noclobber; SEMI2=semi2_noclobber')
        self.set_header('Set-Cookie', 'hidethis=not_clobbered; httponly')
        self.render("security_tests/cookies_misc.html")


class AuthTest(RequestHandler):

    def get(self, *args):
        realm = url_unescape(self.request.query)
        if self.request.header["PHP_AUTH_USER"]:
            self.set_status(401)
            self.set_header("WWW-Authenticate", "basic realm=\"%s\"" % realm)
            self.write(
                "If you are seeing this text, authentication did not work.")
        else:
            self.write("If you are seeing this text, authentication worked.")


class AuthTestNTLM(RequestHandler):

    def get(self, *args):
        self.set_status(401)
        self.set_header("WWW-Authenticate", "NTLM")
        self.render("security_tests/.auth_test_ntlm.html")


class CanCookieP3p(RequestHandler):

    def get(self, *args):
        self.set_header("P3P", "CP=NOI NID NOR")
        self.render("security_tests/.can_cookie.html")


class Refresh(RequestHandler):

    def get(self, *args):
        self.set_header("Refresh", "0;URL=.refresh_target.html")


class ResponseCheckRaw(RequestHandler):

    def get(self, *args):
        ''' Very XSS, much secure '''
        self.write(self.request.query)


class ContentDispHtml(RequestHandler):

    def get(self, *args):
        self.set_header("Content-Type", "text/html")
        self.set_header("Content-Disposition", "attachment")
        self.render("security_tests/.cdisp_html.html")


class ContentDispImage(RequestHandler):

    def get(self, *args):
        self.set_header("Content-Type", "image/jpeg")
        self.set_header("Content-Disposition", "attachment")
        self.write("Test.")


class ReadHeader(RequestHandler):

    def get(self, *args):
        header = self.request.headers["HTTP_%s" % self.request.query]
        self.write(header)


class UrlCharsets2(RequestHandler):

    def get(self, *args):
        self.render("security_tests/url_charsets2.html",
                    SERVER_NAME=self.application.settings["server_name"],
                    SERVER_PATH=SERVER_PATH)


class UrlCharsets2b(RequestHandler):

    def get(self, *args):
        self.render("security_tests/.url_charsets2b.html",
                    QUERY_STRING=self.request.query,
                    REQUEST_URI=self.request.uri)


class CookieRestrictions(RequestHandler):

    def get(self, *args):
        alternate_name = self.application.settings["server_name_alt"]
        self.render("security_tests/cookie_restrictions.html",
                    SERVER_IP=self.application.settings["server_ip"],
                    SERVER_PATH=SERVER_PATH,
                    SERVER_NAME_ALT=alternate_name)


class MixedContent(RequestHandler):

    def get(self, *args):
        self.render("security_tests/mixed_content.html",
                    SERVER_NAME=self.application.settings["server_name"],
                    SERVER_PATH=SERVER_PATH)


class PortChars(RequestHandler):

    def get(self, *args):
        self.render("security_tests/port_chars.html")


#
#  Server-side Logic for Crash Tests
#
class ContextMenuCrash(RequestHandler):

    def get(self, *args):
        self.render("crash_tests/context_menu.html",
                    context_menu=self.lots_of_context)

    @property
    def lots_of_context(self):
        ''' Slightly ineffiecent in Py2 but what eves '''
        ls = []
        for index in range(100000):
            ls.append('<menuitem id="%i" label="STOP SNITCHIN"></menuitem>' % (
                index
            ))
        return ''.join(ls)


# URLs
application = Application([

    # Serves files for the home page
    (r"/", HomeHandler),
    (r"/browsersec", BrowserSecurityTests),
    (r"/crashes", BrowserCrashTests),
    (r"/static/(.*)", StaticFileHandler, {"path": "static/"}),

    # Servers the primary browser test files
    # Most of these are ugly regexes are for backwards compatability
    (r"/security_tests/\.response_check2(.*)", ResponseCheck2),
    (r"/security_tests/\.response_check(.*)", ResponseCheck),
    (r"/security_tests/\.script_response2(.*)", ResponseCheck2),
    (r"/security_tests/\.script_response(.*)", ResponseCheck),
    (r"/security_tests/pass_manager(|\.html)", PassManager),
    (r"/security_tests/\.read_payload_pass", ReadPayloadPass),
    (r"/security_tests/chr_preced1\.html", ChrPreced1),
    (r"/security_tests/chr_preced2\.html", ChrPreced2),
    (r"/security_tests/html_tag_equiv\.html", HtmlTagEquiv),
    (r"/security_tests/html_tag_equiv2\.html", HtmlTagEquiv2),
    (r"/security_tests/\.get_time(.*)", GetTime),
    (r"/security_tests/\.stall(.*)", Stall),
    (r"/security_tests/prob_misc\.html", ProbMisc),
    (r"/security_tests/\.return-code(.*)", ReturnCode),
    (r"/security_tests/\.auth_test(|\.php)", AuthTest),
    (r"/security_tests/\.auth_test_ntlm(|\.php)", AuthTestNTLM),
    (r"/security_tests/\.can_cookie_p3p(|\.php)", CanCookieP3p),
    (r"/security_tests/\.refresh(|\.php)", Refresh),
    (r"/security_tests/\.response_check_raw(|\.php)", ResponseCheckRaw),
    (r"/security_tests/\.cdisp_html(|\.php)", ContentDispHtml),
    (r"/security_tests/\.cdisp_image(|\.php)", ContentDispImage),
    (r"/security_tests/\.read_header(|\.php)", ReadHeader),
    (r"/security_tests/url_charsets2(|\.html)", UrlCharsets2),
    (r"/security_tests/\.url_charsets2b(.*)", UrlCharsets2b),
    (r"/security_tests/mixed_content(|\.html)", MixedContent),


    # Serves any remaining static test files
    (r"/security_tests/(.*)", StaticFileHandler, {"path": "security_tests/"}),

    # Serves the image files, user as part of the browser tests
    (r"/images/(.*)", StaticFileHandler, {"path": "security_tests/images/"}),

    # Serves various plug-in related files related to tests
    (r"/file_restrictions/(.*)", StaticFileHandler,
        {"path": "security_tests/file_restrictions/"}),

    # Crash Tests
    (r"/crash_tests/context_menu(\.html)", ContextMenuCrash),
    (r"/crash_tests/(.*)", StaticFileHandler, {"path": "crash_tests/"}),

],
    debug=False,
)


def tangela(args):
    ''' Main application entry point '''
    tornado.log.enable_pretty_logging()
    application.settings['server_name'] = args.server_name
    application.settings['server_ip'] = args.server_ip
    http_server = HTTPServer(application, xheaders=args.x_headers)
    http_server.listen(args.lport)
    if args.ssl_certfile is not None and args.ssl_keyfile is not None:
        logging.info("SSL server enabled, binding to %d" % args.ssl_lport)
        https_server = HTTPServer(application,
                                  ssl_options={
                                      "certfile": args.ssl_certfile,
                                      "keyfile": args.ssl_keyfile,
                                  },
                                  xheaders=args.x_headers)
        https_server.listen(args.ssl_lport)
    try:
        logging.info("Starting server on port %d ..." % args.lport)
        IOLoop.current().start()
    except KeyboardInterrupt:
        print("\r[!] User exit, stopping ...")
    finally:
        IOLoop.current().stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A collection of browser security tests',
    )
    parser.add_argument('--version', '-v',
                        action='version',
                        version='%(prog)s v0.0.1')
    parser.add_argument('--server-name', '-n',
                        help='server hostname (default: localhost)',
                        dest='server_name',
                        default='localhost')
    parser.add_argument('--server-name-alt', '-a',
                        help='alternate server hostname (default: )',
                        dest='server_name_alt',
                        default='')
    parser.add_argument('--server-ip', '-ip',
                        help='server ip address (default: 127.0.0.1)',
                        dest='server_ip',
                        default='127.0.0.1')
    parser.add_argument('--listen-port', '-l',
                        help='server listen port (default: 80)',
                        dest='lport',
                        default=80,
                        type=int)
    parser.add_argument('--ssl-certfile', '-c',
                        help='ssl certificate',
                        dest='ssl_certfile')
    parser.add_argument('--ssl-keyfile', '-k',
                        help='ssl key file',
                        dest='ssl_keyfile')
    parser.add_argument('--ssl-listen-port', '-s',
                        help='ssl listen port (default: 443)',
                        dest='ssl_lport',
                        default=443,
                        type=int)
    parser.add_argument('--x-headers', '-x',
                        help='honor x-forwarded-for and x-real-ip',
                        dest='x_headers',
                        action='store_true')
    tangela(parser.parse_args())
