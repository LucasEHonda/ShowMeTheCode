import functools
from calls.models import Plan

class LabelCapitalizedMixin:
    @classmethod
    def get_label(cls, value):
        label = super().get_label(value)
        return label.capitalize()


class ChoiceAdapter:
    CHOICES = ()
    MAPPING = {}

    class_adapter = None

    def __init__(self, class_adapter):
        """
        On initializing this class, it defines the CHOICES and MAPPING attributes
        """
        self.class_adapter = class_adapter
        self.CHOICES = self.get_class_choices()
        self.MAPPING = self.get_mapping()

    def get_class_choices(self) -> tuple:
        return self.class_adapter.CHOICES

    def get_mapping(self) -> dict:
        mapping = {}
        excluded_keys = ["__dict__", "__doc__", "__module__", "__weakref__", "CHOICES"]

        items = dict(
            filter(
                lambda item: item[0] not in excluded_keys,
                self.class_adapter.__dict__.items(),
            )
        )

        for item in items:
            if isinstance(items[item], str):
                mapping[items[item]] = item.lower()

        return mapping

    @classmethod
    def get(cls, key):
        return cls.MAPPING.get(key.lower()) or cls.MAPPING.get(key.upper())

    @classmethod
    def get_choice_by_object_key(cls, key, optional=False):
        """Return a choice element by the object key"""
        if key is not None:
            adapter_value = cls.get_by_value(key)
            label = cls.get_label(key)

            return {"label": label, "value": adapter_value}

        if key is None and optional:
            return {"label": "Outros", "value": None}

    @classmethod
    @functools.lru_cache()
    def get_choices(cls, optional=False):
        default = [{"label": "Outros", "value": None}]
        options = [
            {"label": cls.get_label(value), "value": api_value}
            for api_value, value in cls.MAPPING.items()
        ]
        return default + options if optional else options

    @classmethod
    def get_label(cls, value):
        choices_dict = dict(cls.CHOICES)
        return choices_dict.get(value.lower()) or choices_dict.get(value.upper())

    @classmethod
    def get_by_value(cls, value):
        reverse_dict = {v: k for k, v in cls.MAPPING.items()}
        return reverse_dict.get(value.lower()) or reverse_dict.get(value.upper())

    @classmethod
    def get_options(cls):
        options = list(cls.MAPPING.keys())
        first = ", ".join(map(str, options[:-1]))
        last = options[-1]

        return "%(first)s or %(last)s" % dict(first=first, last=last)

class CallAdapter(LabelCapitalizedMixin, ChoiceAdapter):
    class_adapter = Plan
    __adapter = ChoiceAdapter(class_adapter)

    CHOICES = __adapter.CHOICES
    MAPPING = __adapter.MAPPING
