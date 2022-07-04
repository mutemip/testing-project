def get_object_or_none(model, **kwargs):
    try:
        result = model.objects.get(**kwargs)
    except model.DoesNotExist:
        result = None
    return result
