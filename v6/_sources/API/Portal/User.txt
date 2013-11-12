User
====

.. module:: Portal
   :noindex:

   .. extension:: User

      .. action:: Get

         Gets a single user or all users in a group

         :auth logged_in:
         :auth user_manager_permission:
         :param guid: GUID of the user to get
         :param groupGuid: GUID of the group whose users to get
         :returns: The a list of users
         :rtype: UserInfo

      .. action:: GetCurrent

         Gets the current user.

         :auth logged_in:
         :returns: The current (logged in) user
         :rtype: UserInfo

      .. action:: Create

         :auth logged_in:
         :auth user_manager_permission:
         :param guid: GUID for the new user
         :type guid: optional
         :param email: Email for the new user
         :returns: The new user

         If no GUID is supplied CHAOS will generate one for you.

      .. action:: Update

         Change email or permissions for a user.

         :auth logged_in:
         :optauth user_manager_permission:
         :param guid: GUID of the user to update
         :param email: (new) email for the user
         :param permissons: New permissions for the user (an integer from the ``SystemPermissons`` struct)
         :type permissons: optional, integer
         :returns: The updated user

         If your user has the ``SystemPermissons.UserManager`` permission, all users
         can be edited.
         If your user doesn't have this permission, you can edit your own users
         email, but not your own permissions.

         .. note:: The parameter is called *permissons* not *permissions*.

      .. action:: Delete

         Deletes a user

         :auth logged_in:
         :auth user_manager_permission:
         :param guid: GUID of the user to update
         :returns: The number of affected rows in the database

         Throws an exception if no user was deleted.
