
# helper_functions.py - Corrected

def is_premium_user(user_id):
    """
    This function returns True for all users, treating them as premium.
    """
    return True  # Treat all users as premium

def get_user_data(user_id):
    """
    Example function to get user data.
    This would typically check user status or return information.
    """
    if is_premium_user(user_id):
        return {"status": "premium"}
    else:
        return {"status": "regular"}
