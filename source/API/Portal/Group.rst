Group
-----

.. module:: Portal
   :noindex:

   .. extension:: Group

      .. action:: Get

         Gets the groups the current user belongs to.

         :auth logged_in:
         :returns: A list of groups

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
