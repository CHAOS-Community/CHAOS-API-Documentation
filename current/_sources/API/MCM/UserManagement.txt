UserManagement
==============

.. module:: MCM
   :noindex:

   .. extension:: UserManagement

      Users can have their own folder and also their object.
      The ``UserManagement`` extension lets you create and access those.
      By having their own object a user can have metadata about themselves,
      and also have their own set of objects.

      .. action:: GetUserFolder

         Gets the folder of the current user or a specified user.

         :param userGuid: Get user folder of user with this GUID
         :type userGuid: optional
         :param createIfMissing: Create user folder if it doesn't exist
         :type createIfMissing: boolean, optional, default = true
         :returns: The user's folder

         If no ``userGuid`` is given the current user's user folder is returned.

      .. action:: GetUserObject

         Get the Object of the current user or a specified user.

         :param userGuid: Get the user object of the user with this GUID
         :type userGuid: optional
         :param createIfMissing: Create user object if it doesn't exist
         :type createIfMissing: boolean, optional, default = true
         :param includeMetata: Include metadata of the user object
         :type includeMetata: boolean, optional, default = false
         :param includeFiles: Include files of the user object
         :type includeFiles: boolean, optional, default = false
         :returns: A list of Objects

         If no ``userGuid`` is given the current user's user object is returned.
