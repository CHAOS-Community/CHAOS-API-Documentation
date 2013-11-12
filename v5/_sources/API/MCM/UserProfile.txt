UserProfile
===========

.. module:: MCM
   :noindex:

   .. extension:: UserProfile

      .. action:: Get

         Gets the profile of the current user or a specified user.

         :param metadataSchemaGuid: the GUID of the MetadataSchema that describes
                                    the user profile
         :param userGuid: the GUID of the user whose profile to get
         :type userGuid: optional

         If no ``userGuid`` is specified, the current user's profile is returned.

      .. action:: Set

         Sets the user profile of the current user or a specified user.

         :param metadataSchemaGuid: the GUID of the MetadataSchema that describes
                                    the user profile
         :param metadata: The XML representing the user profile
         :param userGuid: the GUID of the user whose profile to get
         :type userGuid: optional
         :returns: The number of affected rows in the database

         If no ``userGuid`` is specified, the current user's profile is set.
