class BaseRepository:

    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        return self.model.objects.filter(pk=id).first()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, id, **kwargs):
        instance = self.get_by_id(id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            instance.save()
        return instance

    def delete(self, id):
        instance = self.get_by_id(id)
        if instance:
            instance.delete()
            return True
        return False
