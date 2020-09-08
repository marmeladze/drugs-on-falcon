import falcon
from sqlalchemy.orm import sessionmaker

from .models import Drug, engine
from .serializer import DrugSerializer


serializer = DrugSerializer()

import json

Session = sessionmaker(bind=engine)
session = Session()


class IngredientsResource(object):
    def on_get(self, req, resp):
        item = req.params.get('q', '')
        limit = int(req.params.get('limit', 50))
        page = int(req.params.get('page', 1))
        if len(item) > 2:
            qry = session.query(Drug).filter(Drug.ingredient_name.ilike(f"%{item}%"))
            count = qry.count()
            drugs = qry.limit(limit).offset((page-1)*limit).all()
            message = f"Found {count} items for {item}"
            drugs = [serializer.serialize(drug) for drug in drugs]
            resp.body = json.dumps({'message': message, 'data':drugs}, ensure_ascii=False)
            resp.status = falcon.HTTP_200

        else:
            message = f"Couldn't found any items with name {item}"
            resp.body = json.dumps({'message': message, 'data':[]}, ensure_ascii=False)
            resp.status = falcon.HTTP_404


class ItemsResource(object):
    def on_get(self, req, resp):
        item = req.params.get('q', '')
        limit = int(req.params.get('limit', 50))
        page = int(req.params.get('page', 1))

        if len(item) > 2:
            qry = session.query(Drug).filter(Drug.item_name.ilike(f"%{item}%"))
            count = qry.count()
            drugs = qry.limit(limit).offset((page-1)*limit).all()
            message = f"Found {count} items for {item}"
            drugs = [serializer.serialize(drug) for drug in drugs]
            resp.body = json.dumps({'message': message, 'data':drugs}, ensure_ascii=False)
            resp.status = falcon.HTTP_200

        else:
            message = f"Couldn't found any items with name {item}"
            resp.body = json.dumps({'message': message, 'data':[]}, ensure_ascii=False)
            resp.status = falcon.HTTP_404


api = application = falcon.API()

items = ItemsResource()
ingredients = IngredientsResource()

application.add_route('/items', items)
application.add_route('/ingredients', ingredients)
