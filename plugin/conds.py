from flogin import Query
from flogin._types import SearchHandlerCondition


class MultiAnyCondition:
    r"""A builtin search condition to check for multiple conditions.

    This condition will only run if all given conditions return ``True``.
    See the :ref:`search handler section <search_handlers>` for more information about using search handlers and conditions.

    .. NOTE::
        This condition will set the query's :attr:`~flogin.query.Query.condition_data` attribute to a dictionary object where the key is the condition and the value is the extra data it provided.

    """

    __slots__ = ("conditions",)

    def __init__(self, *conditions: SearchHandlerCondition) -> None:
        self.conditions = conditions

    def __call__(self, query: Query) -> bool:
        for condition in self.conditions:
            if condition(query) is True:
                query.condition_data = condition
                return True

        return False
