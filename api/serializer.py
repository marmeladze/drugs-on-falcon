class DrugSerializer:

    def serialize(self, drug):
        return {
            'uuid': str(drug.uuid),
            'item_name': drug.item_name,
            'ingredient_name': drug.ingredient_name,
            'dosage_and_unit': drug.dosage_and_unit,
            'pharmaceutical_form': drug.pharmaceutical_form,
            'packaging': drug.packaging,
            'packaging_qty': drug.packaging_qty,
            'company': drug.company,
            'wholesale_price': drug.wholesale_price,
            'sale_price': drug.sale_price,
            'submitted_at': drug.submitted_at.strftime('%d.%m.%Y')        
        }


class RequestSerializer:
    def __init__(self, query=None, limit=50, page=1):
        self.query = query
        self.limit = limit
        self.page = page

    def build(self, **request):
        self.query = request["query"] or ""
        try:
            limit = int(request["limit"])
            self.limit = limit
        except Exception as e:
            pass

        try:
            page = int(request["page"])
            self.page = page
        except Exception as e:
            pass
        return self

