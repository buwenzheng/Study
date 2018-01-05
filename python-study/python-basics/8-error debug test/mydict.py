class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    # 未找到属性的情况下调用
    def __getattr__(self, key):
        try:
            return self[key]
        # 没有属性的情况下抛异常
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
            
    # 设置属性值的时候调用
    def __setattr__(self, key, value):
        self[key] = value
