""" Utility functions and constants that will be used in the project.
"""

# Names of groups for users
ADMIN_GROUP = 'Admin'
AGENT_GROUP = 'Agent'
EXPORT_GROUP = 'Export'

def is_member(user, groups):
    """ Test if a user belongs to any of the groups provided.
    This function is meant to be used by the user_passes_test decorator to control access
    to views.
    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to a certain group.
    groups : list of str
        A list of the groups we are checking if the user belongs to.
    Returns
    ---------
    bool
        True if the user belongs to any of the groups. False otherwise
    """
    return any(map(lambda g: user.groups.filter(name=g).exists(), groups))


def is_admin(user):
    """ Test if a user has the admin group.
    This function is meant to be used by the user_passes_test decorator to control access
    to views. It uses the is_member function with a predefined list of groups.
    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to admin.
    Returns
    ---------
    bool
        True if the user has administrador as a group
    """
    return is_member(user, [ADMIN_GROUP])


def is_agent(user):
    """ Test if a user has the agent group.
    This function is meant to be used by the user_passes_test decorator to control access
    to views. It uses the is_member function with a predefined list of groups.
    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to agent.
    Returns
    ---------
    bool
        True if the user has agent as a group
    """
    return is_member(user, [AGENT_GROUP]) or is_admin(user)


def is_export(user):
    """ Test if a user has the export group.
    This function is meant to be used by the user_passes_test decorator to control access
    to views. It uses the is_member function with a predefined list of groups.
    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to agent.
    Returns
    -------
    bool
        True if the user has Export group
    """
    return is_member(user, [EXPORT_GROUP]) or is_admin(user)
