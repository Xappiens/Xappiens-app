# xappiens_app/overrides/budget.py
import frappe
from erpnext.accounts.doctype.budget.budget import Budget as ErpBudget

class Budget(ErpBudget):
    def validate_duplicate(self):
        # Si no hay cuentas, saltamos esta validación
        if not self.accounts:
            return
        super().validate_duplicate()
