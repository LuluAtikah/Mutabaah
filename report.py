from openerp import osv, api, models, fields
from openerp import tools

class report(osv.osv):
    _name = "graph.report"
    _auto = False

    _columns = {
        'tanggal' : fields.date('Tanggal', readonly=True),
        'ashar' : fields. many2one('mutabaah.ashar', 'Ashar', readonly=True),
        'maghrib' : fields.many2one('mutabaah.maghrib', 'Maghrib', readonly=True),
        'isya' : fields.many2one('mutabaah.isya', 'Isya', readonly=True),
        'tilawah' : fields.many2one('mutabaah.tilawah', 'Tilawah', readonly=True),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'graph.report')
        cr.execute("""
            CREATE OR REPLACE VIEW graph.report AS (
            SELECT
                m.tanggal,
                m.ashar,
                m.maghrib,
                m.isya,
                m.tilawah
                FROM
                "mutabaah" m

            ) """
        )
