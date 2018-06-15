# -*- coding: utf-8 -*-
##############################################################################
#
#    openacademy module for OpenERP, Training Management
#    Copyright (C) 2014 OPENCREA (<http://www.opencrea.fr>) David Verove
#
#    This file is a part of openacademy
#
#    openacademy is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    openacademy is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Manual Execute for Ir Cron",
    'category': "",
    'version': '1.0',
    'depends': ['base'],
    'sequence': 900,
    'author': "Romain FAUQUET, contact@sirius-info.fr",
    'description': """Ajoute un bouton executer manuellement au tache planifier (ir_cron)
    """,
    'data': [
        'views/ir_cron_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
