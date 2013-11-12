Format
======


.. module:: MCM
   :noindex:

   .. extension:: Format

      .. action:: Get

         Gets a file format.

         :auth logged_in:
         :param id: The ID of the format to get
         :type id: optional
         :param name: Name of the format to get

      .. action:: Create

         Creates a new file format.

         :auth logged_in:
         :param formatCategoryID: The ID of the FormatCategory the new Format
				  should
	                          be in
         :type formatCategoryID: optional
         :param name: The name of the format
         :param formatXml: ???
         :param mimeType: The mime-type of the new file format
         :param extension: The file extension of the new file format
