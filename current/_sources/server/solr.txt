--------------------------------------------
External services: MySQL, Couchbase and Solr
--------------------------------------------
CHAOS depends on MySQL, Couchbase and Solr. These services can either run on the
same server as CHAOS or on another server that can be accessed from the CHAOS
server.

Setting up Solr
===============
Below are instructions for setting up Solr.

When you are done setting up Solr, you should set ``SOLR_URL`` in the
*Application Settings* of the IIS site. ``SOLR_URL`` is the URL where your Solr
service is available.

First you need to download and install the JDK (Java SE Development Kit).
http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html

Then download Solr: http://lucene.apache.org/solr/.

When you have downloaded Solr you start Solr directly by executing the command
:code:`java -jar solr-4.6.0/example/start.jar`.

This will start a Solr service on ``http://localhost:8983/solr``
In this scenario ``SOLR_URL`` should have the value  ``http://localhost:8983/solr``.

Go to ``http://localhost:8983/solr`` and select *Core Admin*. Here should
already be a ``Core`` called ``collection1``. Rename it to ``Object``.

You should name the core according to the :code:`<ObjectCoreName>` in the ``MCM``
settings in the ``Module`` table in the MySQL-database.


Setting up MySQL
================
Download MySQL: http://dev.mysql.com/downloads/mysql.
Install MySQL.

MySQL on Windows will by default have the option ``lower_case_table_names``
equal to ``1``, which can be problematic. We recommend changing this setting to
``0`` in either ``C:\ProgramData\MySQL\MySQL Server 5.6\my.ini`` or in *MySQL Workbench*.
(``MySQL Workbench -> Manage Server Instances -> [tab] System Profile -> Configuration File``)
(http://stackoverflow.com/a/17953456/118608)

Setting up Couchbase
====================
Download Couchbase (http://couchbase.com).
Install Couchbase.

In ``C:\CHAOS.Portal.Web\Web.config`` line 10-14:

.. code::

   <couchbase>
     <servers bucket="default" bucketPassword="">
       <add uri="http://localhost:8091/pools/default">
     </servers>
   </couchbase>

set the ``uri`` attribute to your Couchbase URL.

.. This guide sets up a Solr service on a Apache Tomcat server that is installed
   on the same server as CHAOS (a Windows 2008 server machine). You can however
   set up Solr on another machine or really any configuration you want as long the
   Solr service is reachable from the machine running CHAOS.


   First you need the JDK (Java SE Development Kit): download and install it.
   Download and install `Tomcat 7`_, I recommend the "32-bit/64-bit Windows Service
   Installer". Newer versions of Tomcat might work, but haven't been tested in this
   setup.

   Tomcat will by default be set up on http://localhost:8080/, you can go to this
   URL to see if it's running.

   Stop the Tomcat service (there should be a system tray icon where you can do
   this).

   Copy the Solr folder to ``C:\Solr``
   Copy ``C:\Solr\dist\apache-solr-4.6.0.war`` to ``C:\Program Files\Apache
   Software Foundation\Tomcat 7.0\webapps\solr.war``.

   Right-click on the Tomcat icon in the system tray, choose *Configure...*, then
   the click the *Java* tab. On the last line of *Java Options:* insert
   ``-DSolr.Solr.home=C:\Solr``.

   `Tomcat 7`_: http://tomcat.apache.org/download-70.cgi

   Reference:
   http://www.munsplace.com/blog/2012/02/20/installing-solr-on-windows7-x64


