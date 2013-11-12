Group
-----

.. module:: Portal
   :noindex:

   .. extension:: Group

      .. action:: Get

         Gets groups by guid or gets the groups a user belongs to.

         :auth logged_in:
         :optauth user_manager_permission: Requires the System.UserManager
                                           permission if you get the group of
                                           another user
         :param guid: GUID of the group you want to get
         :type guid: optional
         :param userGuid: GUID of the user whose groups you want to get
         :type userGuid: optional
         :returns: A list of groups

         If neither ``guid`` nor ``userGuid`` is given it returns the group of the
         user that is logged in. If ``guid`` is given then the group with the
         specific guid is returned. If ``userGuid`` is given, then the groups of
         the given user is returned.


      .. action:: Create

         Creates a new group.

         :auth logged_in:
         :auth create_group_permission:
         :param name: The name of the new group
         :param systemPermission: the permissions of the new group (an integer
                                  from the ``SystemPermissons`` struct)
         :type systemPermission: integer
         :returns: The created group

      .. action:: Delete

         Deletes a group.

         :auth logged_in:
         :param guid: The GUID of the group that should be deleted
         :returns: Number of affected rows in the database

      .. action:: Update

         Updates a group.

         :auth logged_in:
         :param guid: The GUID of the group that should be updated
         :param newName: The (new) name of the group
         :param newSystemPermission: new permissions for the group (an integer from the
                                     ``SystemPermissons`` struct)
         :type newSystemPermission: integer, optional
         :returns: Number of affected rows in the database

      .. action:: AddUser

         Adds a user to a group.

         :auth logged_in:
         :optauth user_manager_permission:
         :param guid: The GUID of the group that the user should be added to
         :param userGuid: The GUID of the user that should be added
         :param permissions: permissions for the new user (an integer from the
                                     ``SystemPermissons`` struct)
         :type permissions: integer
         :returns: Number of affected rows in the database

         If the user has UserManager permissions (SystemPermissons.UserManager)
         he will be able to add users to all groups. Otherwise he has to have
         the required permission for the specific group.

      .. action:: RemoveUser

         Removes a user from a group.

         :auth logged_in:
         :optauth user_manager_permission:
         :param guid: The GUID of the group that the user should be removed from
         :param userGuid: The GUID of the user that should be removed
         :returns: Number of affected rows in the database

         If the user has UserManager permissions (SystemPermissons.UserManager)
         he will be able to remove users from all groups. Otherwise he has to have
         the required permission for the specific group.

      .. action:: UpdateUserPermissions

         Adds a user to a group.

         :auth logged_in:
         :optauth user_manager_permission:
         :param guid: The GUID of the group to which the user's permissions
                      should be changed
         :param userGuid: The GUID of the user whose permissions should be
                          altered
         :param permissions: the new permissions for the user
                             (an integer from the ``SystemPermissons`` struct)
         :type permissions: integer
         :returns: Number of affected rows in the database

         If the user has UserManager permissions (SystemPermissons.UserManager)
         he will be able to change permissions for all users and all groups.
         Otherwise he has to have the required permission for the specific group.

