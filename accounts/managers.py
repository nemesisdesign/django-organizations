from django.db import models


class AccountManager(models.Manager):

    def active(self):
        return self.get_query_set().filter(is_active=True)

    def get_for_user(self, user):
        """
        Returns all matching `Account` objects

        user: a `User` object
        """
        return self.get_query_set().filter(users__user=user)

    def get_for_request(self, request):
        """
        Returns all matching `Account` objects

        request: an `HttpRequest` object
        """
        return self.get_query_set().filter(user__user=request.user)
