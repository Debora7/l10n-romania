from odoo.upgrade import util

def migrate(cr):
    module_name = 'l10n_ro_stock_account_notice'
    
    cr.execute("SELECT id FROM ir_module_module WHERE name = %s", (module_name,))
    if cr.fetchone():
        util.remove_module(cr, module_name)
        
        cr.execute(
            "UPDATE ir_module_module SET state = 'uninstalled' WHERE name = %s",
            (module_name,)
        )