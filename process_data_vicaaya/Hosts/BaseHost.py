class BaseHost(object):
    def __init__(self, _id, name, title, embed_link_pattern, meta_data):
        self._id = _id
        self.name = name
        self.title = title
        self.embed_link_pattern = embed_link_pattern
        self.ads_frequency = meta_data['ads_frequency']
        self.meta = meta_data
