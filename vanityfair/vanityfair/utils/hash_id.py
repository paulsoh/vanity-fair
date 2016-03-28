from hashids import Hashids


def get_hash_id(instance):
    hashid_object = Hashids(
        salt=instance._meta.model_name,
        min_length=4,
    )
    hash_id = hashid_object.encode(instance.id)
    return hash_id
    

