# bedzie tylko token i ciul 
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"

def check_permission(user, permission):
    if not user.has_perm(permission):
        raise PermissionDenied("Nie masz odpowiednich uprawnień!!! ")