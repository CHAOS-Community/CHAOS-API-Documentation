Link
====

.. module:: MCM
   :noindex:

   .. extension:: Link

      Links are like shortcuts on Windows or symbolic links in Unix:
      they can make an Object appear in multiple folders by having "links" to
      the object in other folders than its parent folder.

      .. action:: Create

	 Creates a new link.

	 :auth logged_in:
	 :auth Permission_to_create_links: The user needs the ``FolderPermission.CreateLink``
					   on the object
	 :param objectGuid: The GUID of object on which to create the link
	 :param folderID: The ID of folder in which to
         :returns: The number of affected rows in the database

      .. action:: Update

	 Moves a link from one folder to another.

	 :auth logged_in:
	 :auth Permission_to_create_links: The user needs the ``FolderPermission.CreateLink``
					   on the object
	 :param objectGuid: The GUID of the object the link points to
	 :param folderID: The ID of the folder where link is currently residing
	 :param newFolderID: The ID of the folder where the link should be moved
			     to
         :returns: The number of affected rows in the database

      .. action:: Delete

	 Deletes a link.

	 :auth logged_in:
	 :auth Permission_to_create_links: The user needs the ``FolderPermission.CreateLink``
					   on the object
	 :param objectGuid: The GUID of the objects the link points to
	 :param folderID: The ID of folder in which link resides
         :returns: The number of affected rows in the database
