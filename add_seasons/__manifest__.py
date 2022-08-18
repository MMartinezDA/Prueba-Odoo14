{
    'name': 'Add Seasons',
    'summary': 'Module',
    'version': '14.0.1.0.0',
    'author': 'Datanalisis consultores',
    'website': 'https://www.smarthoreca.es/',
    'category': 'Sale',
    'depends': ['base','sale'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/account.xml',
        'views/account_payment_view.xml',
        'views/stock_picking_view.xml',
        'views/purchase_order_views.xml',
        'views/account_move_view.xml',
        'views/season_tag_menu.xml',
        'views/season_tag_view.xml',
    ],
    'qweb' : [
        'static/src/xml/account_payment.xml',
    ],
} 