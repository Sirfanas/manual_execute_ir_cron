# coding: utf8

import sys

CHEMIN_ADDONS_SIRIUS = '/etc/librairie-python'
sys.path.append(CHEMIN_ADDONS_SIRIUS)

from sirius_lib.Metro.Models.drop_shipping.flux_rupture import *

from openerp.osv import fields, osv
from openerp import SUPERUSER_ID
import logging
import netsvc
from ftplib import FTP

_logger = logging.getLogger(__name__)


class IrCron(osv.osv):
    _inherit = 'ir.cron'

    def executer_manuellement(self, cr, uid, ids, context=None):
        for cron in self.browse(cr, uid, ids):
            requete = 'self.pool.get("' + cron.model + '").' + cron.function + '(cr, uid, context)'
            _logger.info("Requete manuelle de : " + requete)
            exec(requete)
        return True
