from ..exeptions import MixinIncompatibleException


class AbstractMixin:
    """Required attributes of class
    When class inited with this mixin, it will check if class has required attributes"""
    __mixin_required_parents__ = ()

    def __init_subclass__(cls, **kwargs):
        if AbstractMixin not in cls.__bases__:
            assert issubclass(cls, cls.__mixin_required_parents__), \
                MixinIncompatibleException(
                    f"{cls} must be {cls.__mixin_required_parents__} child"
                )
        return super(AbstractMixin, cls).__init_subclass__()
