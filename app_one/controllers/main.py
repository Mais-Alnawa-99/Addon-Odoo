


from odoo import http
from werkzeug.utils import redirect
from odoo.http import request

class PageMain(http.Controller):

    @http.route('/academy/academy/', auth="user", website=True, methods=['GET', 'POST'], csrf=False)
    def show_property(self, **kw):

        if http.request.httprequest.method == 'POST':
            new_record = request.env['show.properties'].sudo().create(kw)
            return redirect('/academy/academy/')
        return http.request.render('app_one.show')







