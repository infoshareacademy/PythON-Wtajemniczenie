from new_movies.user import Role


def has_role(role):
    def check_user(user):
        return user.role is role

    return check_user


is_admin = has_role(Role.ADMIN)
is_moderator = has_role(Role.MODERATOR)
