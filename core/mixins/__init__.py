class AbstractMixin:
    """Required attributes of class
    When class inited with this mixin, it will check if class has required attributes"""
    required_attrs = ()

    def __init_subclass__(cls, **kwargs):
        super(AbstractMixin, cls).__init_subclass__()
