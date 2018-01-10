from dao import BespokeDao
import sys


class BespokeModel:

    def __init__(self, collection):
        self._id = str(collection['_id']) if '_id' in collection else None
        self.name = collection['name'] if 'name' in collection else None
        self.sweetness = collection['sweetness'] if 'sweetness' in collection else None

    @staticmethod
    def get_by_id(_id):
        try:
            dao = BespokeDao()
            item = dao.get_by_id(_id)
            item_model = BespokeModel(item)
            return item_model if item else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def is_existing_name(name):
        try:
            dao = BespokeDao()
            exists = dao.get_by_name(name)
            return True if exists is not None else False
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def is_existing_id(_id):
        try:
            dao = BespokeDao()
            exists = dao.check_if_id_exists(_id)
            return True if exists is not None else False
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def is_valid(_id):
        try:
            return BespokeModel.is_existing_id(_id)
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def get_all():
        try:
            dao = BespokeDao()
            items = dao.get_all()
            model_array = []
            for i in items:
                model_array.append(BespokeModel(i))
            return model_array
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def update_item(_id, name, sweetness):
        try:
            dao = BespokeDao()
            item = dao.update_item(_id, name, sweetness)
            item_model = BespokeModel({'name': name, 'sweetness': sweetness, '_id': _id})if item else None
            return item_model
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def insert_item(name, sweetness):
        try:
            dao = BespokeDao()
            item = dao.insert_item(name, sweetness)
            item_model = BespokeModel(item) if item else None
            return item_model
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    @staticmethod
    def delete_item(_id):
        try:
            dao = BespokeDao()
            item = dao.get_by_id(_id)
            item_model = BespokeModel(item) if item else None
            dao.delete_item(item_model._id)
            return item_model
        except Exception as e:
            print(e, file=sys.stderr)
            raise
