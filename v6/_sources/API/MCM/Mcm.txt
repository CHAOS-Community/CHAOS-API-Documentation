Mcm
===

.. module:: MCM
   :noindex:

   .. extension:: Mcm

      .. action:: Index

	 (Re-)indexes all objects, a folder or a view.

	 :auth logged_in:
	 :param view: The name of the view to index (may be empty)
	 :param folderID: The ID of the folder to index
         :type folderID: optional
         :param cleanIndex: Removes objects from the index, before re-indexing
         :type cleanIndex: boolean, optional
         :returns: A ``Trace`` which is a list of lines with timings of the
                   different stages of the indexing
