---------------------
CHAOS server instance
---------------------
CHAOS is at heart a series of C# classes called "modules" running via an
HTTP server.

Therefore we recommend a settings up a Windows server running IIS, that can host
the CHAOS web application.

In the following guide we set up an Amazon EC2 instance, but you can use your
own local server or another service for hosting CHAOS.

Amazon EC2
==========
We recommend at least a ``m1.small``-instance running with the image
:code:`Microsoft Windows Server 2012 Base - ami-3937da4e (64-bit)`.
You can use a Windows Server 2008 as well, but it may have some
differences in the setup process. CHAOS is by
default 64-bit, but can be built and run on 32-bit instances if you
change paths in the build configuration from ``Framework64`` to ``Framework``.

I gave my instance a 30 GB EBS disk and made sure that port 3389 (RDP) was open
in the security group. These should be selected by default.
``RDP`` is the Remote Desktop Protocol so that we can access and manage the
instance.

When the instance has been set up, right-click on the server and choose ``Get
Windows Password``. This will present you with a username and password for the
machine. You can use this to "remote desktop" into the machine.

http://windows.microsoft.com/en-us/windows/connect-using-remote-desktop-connection#connect-using-remote-desktop-connection=windows-vista

Your remote desktop client will likely say that the certificate is
incorrect, but you can simply ignore that and connect anyway.

You don't need to tag the instance or give any special settings.

Windows Server 2012 instructions
================================
When you have logged in via the Remote Desktop client, you should be able to see
the desktop and some icons. In the lower left corner in the taskbar you should
see the icon for *Server Manager*: open it and go to *Add Roles*.
Add the roles *Application Server* and *Web Server (IIS)*.

Under *Web Server Role (IIS)* choose the feature *Web Server > Application
Development > .NET Extensibilty 4.5*.

Under *Application Server* choose the feature *Web Server (IIS) Support*.

This will install .Net 4.5 and IIS.

You can open IIS from the *Server Manager*.

Download and build CHAOS modules
================================
Download the sources for the CHAOS modules

In ``PowerShell`` (which can be found in the taskbar next to *Server Manager*)
you can open the web browser and navigate to the CHAOS Github repositories like
this:


.. code::

   explorer http://github.com/malthejorgensen/Portal-HttpModule
   explorer http://github.com/malthejorgensen/Portal
   explorer http://github.com/malthejorgensen/CHAOS.Portal.MCM
   explorer http://github.com/malthejorgensen/CHAOS.Portal.Authentication

Download and extract the code to the following folders:

.. code::

   C:\Portal-HttpModule
   C:\Portal
   C:\CHAOS.Portal.MCM
   C:\CHAOS.Portal.Authentication

To build the CHAOS modules run the following:

.. code::

   C:\Portal-HttpModule\build.bat
   C:\Portal\buil1d.bat
   C:\CHAOS.Portal.MCM\build.bat
   C:\CHAOS.Portal.Authentication\Build.bat

.. note::

   when you try to run ``build.bat`` you may have a permission error with ``nant``

   .. code::

      The action that failed was:
      Demand
      The type of the first permsission that failed was:
      System.Security.Permissions.FileIOPermission
      The Zone of the assembly that failed was:
      Internet

   this is because the files have been downloaded from the internet, and Windows
   sets special permissions (security zones) for those files. You can zip and then
   unzip the folder to remove the security zone. (See http://stackoverflow.com/a/9028795/118608)

* Copy :code:`C:\Portal-HttpModule\src\app\CHAOS.Portal.Web` to :code:`C:\CHAOS.Portal.Web`

.. note::

   If you choose another directory than :code:`C:\CHAOS.Portal.Web` you should
   change the variable ``ServiceDirectory`` in *Application Settings* in IIS
   accordingly. The variable can also be found and changed in the file :code:`CHAOS.Portal.Web\Web.config`.

* Create the folder :code:`C:\CHAOS.Portal.Web\Modules`
.. Copy :code:`C:\Portal\build\CHAOS.Portal.dll` to :code:`C:\CHAOS.Portal.Web\Modules`
* Copy :code:`C:\CHAOS.Portal.MCM\build\CHAOS.Mcm.dll` to :code:`C:\CHAOS.Portal.Web\Modules`
* Copy :code:`C:\CHAOS.Portal.Authentication\build\Chaos.Portal.Authentication.dll` to :code:`C:\CHAOS.Portal.Web\Modules`
* Copy :code:`C:\Portal-HttpModule\lib\CHAOS.dll` to :code:`C:\CHAOS.Portal.Web\bin\CHAOS.dll`
* Copy (overwrite) :code:`C:\Portal\lib\MySql.Data.dll` to :code:`C:\CHAOS.Portal.Web\bin\MySql.Data.dll`
-- as Portal-HttpModule has and old version of ``MySql.Data.dll``.

IIS
===
Open ``Internet Information Services (IIS) Manager`` and set up a new site.
(Right-click on sites and click *Add site...*)

In the *Physical path:* you should choose ``C:\CHAOS.Portal.Web``.

In either *Application Settings* in IIS or in the XML-file
``CHAOS.Portal.Web\Web.config`` you should edit the default ``ConnectionString``
to contain the credentials and location for your database.

.. IIS may say that you cannot override the configuration: this link may help
   you with ``http://stackoverflow.com/questions/9794985/iis-this-configuration-section-cannot-be-used-at-this-path-configuration-lock``

Set database settings
=====================
Run the MySQL-scripts that setup the tables and procedures the different CHAOS
mdoules. The following assumes that the MySQL server is running on
``localhost`` and that you have ``MySQL Workbench CE 6.0.8`` installed.
Furthermore it assumes that your database is called ``CHAOS`` and that a MySQL
user called ``CHAOS`` has access to it.

In Windows Powershell:

.. code-editor:: powershell

   > cd C:\Portal\sql
   > cat '1-create_tables.sql'     | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '3-create_procedures.sql' | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '4-create_views.sql'      | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '6-create_data.sql'       | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p

   > cd C:\CHAOS.Portal.MCM\sql
   > cat '1-create_tables.sql'     | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '2-apply_changes.sql'     | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '3-create_procedures.sql' | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '4-create_views.sql'      | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '6-insert_data.sql'       | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p

   > cd C:\CHAOS.Portal.Authentication\src\sql\Chaos.Portal.Authentication.Sql
   > cat '1-create_tables.sql'     | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '3-create_procedures.sql' | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p
   > cat '6-insert_data.sql'       | & 'C:\Program Files (x86)\MySQL\MySQL Workbench CE 6.0.8\mysql.exe' CHAOS -u CHAOS -p

.. `5.triggers/metadata_create_set_revisionid.sql` assumes the database is `MCM`
   ... here I have used the Portal database for the MCM tables so it fails
   * ``mysql Portal -u root -p < 5-create_triggers.sql``

In the ``Module`` table you need to add two rows, one for the :code:`MCM` and
:code:`Authentication` modules.

The XML-configuration of the ``MCM``-module should be:

.. code-editor:: xml

   <Settings>
     <ConnectionString>Server=localhost;Uid=CHAOS;Pwd=Foobaz123;Database=CHAOS</ConnectionString>
     <ObjectCoreName>Object</ObjectCoreName>
     <!-- AwsConfiguration Aws-->
     <!-- UserManagementConfiguration UserManagement -->
   </Settings>

And the XML-configuration of ``Authentication``-module:

.. code-editor:: xml

   <Settings>
     <ConnectionString>Server=localhost;Uid=CHAOS;Pwd=Foobaz123;Database=CHAOS</ConnectionString>
     <!--<Facebook>
       <AppId></AppId>
       <AppSecret></AppSecret>
     </Facebook>-->
   </Settings>

The values of the :code:`<ConnectionString>` should correspond to your MySQL-database settings.

Finishing touches
=================
Lastly we need some basic setup.
An administrator account has been automatically added to the ``User`` database.
It has the GUID :code:`34613336383661632d333562392d3131` and the email
:code:`admin`. Yes, the email is simply :code:`admin`. Yes, it is not a valid
email.

We now setup a:

* A root folder
* A password for the ``admin`` user
* Permission for the admin to the root folder

..  INSERT INTO `AccessPoint`
   VALUES (
     0x40219A3B7C8F428199044CF4EDB0DD9D, # GUID
     0x7F78F338D77D4814839794DC42101D06, # SubscriptionGUID
     "DefaultAP",                        # Name
     NOW()                               # DateCreated
   );

   INSERT INTO `Subscription`
   VALUES (
     0x7F78F338D77D4814839794DC42101D06, # GUID
     "DefaultSubscription",              # Name
     NOW()                               # DateCreated
   );

.. code-editor:: sql

   INSERT INTO `Folder`
   VALUES (
     1,      # ID
     NULL,   # ParentID
     1,      # FolderTypeID
     NULL,   # SubscriptionGUID
     "root", # Name
     NOW()   # DateCreated
   );

   INSERT INTO `Folder_User_Join`
   VALUES (
     1,                                  # FolderID
     0x34613336383661632d333562392d3131, # UserGUID (admin)
     255,                                # Permission
     NOW()                               # DateCreated
   );

   INSERT INTO `EmailPassword`
   VALUES (
       0x34613336383661632d333562392d3131,         # UserGUID (admin)
       "91554f150aff4801fa2e771a382fe0fc185f5f8c", # Password (SHA1(UTF-16("Foobaz123"))),
       NOW(),                                      # DateCreated
       NOW()                                       # DateModified
   );

You can now login with your :code:`admin` user (you should insert the
corresponding sessionGUID, of course):

* http://localhost/v6/Session/Create
* http://localhost/v6/EmailPassword/Login?email=admin&password=Foobaz123&sessionGUID=0a1b2b02-d531-4a36-a68f-bbba8f3bbd22

And create a new folder and an object in that folder:

* http://localhost/v6/Folder/Create?title=myfolder&folderTypeID=1&parentID=1&sessionGUID=0a1b2b02-d531-4a36-a68f-bbba8f3bbd22
* http://localhost/v6/Object/Create?objectTypeID=1&folderID=2&sessionGUID=0a1b2b02-d531-4a36-a68f-bbba8f3bbd22
