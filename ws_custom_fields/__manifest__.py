# coding: utf-8

{
    'name': 'Custom Fields',
    'version' : '1.0',
    'author' : 'CIEXPRO',
    'category' : 'Uncategorized',
    'description' : """

    - Add new fields in the modules
    - Add new scrap reason model to mp modules
 
    """,

    'depends': [
        'base','stock','mrp',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/stock_scrap_reason_view.xml',
    ],
    'installable': True,
}

