UserSettings
============

.. module:: Portal
   :noindex:

   .. extension:: UserSettings

      .. action:: Get

         Gets settings for current user.

         :param clientGUID: GUID of the client for which to get settings
         :returns: The settings for the specified client for the current user
         :rtype: UserSettings

      .. action:: Set

         Sets settings for current user.

         :param clientGUID: GUID of the client for which to set settings
         :param settings: the new settings
         :type settings: string
         :returns: The number of affected rows in the database

      .. action:: Delete

         Delete settings for a specific client for the current user.

         :param clientGUID: GUID of the client for which to delete settings
         :returns: The number of affected rows in the database
