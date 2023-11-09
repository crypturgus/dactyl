from typing import Type

from django.db import models
from strawberry import type as strawberry_type


class DjangoModelMixin:
    # This mixin assumes that it's being used in a Django model class

    def to_strawberry(
        self: models.Model, strawberry_type: Type[strawberry_type]
    ) -> strawberry_type:
        # Get the names of the fields defined in the Strawberry type
        strawberry_fields = {
            field.name for field in strawberry_type.__strawberry_definition__.fields
        }

        # Collect field values from the Django model instance,
        # but only for fields present in the Strawberry type
        field_values = {
            name: getattr(self, name)
            for name in strawberry_fields
            if hasattr(self, name)
        }

        return strawberry_type(**field_values)
