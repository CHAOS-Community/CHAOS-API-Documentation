Folder
======

.. module:: MCM
   :noindex:

   .. extension:: Folder

      .. action:: GetPermission

         Get permissions for a specific folder.

         :param folderID: the FolderID of the folder
         :type id: unsigned integer
         :returns: the permissions of the folder
         :rtype: FolderPermission:

      .. action:: SetPermission

         Sets the permissions for a specific user or group to a specific folder.

         :auth logged_in:
         :auth Folder_permissions: User must have permission to update the
                                   folder
         :param userGuid: the guid of the user whose permissions should be updated
         :type userGuid: optional
         :param groupGuid: the guid of the group whose permissions should be
                           updated
         :type groupGuid: optional
         :param folderID: the FolderID of the folder
         :type id: unsigned integer
         :param permission: the new permissions for the folder
         :type permission: unsigned integer
         :returns: The number of affected rows in the database

         Either ``userGuid`` or ``groupGuid`` must be given.

      .. action:: Get

         Gets a specific folder (``id``), all folders in a folder
         (``parentID``), or all the folders the current user has access to.

         :auth logged_in:
         :auth Folder_permission: The user has to have permission to read the
                                  folders. (``Permission.FolderPermission.Read``)
         :param id: the ID of the folder to get
         :type id: optional
         :param parentID: get all folders in the folder with this ID
         :type parentID: optional
         :param permission: Get only folders with these permissions
         :type permission: optional

         You may not specify both ``id`` and ``parentID`` at the same time.
         If neither ``id`` nor ``parentID`` is specified all folders the user
         has access to are returned. If ``permission`` is specified only folders
         with these permissions will be returned.

         .. Sending ``folderTypeID`` has no effect, so I've commented it out for
            now.
            :param folderTypeID:
            :type id: optional

      .. action:: Delete

         Deletes a folder.

         :auth logged_in:
         :auth Folder_permission: The user has to have permission to delete the
                                  folder. (``Permission.FolderPermission.Update``)
         :param id: the ID of the folder to delete
         :returns: The number of affected rows in the database

      .. action:: Update

         Updates a folder.

         :auth logged_in:
         :auth Folder_permission: The user has to have permission to update the
                                  folder. (``Permission.FolderPermission.Delete``)
         :param id: the ID of the folder to update
         :param newTitle: the (new) title of folder
         :type newTitle: string
         :param newFolderTypeID: the new FolderTypeID of the folder
         :type newFolderTypeID: optional
         :param newParentID: the ID of the new parent folder
         :type newParentID: optional
         :returns: The number of affected rows in the database

         If ``newParentID`` is specified the folder (with ID ``id``) is moved to
         the ``newParentID`` folder.

      .. action:: Create

         Creates a new folder.

         :auth logged_in:
         :optauth Folder_permission: If ``parentID`` is specified the user has
                                     to have permission to update the folder.
                                     (``Permission.FolderPermission.Write``)
         :optauth Subscription_permission: If ``subscriptionGuid`` is specified
                                           the has to have permission to create
                                           folders in the subscription.
                                           (``SubscriptionPermission.CreateFolder``))
         :param subscriptionGuid: the GUID of the subscription the folder should
                                  belong to
         :type subscriptionGuid: optional
         :param title: the title of the new folder
         :param folderTypeID: the FolderTypeID of the new folder
         :param parentID: the ID of the folder the new folder should be put into
         :type parentID: optional
         :returns: The new folder

         You must either specify either ``subscriptionGuid`` or ``parentID``.
