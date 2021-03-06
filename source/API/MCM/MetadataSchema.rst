MetadataSchema
==============

.. module:: MCM
   :noindex:

   .. extension:: MetadataSchema

      .. action:: Get

         Gets one or all MetadataSchemas in the database.

         :auth logged_in:
         :auth Read_permission: you will get the MetadataSchemas you have permission to read
         :param metadataSchemaGUID: the GUID of the schema to get
         :type metadataSchemaGUID: optional
         :returns: A list of MetadataSchemas

         If no ``metadataSchemaGUID`` is given, all MetadataSchemas which the user
         has rights to read are returned.

         .. code-editor:: xml

            <PortalResult Duration="24">
              <ModuleResults>
                <ModuleResult Fullname="MCM" Duration="0" Count="9">
                  <Results>
                    <Result FullName="CHAOS.MCM.Data.Dto.Standard.MetadataSchema">
                      <GUID>00000000-0000-0000-0000-000063c30000</GUID>
                      <Name>DKA</Name>
                      <SchemaXML>
                      <![CDATA[
                      <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified"><xs:element name="DKA"><xs:complexType><xs:sequence minOccurs="0" maxOccurs="unbounded"><xs:element name="Title" type="xs:string" /><xs:element name="Abstract" type="xs:string" /><xs:element name="Description" type="xs:string" /><xs:element name="Organization" type="xs:string" /><xs:element name="Type" type="xs:string" /><xs:element name="CreatedDate" type="xs:date" minOccurs="0" maxOccurs="unbounded" /><xs:element name="FirstPublishedDate" type="xs:dateTime" /><xs:element name="Identifier" type="xs:string" /><xs:element name="Contributor"><xs:complexType><xs:sequence><xs:element name="Person" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:attribute name="Name" type="xs:string" use="required" /><xs:attribute name="Role" type="xs:string" /></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="Creator"><xs:complexType><xs:sequence><xs:element name="Person" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:attribute name="Name" type="xs:string" use="required" /><xs:attribute name="Role" type="xs:string" /></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="TechnicalComment" type="xs:string" /><xs:element name="Location" type="xs:string" /><xs:element name="RightsDescription" type="xs:string" /><xs:element name="GeoData" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:sequence><xs:element name="Latitude" type="xs:decimal" /><xs:element name="Longitude" type="xs:decimal" /></xs:sequence></xs:complexType></xs:element><xs:element name="Categories"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="Category" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="Tags"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="Tag" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="Metafield" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:sequence><xs:element name="Key" type="xs:string" /><xs:element name="Value" type="xs:string" /></xs:sequence></xs:complexType></xs:element><xs:element name="ProductionID" type="xs:string" minOccurs="0" maxOccurs="unbounded" /><xs:element name="StreamDuration" type="xs:string" minOccurs="0" maxOccurs="unbounded" /></xs:sequence></xs:complexType></xs:element></xs:schema>
                      ]]>
                      </SchemaXML>
                      <DateCreated>09-04-2012 10:33:42</DateCreated>
                    </Result>
                  </Results>
                </ModuleResult>
              </ModuleResults>
            </PortalResult>

      .. action:: Create

         Adds a new MetadataSchema to the database.

         You need to be logged in to use this feature and the user must have
         administritive rights.

         :auth logged_in:
         :auth system_manage_permission:
         :param name: a new name for the new schema
         :param schemaXml: the XML for the new schema
         :param metadataSchemaGUID: the GUID for new schema
         :type metadataSchemaGUID: optional
         :returns: The GUID of the created MetadataSchema

         If no ``metadataSchemaGUID`` is given, CHAOS assigns a GUID to the new
         schema. The new GUID is returned as a result.

      .. action:: Update

         Updates a MetadataSchema in the database.

         :auth logged_in:
         :auth Write_permission: you need to have write-permissions to the MetadataSchema
         :param metadataSchemaGUID: the GUID of the schema to update
         :param name: a new (or the same) name for schema
         :param schemaXml: a new (or the same) XML for the schema
         :returns: The GUID of the updated MetadataSchema

      .. action:: Delete

         Deletes a MetadataSchema in the database.

         :auth logged_in:
         :auth Delete_permission: you need to have permissions delete the MetadataSchema
                                 (``MetadataSchemaPermission.Delete``)
         :param guid: the GUID of the schema to delete
         :returns: The number of affected rows in the database
