import functools
from collections.abc import Callable
from typing import TypeVar, Any, cast

from new_movies.exceptions import ActionNotAllowed
from new_movies.user import Role, User

F = TypeVar("F", bound=Callable[..., Any])


def require_role(required_role: Role) -> Callable[[F], F]:
    def permissions_check_decorator(func: F) -> F:
        # @functools.wraps(func)
        def wrapper(acting_user: User, *args: Any, **kwargs: Any) -> Any:
            if acting_user.role is not required_role:
                raise ActionNotAllowed()
            return func(acting_user, *args, **kwargs)
        return cast(F, wrapper)
    return permissions_check_decorator

