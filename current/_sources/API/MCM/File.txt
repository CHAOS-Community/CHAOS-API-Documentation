File
====

.. module:: MCM
   :noindex:

   .. extension:: File

      .. action:: Create

         Creates a new file.

         :auth logged_in:
         :auth CreateUpdateObjects_permission: The user has to have the
                                               ``FolderPermission.CreateUpdateObjects``
                                               permission for the object on
                                               which the file is created.
         :param objectGuid: The object to which the file should belong
         :param parentFileID: a parent file
         :type parentFileID: optional
         :param formatID: the FormatID of the file
         :param destinationID: The ID of the destination the file belongs to
         :param filename: the filename on the host, see :ext:`Destination`
                          extension
         :param originalFilename: the filename
         :param folderPath: the folder path on the host, see :ext:`Destination`
                            extension
         :returns: The created file

         The ``FormatID`` parameter is described in
         :ref:`Concepts -> Files <concepts-files>`.

      .. action:: Delete

         Deletes a file.

         :auth logged_in:
         :auth CreateUpdateObjects_permission: The user has to have the
                                               ``FolderPermission.CreateUpdateObjects``
                                               permission for the object to
                                               which the file belongs.
         :param id: the ID of the file to be deleted
         :type id: unsigned integer
         :returns: The number of affected rows in the database
