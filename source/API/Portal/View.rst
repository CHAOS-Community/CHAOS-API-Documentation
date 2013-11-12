View
====

.. module:: Portal
   :noindex:

   .. extension:: View

      .. action:: Get

         Queries a specific view.

         :param view: name of the view to get
         :type view: string
         :param query: query for the view
         :returns: A list of objects

      .. action:: List

         Lists all available views.

         :param clientGUID: GUID of the client for which to set settings
         :param settings: the new settings
         :type settings: string
         :returns: The number of affected rows in the database
